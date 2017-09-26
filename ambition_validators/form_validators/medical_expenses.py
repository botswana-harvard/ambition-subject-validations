from django.forms import forms
from edc_base.modelform_validators import FormValidator
from edc_base.modelform_validators.base_form_validator import NOT_REQUIRED_ERROR
from edc_constants.constants import YES, NO, NOT_APPLICABLE


class MedicalExpensesFormValidator(FormValidator):

    def clean(self):
        condition = self.cleaned_data.get(
            'patient_history') and self.cleaned_data.get(
                'patient_history').care_before_hospital == YES

        dependencies = [
            'location_care', 'transport_form',
            'care_provider', 'paid_treatment',
            'medication_bought', 'other_place_visited']

        not_required_dependencies = [
            'transport_cost', 'transport_duration',
            'paid_treatment_amount', 'medication_payment'
        ]

        self.validate_other_specify(field='location_care')

        self.validate_other_specify(field='care_provider')

        for dependency in dependencies:
            self.applicable_if_true(
                condition,
                field_applicable=dependency,
            )

        for dependency in not_required_dependencies:
            self.only_not_required_if(
                NO,
                field='care_before_hospital',
                field_required=dependency,
                cleaned_data=self.cleaned_data
            )

        self.required_if(
            YES,
            field='paid_treatment',
            field_required='paid_treatment_amount')

        self.required_if(
            YES,
            field='medication_bought',
            field_required='medication_payment')

    def only_not_required_if(self, *responses, field=None, field_required=None,
                             cleaned_data=None):

        if (self.cleaned_data.get('patient_history') and getattr(
                self.cleaned_data.get('patient_history'), field) in responses
                and (cleaned_data.get(field_required)
                     and cleaned_data.get(field_required) != NOT_APPLICABLE)):
            message = {
                field_required: 'This field is not required.'}
            self._errors.update(message)
            self._error_codes.append(NOT_REQUIRED_ERROR)
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)
