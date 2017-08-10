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
        blood_form = BloodResultFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, blood_form.clean)

    def test_abnormal_results_wiht_ae_range_valid(self):
        options = {
            'are_results_normal': NO,
            'abnormal_results_in_ae_range': NO}
        blood_form = BloodResultFormValidator(cleaned_data=options)

        try:
            blood_form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_creatinine_mmol_unit_decimal_invalid(self):
        options = {
            'creatinine_unit': 'umol/L',
            'creatinine': '346.12'}
        blood_form = BloodResultFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, blood_form.clean)

    def test_creatinine_mmol_unit_decimal_valid(self):
        options = {
            'creatinine_unit': 'umol/L',
            'creatinine': '346'}
        blood_form = BloodResultFormValidator(cleaned_data=options)

        try:
            blood_form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
