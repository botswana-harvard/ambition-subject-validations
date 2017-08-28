from django import forms
from django.test import TestCase, tag

from edc_base.utils import get_utcnow
from edc_constants.constants import MALE, YES, NOT_APPLICABLE
from edc_base.modelform_validators import NOT_REQUIRED_ERROR

from ..form_validators import SubjectScreeningFormValidator


class TestSubjectScreeningFormValidator(TestCase):
    @tag('999')
    def test_gender(self):
        options = {
            'gender': MALE,
            'pregnancy': YES}
        form_validator = SubjectScreeningFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('pregnancy',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    @tag('999')
    def test_preg_test_date(self):
        options = {
            'pregnancy': NOT_APPLICABLE,
            'preg_test_date': get_utcnow}
        form_validator = SubjectScreeningFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('preg_test_date',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)
