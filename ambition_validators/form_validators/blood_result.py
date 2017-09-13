from django.forms import ValidationError, forms

from edc_base.modelform_validators import FormValidator
from edc_constants.constants import NO
from edc_base.modelform_validators.base_form_validator import NOT_REQUIRED_ERROR


class BloodResultFormValidator(FormValidator):

    def clean(self):

        creatinine_unit = self.cleaned_data.get('creatinine_unit')
        if ((creatinine_unit == 'umol/L')
                and '.' in str(self.cleaned_data.get('creatinine'))):
            raise ValidationError({
                'creatinine': 'Please provide a whole number for μmol/L units'})

        self.value_less_than(field='platelets', value=25)

        self.value_less_than(field='haemoglobin', value=6.5)

        self.value_less_than(field='absolute_neutrophil', value=0.5)

        self.value_less_than_equal(field='sodium', value=120)

        self.value_greater_than_equal(field='sodium', value=160)

        self.value_less_than(field='potassium', value=2)

        self.value_greater_than(field='potassium', value=7)

        self.value_greater_than(field='alt', value=350)

        self.value_less_than_with_units(
            field='magnesium', value=0.3, units_field='magnesium_unit', units='mmol/L')

        self.value_less_than_with_units(
            field='creatinine', value=4.55, units_field='creatinine_unit', units='mg/dL')

        self.value_greater_than_with_units(
            field='creatinine', value=400, units_field='creatinine_unit', units='umol/L')

        self.applicable_if(
            NO,
            field='are_results_normal',
            field_applicable='abnormal_results_in_ae_range')

    def value_less_than(self, field, value):
        if ((self.cleaned_data.get(field) and self.cleaned_data.get(field) < value)
                and self.cleaned_data.get('are_results_normal') not in NO):
            message = {
                'are_results_normal': f'{field} is abnormal, got '
                f'{self.cleaned_data.get(field)}. This field should be No.'}
            self._errors.update(message)
            self._error_codes.append(NOT_REQUIRED_ERROR)
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)

    def value_less_than_equal(self, field, value):
        if ((self.cleaned_data.get(field) and self.cleaned_data.get(field) <= value)
                and self.cleaned_data.get('are_results_normal') not in NO):
            message = {
                'are_results_normal': f'{field} is abnormal, got '
                f'{self.cleaned_data.get(field)}. This field should be No.'}
            self._errors.update(message)
            self._error_codes.append(NOT_REQUIRED_ERROR)
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)

    def value_greater_than(self, field, value):
        if ((self.cleaned_data.get(field) and self.cleaned_data.get(field) > value)
                and self.cleaned_data.get('are_results_normal') not in NO):
            message = {
                'are_results_normal': f'{field} is abnormal, got '
                f'{self.cleaned_data.get(field)}. This field should be No.'}
            self._errors.update(message)
            self._error_codes.append(NOT_REQUIRED_ERROR)
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)

    def value_greater_than_equal(self, field, value):
        if ((self.cleaned_data.get(field) and self.cleaned_data.get(field) >= value)
                and self.cleaned_data.get('are_results_normal') not in NO):
            message = {
                'are_results_normal': f'{field} is abnormal, got '
                f'{self.cleaned_data.get(field)}. This field should be No.'}
            self._errors.update(message)
            self._error_codes.append(NOT_REQUIRED_ERROR)
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)

    def value_less_than_with_units(self, field, value, units_field, units):
        if ((self.cleaned_data.get(field) and self.cleaned_data.get(field) < value)
                and self.cleaned_data.get(units_field) == units
                and self.cleaned_data.get('are_results_normal') not in NO):
            message = {
                'are_results_normal': f'{field} is abnormal, got '
                f'{self.cleaned_data.get(field)} {units}. This field should be No.'}
            self._errors.update(message)
            self._error_codes.append(NOT_REQUIRED_ERROR)
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)

    def value_greater_than_with_units(self, field, value, units_field, units):
        if ((self.cleaned_data.get(field) and self.cleaned_data.get(field) > value)
                and self.cleaned_data.get(units_field) == units
                and self.cleaned_data.get('are_results_normal') not in NO):
            message = {
                'are_results_normal': f'{field} is abnormal, got '
                f'{self.cleaned_data.get(field)} {units}. This field should be No.'}
            self._errors.update(message)
            self._error_codes.append(NOT_REQUIRED_ERROR)
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)
