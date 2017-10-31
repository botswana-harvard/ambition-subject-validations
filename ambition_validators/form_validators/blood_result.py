from django.forms import forms

from edc_base.modelform_validators import FormValidator
from edc_constants.constants import NO


class BloodResultFormValidator(FormValidator):

    def clean(self):

        self.creatinine(
            field='creatinine',
            cleaned_data=self.cleaned_data)
        self.sodium(
            field='sodium',
            cleaned_data=self.cleaned_data)
        self.potassium(
            field='potassium',
            cleaned_data=self.cleaned_data)
        self.magnesium(
            field='magnesium',
            cleaned_data=self.cleaned_data)

        if (self.cleaned_data.get('are_results_normal') == NO
                and self.cleaned_data.get('abnormal_results_in_ae_range') == NO):
            raise forms.ValidationError({
                'abnormal_results_in_ae_range': 'If results are abnormal, they '
                'are considered to be within Grade IV range.'})

    def creatinine(self, field=None, cleaned_data=None):
        if (self.cleaned_data.get('creatinine_unit')
            and ((self.cleaned_data.get('creatinine_unit') in 'mg/dL'
                  and (self.cleaned_data.get(field) < 0.6
                       or self.cleaned_data.get(field) > 1.3)) or
                 (self.cleaned_data.get('creatinine_unit') in
                  'umol/L' and (self.cleaned_data.get(field) < 53
                                or self.cleaned_data.get(field) > 115)))):
            if self.cleaned_data.get('are_results_normal') not in NO:
                message = {
                    'are_results_normal': f'{field} is abnormal, got '
                    f'{self.cleaned_data.get(field)}. '
                    'This field should be No.'}
                raise forms.ValidationError(message)

    def sodium(self, field=None, cleaned_data=None):
        if (self.cleaned_data.get(field)
                and self.cleaned_data.get(field)
                not in range(134, 144)):
            if self.cleaned_data.get('are_results_normal') not in NO:
                message = {
                    'are_results_normal': f'{field} is abnormal, got '
                    f'{self.cleaned_data.get(field)}. '
                    'This field should be No.'}
                raise forms.ValidationError(message)

    def potassium(self, field=None, cleaned_data=None):
        if (self.cleaned_data.get(field)
                and (self.cleaned_data.get(field) < 3.6
                     or self.cleaned_data.get(field) > 5.2)):
            if self.cleaned_data.get('are_results_normal') not in NO:
                message = {
                    'are_results_normal': f'{field} is abnormal, got '
                    f'{self.cleaned_data.get(field)}. '
                    'This field should be No.'}
                raise forms.ValidationError(message)

    def magnesium(self, field=None, cleaned_data=None):
        if (self.cleaned_data.get(field)
                and (self.cleaned_data.get(field) < 0.75
                     or self.cleaned_data.get(field) > 1.2)):
            if self.cleaned_data.get('are_results_normal') not in NO:
                message = {
                    'are_results_normal': f'{field} is abnormal, got '
                    f'{self.cleaned_data.get(field)}. '
                    'This field should be No.'}
                raise forms.ValidationError(message)
