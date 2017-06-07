from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO, POS, NOT_APPLICABLE, OTHER

from ..form_validators import MicrobiologyFormValidator


class TestMicrobiologyFormValidator(TestCase):

    def test_urine_culture_performed_yes_require_urine_culture_results(self):
        cleaned_data = {'urine_culture_performed': YES,
                        'urine_culture_results': None}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_urine_culture_performed_no_require_urine_culture_results(self):
        cleaned_data = {'urine_culture_performed': NO,
                        'urine_culture_results': 'no_growth'}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_urine_culture_performed_na_given_urine_culture_results(self):
        cleaned_data = {'urine_culture_performed': YES,
                        'urine_culture_results': NOT_APPLICABLE}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_urine_culture_performed_yes_given_urine_culture_results(self):
        cleaned_data = {'urine_culture_performed': YES,
                        'urine_culture_results': 'no_growth'}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_pos_urine_culture_results_none_urine_culture_organism(self):
        cleaned_data = {'urine_culture_results': POS,
                        'urine_culture_organism': None}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_pos_urine_results_na_urine_culture_organism(self):
        cleaned_data = {'urine_culture_results': POS,
                        'urine_culture_organism': NOT_APPLICABLE}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_other_urine_culture_results_require_urine_organism_other(self):
        cleaned_data = {'urine_culture_results': OTHER,
                        'urine_culture_organism_other': None}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_other_urine_culture_results_na_urine_organism_other(self):
        cleaned_data = {'urine_culture_results': OTHER,
                        'urine_culture_organism_other': NOT_APPLICABLE}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_yes_blood_culture_performed_none_blood_culture_results(self):
        cleaned_data = {'blood_culture_performed': YES,
                        'blood_culture_results': None}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_no_blood_culture_performed_given_blood_culture_results(self):
        cleaned_data = {'blood_culture_performed': NO,
                        'blood_culture_results': 'no_growth'}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_pos_blood_culture_results_require_date_blood_taken(self):
        cleaned_data = {'blood_culture_results': POS,
                        'date_blood_taken': None}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_pos_blood_culture_results_require_blood_culture_organism(self):
        cleaned_data = {'blood_culture_results': POS,
                        'blood_culture_organism': None}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_pos_blood_culture_results_none_blood_culture_organism(self):
        cleaned_data = {'blood_culture_results': POS,
                        'blood_culture_organism': None}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_pos_blood_culture_results_na_blood_culture_organism(self):
        cleaned_data = {'blood_culture_results': POS,
                        'blood_culture_organism': NOT_APPLICABLE}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_other_blood_culture_organism_require_culture_organism_other(self):
        cleaned_data = {'blood_culture_organism': OTHER,
                        'blood_culture_organism_other': None}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_other_blood_culture_organism_na_culture_organism_other(self):
        cleaned_data = {'blood_culture_organism': OTHER,
                        'blood_culture_organism_other': NOT_APPLICABLE}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_blood_organism_is_bacteria_require_bacteria_identified(self):
        cleaned_data = {'blood_culture_organism': 'BACTERIA',
                        'bacteria_identified': None}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_blood_organism_is_bacteria_na_bacteria_identified(self):
        cleaned_data = {'blood_culture_organism': 'BACTERIA',
                        'bacteria_identified': NOT_APPLICABLE}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_other_bacteria_identified_require_bacteria_identified_other(self):
        cleaned_data = {'bacteria_identified': OTHER,
                        'bacteria_identified_other': None}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_other_bacteria_identified_na_bacteria_identified_other(self):
        cleaned_data = {'bacteria_identified': OTHER,
                        'bacteria_identified_other': NOT_APPLICABLE}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_pos_sputum_results_culture_none_sputum_results_positive(self):
        cleaned_data = {'sputum_results_culture': POS,
                        'sputum_results_positive': None}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_pos_sputum_results_culture_na_sputum_results_positive(self):
        cleaned_data = {'sputum_results_culture': POS,
                        'sputum_results_positive': NOT_APPLICABLE}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_tissue_biopsy_taken_none_tissue_biopsy_results(self):
        cleaned_data = {'tissue_biopsy_taken': YES,
                        'tissue_biopsy_results': None}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_tissue_biopsy_taken_with_tissue_biopsy_results(self):
        cleaned_data = {'tissue_biopsy_taken': NO,
                        'tissue_biopsy_results': 'no_growth'}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_pos_tissue_biopsy_results_require_date_biopsy_taken(self):
        cleaned_data = {'tissue_biopsy_results': POS,
                        'date_biopsy_taken': None}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_pos_tissue_biopsy_results_na_date_biopsy_taken(self):
        cleaned_data = {'tissue_biopsy_results': POS,
                        'date_biopsy_taken': NOT_APPLICABLE}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_pos_tissue_biopsy_results_none_tissue_biopsy_organism(self):
        cleaned_data = {'tissue_biopsy_results': POS,
                        'tissue_biopsy_organism': None}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_pos_tissue_biopsy_results_na_tissue_biopsy_organism(self):
        cleaned_data = {'tissue_biopsy_results': POS,
                        'tissue_biopsy_organism': NOT_APPLICABLE}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_other_tissue_biopsy_org_none_tissue_biopsy_org_other(self):
        cleaned_data = {'tissue_biopsy_organism': OTHER,
                        'tissue_biopsy_organism_other': None}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_other_tissue_biopsy_org_na_tissue_biopsy_org_other(self):
        cleaned_data = {'tissue_biopsy_organism': OTHER,
                        'tissue_biopsy_organism_other': NOT_APPLICABLE}
        form_validator = MicrobiologyFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
