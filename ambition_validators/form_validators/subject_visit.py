from edc_constants.constants import OTHER
from edc_visit_tracking.constants import MISSED_VISIT, UNSCHEDULED
from edc_base.modelform_validators import FormValidator


class SubjectVisitFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            MISSED_VISIT,
            field='reason',
            field_required='reason_missed')

        self.required_if(
            UNSCHEDULED,
            field='reason',
            field_required='reason_unscheduled')

        self.required_if(
            OTHER,
            field='info_source',
            field_required='info_source_other')

        self.required_if(
            OTHER,
            field='reason_unscheduled',
            field_required='reason_unscheduled_other')
