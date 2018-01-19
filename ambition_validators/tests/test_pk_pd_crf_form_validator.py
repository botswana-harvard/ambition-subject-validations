from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_constants.constants import YES, NO

from ..form_validators import PkPdCrfFormValidator


class TestPkPdCrfFormValidator(TestCase):

    # assertRaises flucytosine_dose_missed is required
    def test_flucytosine_doses_yes(self):
        cleaned_data = {'flucytosine_doses_missed': YES,
                        'flucytosine_dose_missed': None}
        form_validator = PkPdCrfFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('flucytosine_dose_missed', form_validator._errors)

        # assertRaises reason_fluconazole_dose_missed is required
    def test_fluconazole_dose_missed_yes(self):
        cleaned_data = {'fluconazole_dose_missed': YES,
                        'reason_fluconazole_dose_missed': None}
        form_validator = PkPdCrfFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('reason_fluconazole_dose_missed', form_validator._errors)

        # assertRaises reason_day_one_missed is required
    def test_any_day_one_sample_missed_yes(self):
        cleaned_data = {'any_day_one_sample_missed': YES,
                        'reason_day_one_missed': None}
        form_validator = PkPdCrfFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('reason_day_one_missed', form_validator._errors)

        # assertRaises reason_day_seven_missed is required
    def test_any_day_seven_sample_missed_yes(self):
        cleaned_data = {'any_day_seven_sample_missed': YES,
                        'reason_day_seven_missed': None}
        form_validator = PkPdCrfFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('reason_day_seven_missed', form_validator._errors)

        # assertRaises post_dose_lp is required
    def test_post_dose_lp(self):
        cleaned_data = {'pre_dose_lp': NO,
                        'post_dose_lp': None}
        form_validator = PkPdCrfFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('post_dose_lp', form_validator._errors)

    # assertRaises reason_fluconazole_dose_missed is required
    def test_fluconazole_doses_missed_yes(self):
        cleaned_data = {'fluconazole_dose_missed': YES,
                        'reason_fluconazole_dose_missed': None}
        form_validator = PkPdCrfFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('reason_fluconazole_dose_missed', form_validator._errors)

    # assertRaises reason_blood_sample_missed is required
    def test_blood_sample_missed_yes(self):
        cleaned_data = {'blood_sample_missed': YES,
                        'reason_blood_sample_missed': None}
        form_validator = PkPdCrfFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('reason_blood_sample_missed', form_validator._errors)
