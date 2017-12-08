from django.apps import apps as django_apps
from django.conf import settings
from django.forms import forms

from edc_form_validators import FormValidator
from edc_constants.constants import NO, YES, MALE, FEMALE


class BloodResultFormValidator(FormValidator):

    def clean(self):

        subject_identifier = self.cleaned_data.get(
            'subject_visit').subject_identifier
        RegisteredSubject = django_apps.get_model(
            'edc_registration.registeredsubject')
        registered_subject = RegisteredSubject.objects.get(
            subject_identifier=subject_identifier)
        if registered_subject.gender == MALE:
            self.range_gauge(
                field='haemoglobin',
                lower_bound=13.5, upper_bound=17.5,
                ae_grade_3_lower=7.0, ae_grade_3_upper=9.0,
                grade_4_high=False)
        elif registered_subject.gender == FEMALE:
            self.range_gauge(
                field='haemoglobin',
                lower_bound=12.0, upper_bound=15.5,
                ae_grade_3_lower=6.5, ae_grade_3_upper=8.5,
                grade_4_high=False)
        else:
            raise ValueError(f'gender is unknown! See {repr(self)}')

        if self.cleaned_data.get('creatinine_unit') == 'mg/dL':
            self.range_gauge(
                field='creatinine',
                lower_bound=0.6, upper_bound=1.3,
                ae_grade_3_lower=2.47, ae_grade_3_upper=4.42,
                grade_4_high=True)
        if self.cleaned_data.get('creatinine_unit') == 'umol/L':
            self.range_gauge(
                field='creatinine',
                lower_bound=53, upper_bound=115,
                ae_grade_3_lower=216, ae_grade_3_upper=400,
                grade_4_high=True)

        if self.cleaned_data.get('magnesium'):
            self.range_gauge(
                field='magnesium',
                lower_bound=0.75, upper_bound=1.2,
                ae_grade_3_lower=0.3, ae_grade_3_upper=0.44,
                grade_4_high=False)

        self.range_gauge(
            field='potassium',
            lower_bound=3.6, upper_bound=5.2,
            ae_grade_3_lower=2.0, ae_grade_3_upper=2.4,
            grade_4_high=False)

        self.range_gauge(
            field='potassium',
            lower_bound=3.6, upper_bound=5.2,
            ae_grade_3_lower=6.5, ae_grade_3_upper=7.0,
            grade_4_high=True)

        if self.cleaned_data.get('sodium') < 135:
            self.range_gauge(
                field='sodium',
                lower_bound=135, upper_bound=145,
                ae_grade_3_lower=121, ae_grade_3_upper=124,
                grade_4_high=False)
        else:
            self.range_gauge(
                field='sodium',
                lower_bound=135, upper_bound=145,
                ae_grade_3_lower=154, ae_grade_3_upper=159,
                grade_4_high=True)

        self.range_gauge(
            field='alt',
            lower_bound=10, upper_bound=40,
            ae_grade_3_lower=200, ae_grade_3_upper=400,
            grade_4_high=True)

        self.range_gauge(
            field='platelets',
            lower_bound=150, upper_bound=450,
            ae_grade_3_lower=25, ae_grade_3_upper=51,
            grade_4_high=False)

        self.range_gauge(
            field='absolute_neutrophil',
            lower_bound=2.5, upper_bound=7.5,
            ae_grade_3_lower=0.4, ae_grade_3_upper=0.59,
            grade_4_high=False)

        # TODO: Use site code to validate not country, Gaborone & Blantyre
        condition = settings.COUNTRY == 'botswana' or settings.COUNTRY == 'malawi'
        self.applicable_if_true(
            condition=condition, field_applicable='bios_crag')

        self.required_if(
            YES,
            field='bios_crag',
            field_required='crag_control_result')

        self.required_if(
            YES,
            field='bios_crag',
            field_required='crag_t1_result')

        self.required_if(
            YES,
            field='bios_crag',
            field_required='crag_t2_result')

    def range_gauge(self, field=None, lower_bound=None,
                    upper_bound=None, ae_grade_3_lower=None, ae_grade_3_upper=None,
                    grade_4_high=None):
        """Method to validate for Grade 3 and Grade 4 results.

        grade_4_high = True if Grade 4 AE > ae_grade_3_upper.
        """
        valid_result = (self.cleaned_data.get(field) > lower_bound
                        and self.cleaned_data.get(field) < upper_bound)

        within_grade_3 = (self.cleaned_data.get(field) > ae_grade_3_lower
                          and self.cleaned_data.get(field) < ae_grade_3_upper)

        grade_4_gt = self.cleaned_data.get(field) > ae_grade_3_upper

        grade_4_lt = self.cleaned_data.get(field) < ae_grade_3_lower

        if (not within_grade_3 and not grade_4_gt and not grade_4_lt
                and valid_result
                and self.cleaned_data.get('are_results_normal') != YES):
            message = {
                'are_results_normal': f'Results are not within Grade III or IV range.'
                ' This field should be Yes.'}
            raise forms.ValidationError(message)

        elif (within_grade_3
                and self.cleaned_data.get('are_results_normal') != NO):
            message = {
                'are_results_normal': f'{field} is abnormal and is Grade III AE, got '
                f'{self.cleaned_data.get(field)}. '
                'This field should be No.'}
            raise forms.ValidationError(message)

        elif (grade_4_high
              and grade_4_gt
              and self.cleaned_data.get('are_results_normal') != NO):
            message = {
                'are_results_normal': f'{field} is abnormal and is Grade IV AE, got '
                f'{self.cleaned_data.get(field)}. '
                'This field should be No.'}
            raise forms.ValidationError(message)

        elif (not grade_4_high
              and grade_4_lt
              and self.cleaned_data.get('are_results_normal') != NO):
            message = {
                'are_results_normal': f'{field} is abnormal and is Grade IV AE, got '
                f'{self.cleaned_data.get(field)}. '
                'This field should be No.'}
            raise forms.ValidationError(message)
        else:
            if (self.cleaned_data.get('are_results_normal') == NO
                    and self.cleaned_data.get('abnormal_results_in_ae_range') != YES):
                message = {
                    'abnormal_results_in_ae_range': 'Results are within Grade III '
                    'or IV. This field should be Yes.'}
                raise forms.ValidationError(message)
