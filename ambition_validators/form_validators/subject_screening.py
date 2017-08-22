from edc_base.modelform_validators import FormValidator
from edc_constants.constants import FEMALE, YES


class SubjectScreeningFormValidator(FormValidator):

    def clean(self):
        self.required_if(
            FEMALE,
            field='gender',
            field_required='pregnancy_or_lactation')

        self.required_if(
            YES,
            field='pregnancy_or_lactation',
            field_required='preg_test_date')
