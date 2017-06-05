from edc_base.modelform_mixins import RequiredFieldValidationMixin
from edc_constants.constants import YES, OTHER


class ProtocolDeviationViolation(RequiredFieldValidationMixin):

    def __init__(self, cleaned_data=None):
        self.cleaned_data = cleaned_data

    def clean(self):
        self.required_if(
            YES,
            field='participant_safety_impact',
            field_required='participant_safety_impact_details')
        self.required_if(
            YES,
            field='study_outcomes_impact',
            field_required='study_outcomes_impact_details')
        self.required_if(
            OTHER,
            field='protocol_violation_type',
            field_required='other_protocol_violation_type')
