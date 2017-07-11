from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES

from ..form_validators import LumbarPunctureCSFFormValidator


class TestLumbarPunctureFormValidator(TestCase):

    def test_csf_culture_yes(self):
        cleaned_data = {'csf_culture': YES,
                        'other_csf_culture': None}
        form = LumbarPunctureCSFFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_csf_culture_no(self):
        cleaned_data = {'csf_culture': YES,
                        'other_csf_culture': 'blah'}
        form = LumbarPunctureCSFFormValidator(cleaned_data=cleaned_data)
        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_csf_wbc_cell_count_less_than_three(self):
        cleaned_data = {'csf_wbc_cell_count': 2, }
        form = LumbarPunctureCSFFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_csf_wbc_cell_count_greater_than_zero(self):
        """Assert that the csf wbc count greater than 0.
        """
        cleaned_data = {'csf_wbc_cell_count': 5, }
        form = LumbarPunctureCSFFormValidator(cleaned_data=cleaned_data)
        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_india_ink_csf_arg_not_done_invalid(self):
        """Assert that the csf wbc count greater than 0.
        """
        cleaned_data = {'csf_cr_ag': 'not_done',
                        'india_ink': 'not_done'}
        form = LumbarPunctureCSFFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_india_ink_csf_arg_done_valid(self):
        """Assert that the csf wbc count greater than 0.
        """
        cleaned_data = {'csf_cr_ag': 'Positive',
                        'india_ink': 'Positive'}
        form = LumbarPunctureCSFFormValidator(cleaned_data=cleaned_data)

        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_differential_lymphocyte_count_greater_than_zero(self):
        cleaned_data = {
            'csf_wbc_cell_count': 0, 'differential_lymphocyte_count': 5}
        form = LumbarPunctureCSFFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_differential_lymphocyte_count_not_required(self):
        cleaned_data = {
            'csf_wbc_cell_count': 0, 'differential_lymphocyte_count': None}
        form = LumbarPunctureCSFFormValidator(cleaned_data=cleaned_data)
        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_neutrophil_count_greater_than_zero(self):
        cleaned_data = {
            'csf_wbc_cell_count': 1, 'differential_neutrophil_count': 5}
        form = LumbarPunctureCSFFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_differential_neutrophil_count_not_required(self):
        cleaned_data = {
            'csf_wbc_cell_count': 2, 'differential_neutrophil_count': None}
        form = LumbarPunctureCSFFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_csf_cr_ag_no_csf_cr_ag_lfa_invalid(self):
        """Assert that the csf wbc count greater than 0.
        """
        cleaned_data = {'csf_cr_ag': 'not_done',
                        'csf_cr_ag_lfa': YES}
        form = LumbarPunctureCSFFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_csf_cr_ag_csf_cr_ag_lfa_valid(self):
        """Assert that the csf wbc count greater than 0.
        """
        cleaned_data = {'csf_cr_ag': 'Positive',
                        'not_done': None}
        form = LumbarPunctureCSFFormValidator(cleaned_data=cleaned_data)

        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_differential_neutrophil_count_percent_limit_passed(self):
        cleaned_data = {'differential_neutrophil_count': 125.6,
                        'differential_neutrophil_unit': '%'}
        form = LumbarPunctureCSFFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_differential_neutrophil_count_percent_limit_not_passed(self):
        cleaned_data = {'differential_neutrophil_count': 100,
                        'differential_neutrophil_unit': '%'}
        form = LumbarPunctureCSFFormValidator(cleaned_data=cleaned_data)

        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_differential_lymphocyte_count_percent_limit_passed(self):
        cleaned_data = {'differential_lymphocyte_count': 125.6,
                        'differential_lymphocyte_unit': '%'}
        form = LumbarPunctureCSFFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_differential_lymphocyte_count_percent_limit_not_passed(self):
        cleaned_data = {'differential_lymphocyte_count': 100,
                        'differential_lymphocyte_unit': '%'}
        form = LumbarPunctureCSFFormValidator(cleaned_data=cleaned_data)

        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
