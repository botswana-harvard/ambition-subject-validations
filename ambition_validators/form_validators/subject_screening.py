from edc_base.modelform_validators import FormValidator
from edc_constants.constants import MALE, NOT_APPLICABLE, YES, NO


class SubjectScreeningFormValidator(FormValidator):

    def clean(self):
        self.not_required_if(
            MALE,
            field='gender',
            field_required='pregnancy')

        self.required_if_true(
            condition=(self.cleaned_data.get(
                'pregnancy') in [YES, NO]),
            field_required='preg_test_date')

        self.not_required_if(
            NOT_APPLICABLE,
            field='pregnancy',
            field_required='preg_test_date'
        )
