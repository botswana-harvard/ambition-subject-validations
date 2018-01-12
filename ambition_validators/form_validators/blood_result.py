from ambition_labs.labs import cd4_panel, viral_load_panel, fbc_panel
from ambition_labs.labs import chemistry_panel, chemistry_alt_panel
from ambition_subject.constants import ALREADY_REPORTED
from arrow.arrow import Arrow
from django.apps import apps as django_apps
from django.conf import settings
from django.forms import forms
from django.utils import timezone
from edc_base.utils import convert_php_dateformat
from edc_constants.constants import NO, YES, NOT_APPLICABLE
from edc_form_validators import FormValidator
from edc_reportable import site_reportables, NotEvaluated, GRADE3, GRADE4


class BloodResultFormValidator(FormValidator):

    def clean(self):

        self.required_if_true(
            any([self.cleaned_data.get(f) is not None
                 for f in [f for f in self.instance.ft_fields]]),
            field_required='ft_requisition')

        ft_requisition = self.cleaned_data.get('ft_requisition')
        if ft_requisition and ft_requisition.panel_object not in [
                chemistry_panel, chemistry_alt_panel]:
            raise forms.ValidationError(
                {'ft_requisition': 'Incorrect requisition.'})

        self.required_if_true(
            self.cleaned_data.get('ft_requisition'),
            field_required='ft_assay_datetime')

        ft_assay_datetime = self.cleaned_data.get('ft_assay_datetime')
        self.validate_assay_datetime(
            ft_assay_datetime, ft_requisition, 'ft_assay_datetime')

        self.required_if_true(
            any([self.cleaned_data.get(f) is not None
                 for f in [f for f in self.instance.cbc_fields]]),
            field_required='cbc_requisition')

        cbc_requisition = self.cleaned_data.get('cbc_requisition')
        if cbc_requisition and cbc_requisition.panel_object != fbc_panel:
            raise forms.ValidationError(
                {'cbc_requisition': 'Incorrect requisition.'})

        self.required_if_true(
            self.cleaned_data.get('cbc_requisition'),
            field_required='cbc_assay_datetime')

        cbc_assay_datetime = self.cleaned_data.get('cbc_assay_datetime')
        self.validate_assay_datetime(
            cbc_assay_datetime, cbc_requisition, 'cbc_assay_datetime')

        self.required_if_true(
            self.cleaned_data.get('cd4') is not None,
            field_required='cd4_requisition')

        cd4_requisition = self.cleaned_data.get('cd4_requisition')
        if cd4_requisition and cd4_requisition.panel_object != cd4_panel:
            raise forms.ValidationError(
                {'cd4_requisition': 'Incorrect requisition.'})

        self.required_if_true(
            self.cleaned_data.get('cd4_requisition'),
            field_required='cd4_assay_datetime')

        cd4_assay_datetime = self.cleaned_data.get('cd4_assay_datetime')
        self.validate_assay_datetime(
            cd4_assay_datetime, cd4_requisition, 'cd4_assay_datetime')

        self.required_if_true(
            self.cleaned_data.get('vl') is not None,
            field_required='vl_requisition')

        vl_requisition = self.cleaned_data.get('vl_requisition')
        if vl_requisition and vl_requisition.panel_object != viral_load_panel:
            raise forms.ValidationError(
                {'vl_requisition': 'Incorrect requisition.'})

        self.required_if_true(
            self.cleaned_data.get('vl_requisition'),
            field_required='vl_assay_datetime')

        vl_assay_datetime = self.cleaned_data.get('vl_assay_datetime')
        self.validate_assay_datetime(
            vl_assay_datetime, vl_requisition, 'vl_assay_datetime')

        subject_identifier = self.cleaned_data.get(
            'subject_visit').subject_identifier
        RegisteredSubject = django_apps.get_model(
            'edc_registration.registeredsubject')
        subject_visit = self.cleaned_data.get('subject_visit')
        registered_subject = RegisteredSubject.objects.get(
            subject_identifier=subject_identifier)
        gender = registered_subject.gender
        dob = registered_subject.dob

        # check normal ranges and grade result values
        opts = dict(
            gender=gender, dob=dob, report_datetime=subject_visit.report_datetime)
        for field, value in self.cleaned_data.items():
            grp = site_reportables.get('ambition').get(field)
            if value and grp:
                self.evaluate_result(field, value, grp, **opts)

        # results_abnormal
        self.validate_final_assessment(
            field='results_abnormal', responses=[YES], suffix='_abnormal', word='abnormal')
        self.applicable_if(
            YES, field='results_abnormal',
            field_applicable='results_reportable')
        self.validate_final_assessment(
            field='results_reportable', responses=[GRADE3, GRADE4],
            suffix='_reportable', word='reportable')

        # TODO: Use site code to validate not country, Gaborone & Blantyre
        if (settings.COUNTRY not in ['botswana', 'malawi']
                and self.cleaned_data.get('bios_crag') != NOT_APPLICABLE):
            raise forms.ValidationError(
                {f'bios_crag': 'This field is not applicable'})

        self.applicable_if(
            YES,
            field='bios_crag',
            field_applicable='crag_control_result')

        self.applicable_if(
            YES,
            field='bios_crag',
            field_applicable='crag_t1_result')

        self.applicable_if(
            YES,
            field='bios_crag',
            field_applicable='crag_t2_result')

    def evaluate_result(self, field, value, grp, **opts):
        """Evaluate a single result value.

        Grading is done first. If the value is not gradeable,
        the value is checked against the normal limits.

        Expected field naming convention:
            * {field}
            * {field}_units
            * {field}_abnormal [YES, (NO)]
            * {field}_reportable [(NOT_APPLICABLE), NO, GRADE3, GRADE4]
        """
        abnormal = self.cleaned_data.get(f'{field}_abnormal')
        reportable = self.cleaned_data.get(f'{field}_reportable')
        units = self.cleaned_data.get(f'{field}_units')
        opts.update(units=units)
        if not units:
            raise forms.ValidationError(
                {f'{field}_units': f'Units required.'})
        try:
            grade = grp.get_grade(value, **opts)
        except NotEvaluated as e:
            raise forms.ValidationError({field: str(e)})
        if grade and grade.grade and reportable != str(grade.grade):
            if reportable != ALREADY_REPORTED:
                raise forms.ValidationError({
                    field: f'{field.upper()} is reportable. Got {grade.description}.'})
        elif not grade and reportable not in [NO, NOT_APPLICABLE]:
            raise forms.ValidationError({
                f'{field}_reportable': 'Invalid. Expected \'No\' or \'Not applicable\'.'})
        else:
            try:
                normal = grp.get_normal(value, **opts)
            except NotEvaluated as e:
                raise forms.ValidationError({field: str(e)})
            if not normal and abnormal == NO:
                descriptions = grp.get_normal_description(**opts)
                raise forms.ValidationError({
                    field:
                    f'{field.upper()} is abnormal. Normal ranges: {", ".join(descriptions)}'})
            elif normal and not grade and abnormal == YES:
                raise forms.ValidationError({
                    f'{field}_abnormal': 'Invalid. Result is not abnormal'})
        if abnormal == YES and reportable == NOT_APPLICABLE:
            raise forms.ValidationError(
                {f'{field}_reportable': 'This field is applicable if result is abnormal'})
        elif abnormal == NO and reportable != NOT_APPLICABLE:
            raise forms.ValidationError(
                {f'{field}_reportable': 'This field is not applicable'})

    def validate_final_assessment(self, field=None, responses=None, suffix=None, word=None):
        """Common code to validate fields `results_abnormal`
        and `results_reportable`.
        """
        answers = list({k: v for k, v in self.cleaned_data.items()
                        if k.endswith(suffix)}.values())
        if len([True for v in answers if v is not None]) == 0:
            raise forms.ValidationError(
                {'results_abnormal': f'No results have been entered.'})
        answers_as_bool = [True for v in answers if v in responses]
        if self.cleaned_data.get(field) == NO:
            if any(answers_as_bool):
                are = 'is' if len(answers_as_bool) == 1 else 'are'
                raise forms.ValidationError(
                    {field: f'{len(answers_as_bool)} of the above results {are} {word}'})
        elif self.cleaned_data.get(field) == YES:
            if not any(answers_as_bool):
                raise forms.ValidationError(
                    {field: f'None of the above results are {word}'})

    def validate_assay_datetime(self, assay_datetime, requisition, field):
        if assay_datetime:
            assay_datetime = Arrow.fromdatetime(
                assay_datetime, assay_datetime.tzinfo).to('utc').datetime
            if assay_datetime < requisition.requisition_datetime:
                formatted = timezone.localtime(requisition.requisition_datetime).strftime(
                    convert_php_dateformat(settings.SHORT_DATETIME_FORMAT))
                raise forms.ValidationError({
                    field: (f'Invalid. Cannot be before date of '
                            f'requisition {formatted}.')})
