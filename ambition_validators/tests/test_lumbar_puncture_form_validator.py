from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import YES, NO

from ..form_validators import LumbarPunctureCSFFormValidator


class TestLumbarPunctureFormValidator(TestCase):

    def test_closing_pressure_error(self):
        cleaned_data = {
            'opening_pressure': 10,
            'closing_pressure': 11
        }
        form_validator = LumbarPunctureCSFFormValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('closing_pressure', form_validator._errors)

    def test_closing_pressure(self):
        cleaned_data = {
            'opening_pressure': 10,
            'closing_pressure': 9}
        form_validator = LumbarPunctureCSFFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_csf_culture_yes(self):
        cleaned_data = {'csf_culture': YES,
                        'other_csf_culture': None}
        form_validator = LumbarPunctureCSFFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('other_csf_culture', form_validator._errors)

    def test_csf_culture_no(self):
        cleaned_data = {'csf_culture': NO,
                        'other_csf_culture': 'blah'}
        form_validator = LumbarPunctureCSFFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('other_csf_culture', form_validator._errors)

    def test_csf_wbc_cell_count_less_than_three(self):
        cleaned_data = {'csf_wbc_cell_count': 2, }
        form_validator = LumbarPunctureCSFFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('csf_wbc_cell_count', form_validator._errors)

    def test_india_ink_csf_arg_not_done_invalid(self):
        """Assert that either csf_cr_ag or india_ink is done.
        """
        cleaned_data = {'csf_cr_ag': 'not_done',
                        'india_ink': 'not_done'}
        form_validator = LumbarPunctureCSFFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('csf_cr_ag', form_validator._errors)
        self.assertIn('india_ink', form_validator._errors)

    def test_differential_lymphocyte_count_greater_than_zero(self):
        cleaned_data = {
            'csf_wbc_cell_count': 0, 'differential_lymphocyte_count': 5}
        form_validator = LumbarPunctureCSFFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('differential_lymphocyte_count', form_validator._errors)

    def test_neutrophil_count_greater_than_zero(self):
        cleaned_data = {
            'csf_wbc_cell_count': 0, 'differential_neutrophil_count': 5}
        form_validator = LumbarPunctureCSFFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('differential_neutrophil_count', form_validator._errors)

    def test_csf_cr_ag_no_csf_cr_ag_lfa_invalid(self):
        """Assert that the csf wbc count greater than 0.
        """
        cleaned_data = {'csf_cr_ag': 'not_done',
                        'csf_cr_ag_lfa': YES}
        form_validator = LumbarPunctureCSFFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('csf_cr_ag_lfa', form_validator._errors)

    def test_differential_neutrophil_count_percent_limit_passed(self):
        cleaned_data = {'differential_neutrophil_count': 125.6,
                        'differential_neutrophil_unit': '%'}
        form_validator = LumbarPunctureCSFFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('differential_neutrophil_count', form_validator._errors)

    def test_differential_lymphocyte_count_percent_limit_passed(self):
        cleaned_data = {'differential_lymphocyte_count': 125.6,
                        'differential_lymphocyte_unit': '%'}
        form_validator = LumbarPunctureCSFFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('differential_lymphocyte_count', form_validator._errors)
