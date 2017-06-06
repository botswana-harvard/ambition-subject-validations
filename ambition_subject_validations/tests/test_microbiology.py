from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES

from ..validations import Microbiology


class TestMicrobiologyValidations(TestCase):
    def test_urine_culture_performed_require_urine_culture_results(self):
        cleaned_data = {'urine_culture_performed': YES,
                        'urine_culture_results': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'urine_culture_performed': YES,
                        'urine_culture_results': 'no_growth'}
        follow_up = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())
