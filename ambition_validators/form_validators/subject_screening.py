from edc_base.modelform_validators import FormValidator
from edc_constants.constants import FEMALE, YES, NO


class SubjectScreeningFormValidator(FormValidator):

    def clean(self):
        condition = self.cleaned_data.get('gender') == FEMALE
        self.required_if_true(
            condition=condition, field_required='pregnancy_or_lactation')

        preg = self.cleaned_data.get('pregnancy_or_lactation') in [YES, NO]
        self.required_if_true(
            condition=preg,
            field='pregnancy_or_lactation',
            field_required='preg_test_date')
