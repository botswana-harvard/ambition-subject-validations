from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO, POS

from ..validations import Microbiology


class TestMicrobiologyValidations(TestCase):

    def test_urine_culture_performed_require_urine_culture_results(self):
        cleaned_data = {'urine_culture_performed': YES,
                        'urine_culture_results': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'urine_culture_performed': YES,
                        'urine_culture_results': 'no_growth'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

        cleaned_data = {'urine_culture_performed': NO,
                        'urine_culture_results': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

        cleaned_data = {'urine_culture_performed': NO,
                        'urine_culture_results': 'no_growth'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

    def test_pos_urine_culture_results_require_urine_culture_organism(self):
        cleaned_data = {'urine_culture_results': POS,
                        'urine_culture_organism': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

