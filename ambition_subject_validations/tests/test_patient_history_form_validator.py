from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES

from ..form_validators import PatientHistoryFormValidator


class TestPatientHistoryFormValidator(TestCase):

    def test_first_line_choice_yes(self):
        """Assert that the first line choice is within the first_line_arvs
        """
        options = {'first_line_choice': 'EFV'}
        form = PatientHistoryFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form.clean)

    def test_first_line_choice_no(self):
        """Assert that the first line choice is not provided
        """
        options = {'first_line_arvs': 'AZT + 3-TC + either EFV or NVP or DTG',
                   'first_line_choice': None}
        form = PatientHistoryFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form.clean)

    def test_if_focal_neurological_deficit_yes(self):
        """Assert that patient has focal neurological deficit
        """
        options = {'neurological': YES, 'focal_neurologic_deficit': 'meningismus', 'first_line_choice': 'EFV'}
        form = PatientHistoryFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form.clean)

    def test_if_focal_neurological_deficit_none(self):
        options = {'first_line_arvs': 'AZT + 3-TC + either EFV or NVP or DTG',
                   'first_line_choice': None}
        form = PatientHistoryFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form.clean)
