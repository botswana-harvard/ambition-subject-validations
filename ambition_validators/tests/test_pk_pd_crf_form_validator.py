from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO, NOT_APPLICABLE, OTHER

from ..constants import DEVIATION, VIOLATION
from ..form_validators import PkPdCrfFormValidator


class TestPkPdCrfFormValidator(TestCase):

    # assertRaises flucytosine_dose_missed is required
    def test_csf_culture_yes(self):
        cleaned_data = {'flucytosine_doses_missed': YES,
                        'flucytosine_dose_missed': None}
        form_validator = PkPdCrfFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('flucytosine_dose_missed', form_validator._errors)
