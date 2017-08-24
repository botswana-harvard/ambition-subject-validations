from django import forms
from django.test import TestCase

from edc_constants.constants import YES, FEMALE
from edc_base.modelform_validators import REQUIRED_ERROR

from ..form_validators import SubjectScreeningFormValidator


class TestSubjectScreeningFormValidator(TestCase):

    def test_gender(self):
        options = {
            'gender': FEMALE,
            'pregnancy_or_lactation': None}
        form_validator = SubjectScreeningFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('pregnancy_or_lactation',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)
