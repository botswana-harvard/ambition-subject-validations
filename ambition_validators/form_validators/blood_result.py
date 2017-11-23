from django.apps import apps as django_apps
from django.forms import forms

from edc_form_validators import FormValidator
from edc_constants.constants import NO


class BloodResultFormValidator(FormValidator):

    def clean(self):
        model_cls = django_apps.get_model(self.cleaned_data.get(
            'subject_visit')._meta.consent_model)

        subject_identifier = self.cleaned_data.get(
            'subject_visit').subject_identifier

        gender = model_cls.objects.get(
            subject_identifier=subject_identifier).gender

        if gender == 'M':
            self.range_gauge(
                field='haemoglobin', cleaned_data=self.cleaned_data,
                lower_bound=13.5, upper_bound=17.5)
        elif gender == 'F':
            self.range_gauge(
                field='haemoglobin', cleaned_data=self.cleaned_data,
                lower_bound=12.0, upper_bound=15.5)

        self.creatinine(
            field='creatinine',
            cleaned_data=self.cleaned_data)

        self.range_gauge(
            field='magnesium', cleaned_data=self.cleaned_data,
            lower_bound=0.75, upper_bound=1.2)

        self.range_gauge(
            field='potassium', cleaned_data=self.cleaned_data,
            lower_bound=3.6, upper_bound=5.2)

        self.range_gauge(
            field='sodium', cleaned_data=self.cleaned_data,
            lower_bound=135, upper_bound=145)

        self.range_gauge(
            field='alt', cleaned_data=self.cleaned_data,
            lower_bound=10, upper_bound=40)

        self.range_gauge(
            field='platelets', cleaned_data=self.cleaned_data,
            lower_bound=150, upper_bound=450)

        self.range_gauge(
            field='absolute_neutrophil', cleaned_data=self.cleaned_data,
            lower_bound=2500, upper_bound=7500)

        if (self.cleaned_data.get('are_results_normal') == NO
                and self.cleaned_data.get('abnormal_results_in_ae_range') == NO):
            raise forms.ValidationError({
                'abnormal_results_in_ae_range': 'If results are abnormal, they '
                'are considered to be within Grade IV range.'})

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

    def range_gauge(self, field=None, cleaned_data=None,
                    lower_bound=None, upper_bound=None):
        if (self.cleaned_data.get(field)
                and (self.cleaned_data.get(field) < lower_bound
                     or self.cleaned_data.get(field) > upper_bound)):
            if self.cleaned_data.get('are_results_normal') != NO:
                message = {
                    'are_results_normal': f'{field} is abnormal, got '
                    f'{self.cleaned_data.get(field)}. '
                    'This field should be No.'}
                raise forms.ValidationError(message)
