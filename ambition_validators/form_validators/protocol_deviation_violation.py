from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, OTHER

from ..constants import DEVIATION


class ProtocolDeviationViolationFormValidator(FormValidator):

    def clean(self):
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

        self.required_if(
            OTHER,
            field='protocol_violation_type',
            field_required='other_protocol_violation_type')
