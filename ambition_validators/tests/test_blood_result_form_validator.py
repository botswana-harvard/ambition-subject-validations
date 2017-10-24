from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_constants.constants import YES, NO

from ..form_validators import BloodResultFormValidator


@tag('br')
class TestBloodResultFormValidator(TestCase):

    def test_no_creatinine_mg_invalid(self):
        cleaned_data = {
            'creatinine': 0.3,
            'creatinine_unit': None,
            'are_results_normal': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_creatinine_mg_invalid(self):
        cleaned_data = {
            'creatinine': 0.3,
            'creatinine_unit': 'mg/dL',
            'are_results_normal': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_creatinine_mg(self):

        cleaned_data = {
            'creatinine': 1.3,
            'creatinine_unit': 'mg/dL',
            'are_results_normal': NO
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_creatinine_umol_invalid(self):
        cleaned_data = {
            'creatinine': 43,
            'creatinine_unit': 'umol/L',
            'are_results_normal': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_creatinine_umol(self):

        cleaned_data = {
            'creatinine': 100,
            'creatinine_unit': 'mg/dL',
            'are_results_normal': NO
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_sodium_invalid(self):
        cleaned_data = {
            'sodium': 100,
            'are_results_normal': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_sodium(self):

        cleaned_data = {
            'sodium': 135,
            'are_results_normal': NO
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_potassium_invalid(self):
        cleaned_data = {
            'potassium': 1.0,
            'are_results_normal': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_potassium(self):

        cleaned_data = {
            'potassium': 5.0,
            'are_results_normal': NO}
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_magnesium_invalid(self):
        cleaned_data = {
            'magnesium': 0.01,
            'are_results_normal': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_magnesium(self):

        cleaned_data = {
            'magnesium': 1.0,
            'are_results_normal': NO}
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
