from edc_visit_tracking.form_validators import VisitFormValidator
from edc_constants.constants import YES, NO, OTHER


class SubjectVisitFormValidator(VisitFormValidator):

    def clean(self):

        self.required_if(
            OTHER,
            field='reason_unscheduled',
            field_required='reason_unscheduled_other')
