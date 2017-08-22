from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER

from ..constants import TUBERCULOSIS


class DeathReportFormValidator(FormValidator):

    def clean(self):
        self.required_if(
            OTHER,
            field='cause_of_death',
            field_required='cause_of_death_other')

        self.required_if(
            TUBERCULOSIS,
            field='cause_of_death',
            field_required='tb_site')
