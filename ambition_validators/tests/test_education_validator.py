from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import NO

from ..form_validators import EducationFormValidator


class TestEducationalBackgroundFormValidator(TestCase):

    def test_attendance_years(self):
        cleaned_data = {'elementary': NO,
                        'attendance_years': 1}
        form = EducationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('attendance_years', form._errors)

    def test_secondary_years(self):
        cleaned_data = {'secondary': NO,
                        'secondary_years': 1}
        form = EducationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('secondary_years', form._errors)

    def test_higher_education(self):
        cleaned_data = {'higher_education': NO,
                        'higher_years': 1}
        form = EducationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('higher_years', form._errors)
