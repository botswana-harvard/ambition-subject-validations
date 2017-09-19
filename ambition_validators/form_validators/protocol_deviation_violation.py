from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, OTHER

from ..constants import DEVIATION
from edc_base.modelform_validators.base_form_validator import NOT_REQUIRED_ERROR
from django.forms import forms


class ProtocolDeviationViolationFormValidator(FormValidator):

    def clean(self):

        self.validate_other_specify(
            field='protocol_violation_type',
            other_specify_field='protocol_violation_type_other',
            other_stored_value=OTHER)

        field_required_list = [
            'date_violation_datetime',
            'protocol_violation_type',
            'violation_description',
            'violation_reason']
        for field_required in field_required_list:
            self.not_required_if(
                DEVIATION,
                field='deviation_or_violation',
                field_required=field_required)

        self.required_if(
            YES,
            field='participant_safety_impact',
            field_required='participant_safety_impact_details')
 
        self.required_if(
            YES,
            field='study_outcomes_impact',
            field_required='study_outcomes_impact_details')
 
        if (self.cleaned_data.get('corrective_action_datetime') and not
                self.cleaned_data.get('corrective_action')):
            message = {
                'corrective_action': 'This field is required.'}
            self._errors.update(message)
            self._error_codes.append(NOT_REQUIRED_ERROR)
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)
 
        if (self.cleaned_data.get('preventative_action_datetime') and not
                self.cleaned_data.get('preventative_action')):
            message = {
                'preventative_action': 'This field is required.'}
            self._errors.update(message)
            self._error_codes.append(NOT_REQUIRED_ERROR)
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)
