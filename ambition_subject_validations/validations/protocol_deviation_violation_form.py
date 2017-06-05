from edc_constants.constants import YES, OTHER

from .form_mixins import SubjectModelFormMixin
from ..models import ProtocolDeviationViolation


class ProtocolDeviationViolationForm(SubjectModelFormMixin):

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

    class Meta:
        model = ProtocolDeviationViolation
        fields = '__all__'
