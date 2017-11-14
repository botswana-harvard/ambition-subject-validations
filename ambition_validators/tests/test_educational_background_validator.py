from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import NO

from ..form_validators import EducationalBackgroundFormValidator


class TestEducationalBackgroundFormValidator(TestCase):

    def test_head_attendance_years(self):
        cleaned_data = {'head_elementary': NO,
                        'head_attendance_years': 1}
        form = EducationalBackgroundFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('head_attendance_years', form._errors)

    def test_head_secondary_years(self):
        cleaned_data = {'head_secondary': NO,
                        'head_secondary_years': 1}
        form = EducationalBackgroundFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('head_secondary_years', form._errors)

    def test_head_higher_education(self):
        cleaned_data = {'head_higher_education': NO,
                        'head_higher_years': 1}
        form = EducationalBackgroundFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('head_higher_years', form._errors)
