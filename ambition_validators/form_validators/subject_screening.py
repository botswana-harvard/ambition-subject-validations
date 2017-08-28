from edc_base.modelform_validators import FormValidator
from edc_constants.constants import FEMALE


class SubjectScreeningFormValidator(FormValidator):

    def clean(self):
        self.required_if(
            FEMALE,
            field='gender',
            field_required='pregnancy_or_lactation')
