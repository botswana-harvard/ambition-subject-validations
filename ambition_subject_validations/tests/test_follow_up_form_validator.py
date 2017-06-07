from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO
from edc_base.utils import get_utcnow

from ..form_validators import FollowUpFormValidator


class TestFollowUpFormValidatorFormValidators(TestCase):

    def test_tb_pulmonary_dx_yes_require_tb_pulmonary_dx_date(self):
        cleaned_data = {'tb_pulmonary_dx': YES,
                        'tb_pulmonary_dx_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'tb_pulmonary_dx': YES,
                        'tb_pulmonary_dx_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

    def test_tb_pulmonary_dx_no_require_tb_pulmonary_dx_date(self):
        cleaned_data = {'tb_pulmonary_dx': NO,
                        'tb_pulmonary_dx_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'tb_pulmonary_dx': NO,
                        'tb_pulmonary_dx_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

    def test_extra_pulmonary_yes_require_extra_tb_pulmonary_dx_date(self):
        cleaned_data = {'extra_pulmonary_tb_dx': YES,
                        'extra_tb_pulmonary_dx_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'extra_pulmonary_tb_dx': YES,
                        'extra_tb_pulmonary_dx_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

    def test_extra_pulmonary_tb_dx_no_require_extra_tb_pulmonary_dx_date(self):
        cleaned_data = {'extra_pulmonary_tb_dx': NO,
                        'extra_tb_pulmonary_dx_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'extra_pulmonary_tb_dx': NO,
                        'extra_tb_pulmonary_dx_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

    def test_kaposi_sarcoma_dx_yes_require_kaposi_sarcoma_dx_date(self):
        cleaned_data = {'kaposi_sarcoma_dx': YES,
                        'kaposi_sarcoma_dx_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'kaposi_sarcoma_dx': YES,
                        'kaposi_sarcoma_dx_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

    def test_kaposi_sarcoma_dx_no_require_kaposi_sarcoma_dx_date(self):
        cleaned_data = {'kaposi_sarcoma_dx': NO,
                        'kaposi_sarcoma_dx_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'kaposi_sarcoma_dx': NO,
                        'kaposi_sarcoma_dx_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

    def test_malaria_dx_yes_require_malaria_dx_date(self):
        cleaned_data = {'malaria_dx': YES,
                        'malaria_dx_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'malaria_dx': YES,
                        'malaria_dx_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

    def test_malaria_dx_no_require_malaria_dx_date(self):
        cleaned_data = {'malaria_dx': NO,
                        'malaria_dx_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'malaria_dx': NO,
                        'malaria_dx_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

    def test_bacteraemia_dx_yes_require_bacteraemia_dx_date(self):
        cleaned_data = {'bacteraemia_dx': YES,
                        'bacteraemia_dx_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'bacteraemia_dx': YES,
                        'bacteraemia_dx_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

    def test_bacteraemia_dx_no_require_bacteraemia_dx_date(self):
        cleaned_data = {'bacteraemia_dx': NO,
                        'bacteraemia_dx_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'bacteraemia_dx': NO,
                        'bacteraemia_dx_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

    def test_pneumonia_dx_yes_require_bacteraemia_dx_date(self):
        cleaned_data = {'pneumonia_dx': YES,
                        'pneumonia_dx_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'pneumonia_dx': YES,
                        'pneumonia_dx_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

    def test_pneumonia_dx_no_require_bacteraemia_dx_date(self):
        cleaned_data = {'pneumonia_dx': NO,
                        'pneumonia_dx_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'pneumonia_dx': NO,
                        'pneumonia_dx_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

    def test_diarrhoeal_wasting_dx_yes_require_bacteraemia_dx_date(self):
        cleaned_data = {'diarrhoeal_wasting_dx': YES,
                        'diarrhoeal_wasting_dx_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'diarrhoeal_wasting_dx': YES,
                        'diarrhoeal_wasting_dx_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

    def test_diarrhoeal_wasting_dx_no_require_bacteraemia_dx_date(self):
        cleaned_data = {'diarrhoeal_wasting_dx': NO,
                        'diarrhoeal_wasting_dx_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'diarrhoeal_wasting_dx': NO,
                        'diarrhoeal_wasting_dx_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

    def test_significant_diagnosis_yes_require_diagnosis_date(self):
        cleaned_data = {'other_significant_new_diagnosis': YES,
                        'diagnosis_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'other_significant_new_diagnosis': YES,
                        'diagnosis_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

    def test_significant_diagnosis_no_require_diagnosis_date(self):
        cleaned_data = {'other_significant_new_diagnosis': NO,
                        'diagnosis_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'other_significant_new_diagnosis': NO,
                        'diagnosis_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

    def test_rifampicin_started_yes_require_rifampicin_start_date(self):
        cleaned_data = {'rifampicin_started': YES,
                        'rifampicin_start_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'rifampicin_started': YES,
                        'rifampicin_start_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

    def test_rifampicin_started_no_require_rifampicin_start_datee(self):
        cleaned_data = {'rifampicin_started': NO,
                        'rifampicin_start_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'rifampicin_started': NO,
                        'rifampicin_start_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

    def test_fluconazole_dose_yes_require_other_fluconazole_dose_reason(self):
        cleaned_data = {'fluconazole_dose': YES,
                        'other_fluconazole_dose_reason': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

        cleaned_data = {'fluconazole_dose': YES,
                        'other_fluconazole_dose_reason': 'reason'}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

    def test_fluconazole_dosed_no_require_rifampicin_start_datee(self):
        cleaned_data = {'fluconazole_dose': NO,
                        'other_fluconazole_dose_reason': 'reason'}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

        cleaned_data = {'fluconazole_dose': NO,
                        'other_fluconazole_dose_reason': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

    def other_fluconazole_dose_yes_require_other_fluconazole_dose_reason(self):
        cleaned_data = {'other_fluconazole_dose': YES,
                        'other_fluconazole_dose_reason': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'other_fluconazole_dose': YES,
                        'other_fluconazole_dose_reason': 'reason'}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())

    def other_fluconazole_dose_no_require_rifampicin_start_datee(self):
        cleaned_data = {'other_fluconazole_dose': NO,
                        'other_fluconazole_dose_reason': 'reason'}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'other_fluconazole_dose': NO,
                        'other_fluconazole_dose_reason': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())
