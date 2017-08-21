from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import NO, NOT_APPLICABLE

from ..form_validators import BloodResultFormValidator


class TestAdverseEventFormValidator(TestCase):

    def test_abnormal_results_no_ae_range_invalid(self):
        options = {
            'are_results_normal': NO,
            'abnormal_results_in_ae_range': NOT_APPLICABLE}
        form_validator = BloodResultFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('abnormal_results_in_ae_range', form_validator._errors)

    def test_abnormal_results_wiht_ae_range_valid(self):
        options = {
            'are_results_normal': NO,
            'abnormal_results_in_ae_range': NO}
        form_validator = BloodResultFormValidator(cleaned_data=options)

        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_creatinine_mmol_unit_decimal_invalid(self):
        cleaned_data = dict(creatinine_unit='umol/L')
        for value in ['346.12', 346.12, '346.']:
            with self.subTest(value=value):
                cleaned_data.update(creatinine=value)
                form_validator = BloodResultFormValidator(
                    cleaned_data=cleaned_data)
                self.assertRaises(ValidationError, form_validator.validate)

    def test_creatinine_mmol_unit_decimal_valid(self):
        cleaned_data = dict(creatinine_unit='umol/L')
        for value in ['346.12', 346.12, '346.']:
            with self.subTest(value=value):
                cleaned_data.update(creatinine=value)
                form_validator = BloodResultFormValidator(
                    cleaned_data=cleaned_data)
                self.assertRaises(ValidationError, form_validator.validate)
