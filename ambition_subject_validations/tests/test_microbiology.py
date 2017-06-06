from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO, POS, NOT_APPLICABLE, OTHER
from edc_base.utils import get_utcnow

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

        cleaned_data = {'urine_culture_results': POS,
                        'urine_culture_organism': NOT_APPLICABLE}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'urine_culture_results': POS,
                        'urine_culture_organism': 'klebsiella_sp'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

    def test_other_urine_culture_results_require_urine_organism_other(self):
        cleaned_data = {'urine_culture_results': OTHER,
                        'urine_culture_organism_other': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'urine_culture_results': OTHER,
                        'urine_culture_organism_other': NOT_APPLICABLE}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'urine_culture_results': OTHER,
                        'urine_culture_organism_other': 'other organism'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

    def test_blood_culture_performed_yes_blood_culture_results(self):
        cleaned_data = {'blood_culture_performed': YES,
                        'blood_culture_results': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'blood_culture_performed': YES,
                        'blood_culture_results': 'no_growth'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

        cleaned_data = {'blood_culture_performed': NO,
                        'blood_culture_results': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

        cleaned_data = {'blood_culture_performed': NO,
                        'blood_culture_results': 'no_growth'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

    def test_pos_blood_culture_results_require_date_blood_taken(self):
        cleaned_data = {'blood_culture_results': POS,
                        'date_blood_taken': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'blood_culture_results': POS,
                        'date_blood_taken': get_utcnow()}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

    def test_pos_blood_culture_results_require_blood_culture_organism(self):
        cleaned_data = {'blood_culture_results': POS,
                        'blood_culture_organism': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'blood_culture_results': POS,
                        'blood_culture_organism': NOT_APPLICABLE}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'blood_culture_results': POS,
                        'blood_culture_organism': 'cryptococcus_neoformans'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())


