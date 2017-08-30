from django import forms
from django.test import TestCase

from edc_constants.constants import YES, FEMALE, NOT_APPLICABLE, NO
from edc_base.modelform_validators import APPLICABLE_ERROR, REQUIRED_ERROR

from ..form_validators import SubjectScreeningFormValidator


class TestSubjectScreeningFormValidator(TestCase):

    def test_female_pregnancy_not_applicable_invalid(self):
        options = {
            'gender': FEMALE,
            'pregnancy': NOT_APPLICABLE}
        form_validator = SubjectScreeningFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('pregnancy',
                      form_validator._errors)
        self.assertIn(APPLICABLE_ERROR, form_validator._error_codes)

    def test_pregnancy_no_preg_test_date_invalid(self):
        options = {
            'pregnancy': NO,
            'preg_test_date': None}
        form_validator = SubjectScreeningFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('preg_test_date',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_female_breast_feeding_not_applicable_invalid(self):
        options = {
            'gender': FEMALE,
            'breast_feeding': NOT_APPLICABLE}
        form_validator = SubjectScreeningFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('breast_feeding',
                      form_validator._errors)
        self.assertIn(APPLICABLE_ERROR, form_validator._error_codes)
