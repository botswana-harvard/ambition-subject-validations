from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER

from ..constants import TUBERCULOSIS


class DeathReportFormValidator(FormValidator):

    def clean(self):

        self.validate_other_specify(
            field='cause_of_death',
            other_specify_field='cause_of_death_other',
            other_stored_value=OTHER)

        self.required_if(
            TUBERCULOSIS,
            field='cause_of_death',
            field_required='tb_site')
