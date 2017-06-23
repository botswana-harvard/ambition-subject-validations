from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO

from ..form_validators import LumbarPunctureCSFFormValidator


class TestLumbarPunctureFormValidator(TestCase):

    def test_csf_culture_yes(self):
        cleaned_data = {'csf_culture': YES, 'other_csf_culture': None}
        form = LumbarPunctureCSFFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_csf_culture_no(self):
        options = {'csf_culture': NO, 'other_csf_culture': YES}
        form = LumbarPunctureCSFFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form.clean)

    def test_if_csf_wbc_cell_count_less_than_three(self):
        options = {'csf_culture': YES, 'csf_wbc_cell_count': 3}
        form = LumbarPunctureCSFFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form.clean)

    def test_if_csf_wbc_cell_count_greater_than_zero(self):
        """Assert that the csf wbc count greater than 0.
        """
        options = {'csf_wbc_cell_count': 1}
        form = LumbarPunctureCSFFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form.clean)

    def test_india_ink_csf_arg_not_done_invalid(self):
        """Assert that the csf wbc count greater than 0.
        """
        options = {'csf_cr_ag': 'not_done',
                   'india_ink': 'not_done'}
        form = LumbarPunctureCSFFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form.clean)

    def test_india_ink_csf_arg_done_valid(self):
        """Assert that the csf wbc count greater than 0.
        """
        options = {'csf_cr_ag': 'Positive',
                   'india_ink': 'Positive'}
        form = LumbarPunctureCSFFormValidator(cleaned_data=options)

        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_differential_lymphocyte_count_greater_than_zero(self):
        options = {'csf_wbc_cell_count': 1, 'differential_lymphocyte_count': 4}
        form = LumbarPunctureCSFFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form.clean)

    def test_differential_lymphocyte_count_not_required(self):
        options = {
            'csf_wbc_cell_count': 1, 'differential_lymphocyte_count': None}
        form = LumbarPunctureCSFFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form.clean)

    def test_neutrophil_count_greater_than_zero(self):
        options = {'csf_wbc_cell_count': 1, 'differential_neutrophil_count': 5}
        form = LumbarPunctureCSFFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form.clean)

    def differential_neutrophil_count_not_required(self):
        options = {
            'csf_wbc_cell_count': 2, 'differential_neutrophil_count': None}
        form = LumbarPunctureCSFFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form.clean)
