from django.core.exceptions import ValidationError
from django.test import TestCase

from ..validations import PatientHistory


class TestPatientHistoryValidations(TestCase):

    def test_first_line_choice_yes(self):
        """Assert that the first line choice is within the first_line_arvs
        """
        options = {'first_line_arvs': 'AZT + 3-TC + either EFV or NVP or DTG',
                   'first_line_choice': 'EFV'}
        form = PatientHistory(cleaned_data=options)
        self.assertTrue(form.clean())

    def test_first_line_choice_no(self):
        """Assert that the first line choice is not provided
        """
        options = {'first_line_arvs': 'AZT + 3-TC + either EFV or NVP or DTG',
                   'first_line_choice': None}
        form = PatientHistory(cleaned_data=options)
        self.assertRaises(ValidationError, form.clean)

    def test_if_focal_neurological_deficit(self):
        """Assert that patient has focal neurological deficit
        """
        options = {'focal_neurologic_deficit': 'meningismus'}
        form = PatientHistory(cleaned_data=options)
        self.assertTrue(form.clean())

    def test_if_focal_neurological_deficit_none(self):
        options = {'first_line_arvs': 'AZT + 3-TC + either EFV or NVP or DTG',
                   'first_line_choice': None}
        form = PatientHistory(cleaned_data=options)
        self.assertRaises(ValidationError, form.clean)
