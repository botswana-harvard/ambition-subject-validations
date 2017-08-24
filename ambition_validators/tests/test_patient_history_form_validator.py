from dateutil.relativedelta import relativedelta
from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO, OTHER, NOT_APPLICABLE

from ..constants import HEADACHE, VISUAL_LOSS
from ..form_validators import PatientHistoryFormValidator


class TestPatientHistoryFormValidator(TestCase):

    #     def test_headache_requires_headache_duration(self):
    #         """Assert that headache selection requires duration
    #         """
    #         cleaned_data = {'symptom': HEADACHE,
    #                         'headache_duration': None}
    #         form_validator = PatientHistoryFormValidator(cleaned_data=cleaned_data)
    #         self.assertRaises(ValidationError, form_validator.validate)
    #         self.assertIn('headache_duration', form_validator._errors)

    def test_tb_history_yes_tb_site_none_invalid(self):
        cleaned_data = {'tb_history': YES,
                        'tb_site': NOT_APPLICABLE}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('tb_site', form._errors)

    def test_tb_treatment_taking_rifapicin_none_invalid(self):
        cleaned_data = {'tb_treatment': YES,
                        'taking_rifampicin': NOT_APPLICABLE}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('taking_rifampicin', form._errors)

    def test_taking_rifapicin_started_date_none_invalid(self):
        cleaned_data = {'taking_rifampicin': YES,
                        'rifampicin_started_date': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('rifampicin_started_date', form._errors)

    def test_previous_non_tb_oi_name_none_invalid(self):
        cleaned_data = {'previous_non_tb_oi': YES,
                        'previous_non_tb_oi_name': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('previous_non_tb_oi_name', form._errors)

    def test_previous_non_tb_oi_date_none_invalid(self):
        cleaned_data = {'previous_non_tb_oi': YES,
                        'previous_non_tb_oi_name': 'blah',
                        'previous_non_tb_oi_date': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('previous_non_tb_oi_date', form._errors)

    def test_new_hiv_diagnosis_taking_arv_none_invalid(self):
        cleaned_data = {'new_hiv_diagnosis': YES,
                        'taking_arv': NOT_APPLICABLE}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('taking_arv', form._errors)

    def test_taking_arv_arv_date_none_invalid(self):
        cleaned_data = {'taking_arv': YES,
                        'arv_date': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('arv_date', form._errors)

    def test_taking_arv_first_arv_regimen_none_invalid(self):
        cleaned_data = {'taking_arv': YES,
                        'arv_date': get_utcnow(),
                        'first_arv_regimen': NOT_APPLICABLE}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('first_arv_regimen', form._errors)

    def test_first_arv_regimen_other_none_invalid(self):
        cleaned_data = {'first_arv_regimen': OTHER,
                        'first_arv_regimen_other': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('first_arv_regimen_other', form._errors)

    def test_second_arv_regimen_other_none_invalid(self):
        cleaned_data = {'second_arv_regimen': OTHER,
                        'second_arv_regimen_other': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('second_arv_regimen_other', form._errors)

    def test_first_arv_regimen_first_line_choice_none_invalid(self):
        cleaned_data = {'first_arv_regimen': YES,
                        'first_line_choice': NOT_APPLICABLE}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('first_line_choice', form._errors)

    def test_taking_arv_patient_adherence_none_invalid(self):
        cleaned_data = {'taking_arv': NO,
                        'patient_adherence': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('patient_adherence', form._errors)

    def test_patient_adherence_last_dose_none_invalid(self):
        cleaned_data = {'patient_adherence': NO,
                        'last_dose': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('last_dose', form._errors)

#     def test_patient_adherence_last_dose_none_invalid(self):
#         cleaned_data = {'neurological': 'focal_neurologic_deficit',
#                         'focal_neurologic_deficit': None}
#         form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
#         self.assertRaises(ValidationError, form.validate)
#         self.assertIn('focal_neurologic_deficit', form._errors)
