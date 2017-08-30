from edc_base.modelform_validators import FormValidator
from edc_constants.constants import FEMALE, YES, NOT_APPLICABLE


class SubjectScreeningFormValidator(FormValidator):

    def clean(self):
        self.applicable_if(
            FEMALE,
            field='gender',
            field_applicable='pregnancy')

        self.not_required_if(
            NOT_APPLICABLE,
            field='pregnancy',
            field_required='preg_test_date')

        self.applicable_if(
            FEMALE,
            field='gender',
            field_applicable='breast_feeding')
