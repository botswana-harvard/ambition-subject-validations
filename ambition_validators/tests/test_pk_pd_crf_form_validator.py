from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_constants.constants import NO

from ..form_validators import PkPdCrfFormValidator


class TestPkPdCrfFormValidator(TestCase):

    def test_post_dose_lp(self):
        cleaned_data = {'pre_dose_lp': NO,
                        'post_dose_lp': None}
        form_validator = PkPdCrfFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('post_dose_lp', form_validator._errors)
