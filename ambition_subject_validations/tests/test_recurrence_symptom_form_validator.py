from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import OTHER, YES

from ..form_validators import RecurrenceSymptomFormValidator


class TestRecurrenceSymptomFormValidator(TestCase):

    def test_meningitis_symptom_other_none(self):
        options = {
            'meningitis_symptom': OTHER,
            'meningitis_symptom_other': None}
        form_validator = RecurrenceSymptomFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)
