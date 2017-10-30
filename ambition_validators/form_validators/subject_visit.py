from ambition_validators.form_validators import appointment
from django.forms import ValidationError
from edc_base.modelform_validators import REQUIRED_ERROR, NOT_REQUIRED_ERROR
from edc_constants.constants import OTHER
from edc_visit_tracking.constants import MISSED_VISIT, UNSCHEDULED
from edc_visit_tracking.form_validators import VisitFormValidator


class SubjectVisitFormValidator(VisitFormValidator):

    def clean(self):
        condition = (
            self.cleaned_data.get('appointment')
            and self.cleaned_data.get('appointment').visit_code_sequence == 0)

        if condition and self.cleaned_data.get('reason') in [UNSCHEDULED]:
            message = {
                'reason': 'Visit cannot be unscheduled.'}
            self._errors.update(message)
            self._error_codes.append(REQUIRED_ERROR)
            raise ValidationError(message, code=REQUIRED_ERROR)

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
