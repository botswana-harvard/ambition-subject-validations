from django.apps import apps as django_apps
from django.conf import settings
from django.forms import forms

from edc_form_validators import FormValidator
from edc_constants.constants import NO, YES


class BloodResultFormValidator(FormValidator):

    def clean(self):
        # model_cls = django_apps.get_model(self.cleaned_data.get(
        # 'subject_visit')._meta.consent_model)

        # subject_identifier = self.cleaned_data.get(
        # 'subject_visit').subject_identifier
        #
        # gender = model_cls.objects.get(
        # subject_identifier=subject_identifier).gender

        self.range_gauge(
            field='haemoglobin',
            cleaned_data=self.cleaned_data,
            lower_bound=12.0, upper_bound=17.5,
            ae_grade_3_lower=6.5, ae_grade_3_upper=7.5,
            grade_4_high=False)

        self.creatinine(
            field='creatinine',
            cleaned_data=self.cleaned_data)

        self.range_gauge(
            field='magnesium', cleaned_data=self.cleaned_data,
            lower_bound=0.75, upper_bound=1.2,
            ae_grade_3_lower=0.3, ae_grade_3_upper=0.44,
            grade_4_high=False)

        self.range_gauge(
            field='potassium', cleaned_data=self.cleaned_data,
            lower_bound=3.6, upper_bound=5.2,
            ae_grade_3_lower=2.0, ae_grade_3_upper=2.4,
            grade_4_high=False)

        self.range_gauge(
            field='potassium', cleaned_data=self.cleaned_data,
            lower_bound=3.6, upper_bound=5.2,
            ae_grade_3_lower=6.6, ae_grade_3_upper=7.0,
            grade_4_high=True)

        self.range_gauge(
            field='sodium', cleaned_data=self.cleaned_data,
            lower_bound=135, upper_bound=145,
            ae_grade_3_lower=121, ae_grade_3_upper=124,
            grade_4_high=False)

        self.range_gauge(
            field='sodium', cleaned_data=self.cleaned_data,
            lower_bound=135, upper_bound=145,
            ae_grade_3_lower=155, ae_grade_3_upper=159,
            grade_4_high=True)

        self.range_gauge(
            field='alt', cleaned_data=self.cleaned_data,
            lower_bound=10, upper_bound=40,
            ae_grade_3_lower=177, ae_grade_3_upper=350,
            grade_4_high=True)

        self.range_gauge(
            field='platelets', cleaned_data=self.cleaned_data,
            lower_bound=150, upper_bound=450,
            ae_grade_3_lower=25, ae_grade_3_upper=51,
            grade_4_high=False)

        self.range_gauge(
            field='absolute_neutrophil', cleaned_data=self.cleaned_data,
            lower_bound=2.5, upper_bound=7.5,
            ae_grade_3_lower=0.5, ae_grade_3_upper=0.75,
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

        if (self.cleaned_data.get('are_results_normal') == NO
                and self.cleaned_data.get('abnormal_results_in_ae_range') == NO):
            raise forms.ValidationError({
                'abnormal_results_in_ae_range': 'Results are abnormal, they are '
                'considered to be within Grade III or IV range.'})

    def creatinine(self, field=None, cleaned_data=None):
        if (self.cleaned_data.get('creatinine_unit')
            and ((self.cleaned_data.get('creatinine_unit') == 'mg/dL'
                  and (self.cleaned_data.get(field) < 0.6
                       or self.cleaned_data.get(field) > 1.3)) or
                 (self.cleaned_data.get('creatinine_unit') ==
                  'umol/L' and (self.cleaned_data.get(field) < 53
                                or self.cleaned_data.get(field) > 115)))):
            if self.cleaned_data.get('are_results_normal') != NO:
                message = {
                    'are_results_normal': f'{field} is abnormal, got '
                    f'{self.cleaned_data.get(field)}. '
                    'This field should be No.'}
                raise forms.ValidationError(message)

    def range_gauge(self, field=None, cleaned_data=None, lower_bound=None,
                    upper_bound=None, ae_grade_3_lower=None, ae_grade_3_upper=None,
                    grade_4_high=None):
        """Method to validate for Grade 3 and Grade 4 results.

        grade_4_high = True if Grade 4 AE > ae_grade_3_upper.
        """
        if self.cleaned_data.get(field):
            if ((self.cleaned_data.get(field) > lower_bound
                 and self.cleaned_data.get(field) < upper_bound)
                    and self.cleaned_data.get('are_results_normal') != YES):
                message = {
                    'are_results_normal': f'Results are not within Grade III or IV range.'
                    ' This field should be Yes.'}
                raise forms.ValidationError(message)
            elif ((self.cleaned_data.get(field) > ae_grade_3_lower
                   and self.cleaned_data.get(field) < ae_grade_3_upper)
                    and self.cleaned_data.get('are_results_normal') != NO):
                message = {
                    'are_results_normal': f'{field} is abnormal and is Grade III AE, got '
                    f'{self.cleaned_data.get(field)}. '
                    'This field should be No.'}
                raise forms.ValidationError(message)
            elif (grade_4_high
                  and self.cleaned_data.get(field) > ae_grade_3_upper
                  and self.cleaned_data.get('are_results_normal') != NO):
                message = {
                    'are_results_normal': f'{field} is abnormal and is Grade IV AE, got '
                    f'{self.cleaned_data.get(field)}. '
                    'This field should be No.'}
            elif (not grade_4_high
                  and self.cleaned_data.get(field) < ae_grade_3_lower
                  and self.cleaned_data.get('are_results_normal') != NO):
                message = {
                    'are_results_normal': f'{field} is abnormal and is Grade IV AE, got '
                    f'{self.cleaned_data.get(field)}. '
                    'This field should be No.'}
                raise forms.ValidationError(message)
