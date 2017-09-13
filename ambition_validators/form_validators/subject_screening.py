from django.forms import forms
from edc_base.modelform_validators import FormValidator
from edc_base.modelform_validators.base_form_validator import REQUIRED_ERROR
from edc_constants.constants import FEMALE, YES, NO, MALE, NOT_APPLICABLE


class SubjectScreeningFormValidator(FormValidator):

    def clean(self):

        condition = (
            self.cleaned_data.get('gender') == FEMALE and
            self.cleaned_data.get('pregnancy') in [YES, NO])

        self.required_if_true(
            condition=condition, field_required='preg_test_date')

        self.applicable_if(
            FEMALE,
            field='gender',
            field_applicable='pregnancy')

        self.applicable_if(
            FEMALE,
            field='gender',
            field_applicable='breast_feeding')
