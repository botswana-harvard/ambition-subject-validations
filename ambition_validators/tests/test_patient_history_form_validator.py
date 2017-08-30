from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO, OTHER, NOT_APPLICABLE

from ..constants import WORKING
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

    def test_taking_arv_first_arv_regimen_no(self):
        cleaned_data = {'taking_arv': NO,
                        'first_arv_regimen': 'Other'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('first_arv_regimen', form._errors)

    def test_taking_arv_second_arv_regimen_no(self):
        cleaned_data = {'taking_arv': NO,
                        'first_arv_regimen': NOT_APPLICABLE,
                        'second_arv_regimen': 'AZT+3-TC+ either ATZ/r '
                        'or Lopinavir/r'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('second_arv_regimen', form._errors)

    def test_taking_arv_first_line_choice_no(self):
        cleaned_data = {'taking_arv': NO,
                        'first_arv_regimen': NOT_APPLICABLE,
                        'second_arv_regimen': NOT_APPLICABLE,
                        'first_line_choice': 'EFV'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('first_line_choice', form._errors)

    def test_taking_arv_patient_adherence_no(self):
        cleaned_data = {'taking_arv': NO,
                        'first_arv_regimen': NOT_APPLICABLE,
                        'second_arv_regimen': NOT_APPLICABLE,
                        'first_line_choice': NOT_APPLICABLE,
                        'patient_adherence': YES}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('patient_adherence', form._errors)

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

#     def test_taking_arv_patient_adherence_none_invalid(self):
#         cleaned_data = {'taking_arv': NO,
#                         'patient_adherence': None}
#         form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
#         self.assertRaises(ValidationError, form.validate)
#         self.assertIn('patient_adherence', form._errors)

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

    def test_care_before_hospital_yes(self):
        cleaned_data = {'care_before_hospital': YES,
                        'location_care': NOT_APPLICABLE}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('location_care', form._errors)

    def test_care_before_hospital_no(self):
        cleaned_data = {'care_before_hospital': NO,
                        'location_care': 'healthcare'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('location_care', form._errors)

    def test_care_before_hospital_other(self):
        cleaned_data = {'care_before_hospital': OTHER,
                        'care_before_hospital_other': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('care_before_hospital_other', form._errors)

    def test_location_care_other(self):
        cleaned_data = {'location_care': OTHER,
                        'location_care_other': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('location_care_other', form._errors)

    def test_activities_missed(self):
        cleaned_data = {'activities_missed': WORKING,
                        'time_off_work': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('time_off_work', form._errors)

    def test_activities_missed_other(self):
        cleaned_data = {'activities_missed': OTHER,
                        'activities_missed_other': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('activities_missed_other', form._errors)

    def test_loss_of_earnings_yes(self):
        cleaned_data = {'loss_of_earnings': YES,
                        'earnings_lost_amount': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('earnings_lost_amount', form._errors)

    def test_loss_of_earnings_no(self):
        cleaned_data = {'loss_of_earnings': NO,
                        'earnings_lost_amount': 100}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('earnings_lost_amount', form._errors)

    def test_profession(self):
        cleaned_data = {'household_head': NO,
                        'profession': 'teacher'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('profession', form._errors)

    def test_education_years(self):
        cleaned_data = {'household_head': NO,
                        'profession': None,
                        'education_years': 11}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('education_years', form._errors)

    def test_education_certificate(self):
        cleaned_data = {'household_head': NO,
                        'profession': None,
                        'education_years': None,
                        'education_certificate': 'BGCSE'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('education_certificate', form._errors)

    def test_elementary_school(self):
        cleaned_data = {'household_head': NO,
                        'profession': None,
                        'education_years': None,
                        'education_certificate': None,
                        'elementary_school': YES}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('elementary_school', form._errors)

    def test_attendance_years(self):
        cleaned_data = {'household_head': NO,
                        'profession': None,
                        'education_years': None,
                        'education_certificate': None,
                        'elementary_school': NOT_APPLICABLE,
                        'elementary_attendance_years': 10}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('elementary_attendance_years', form._errors)

    def test_secondary_school(self):
        cleaned_data = {'household_head': NO,
                        'profession': None,
                        'education_years': None,
                        'education_certificate': None,
                        'elementary_school': NOT_APPLICABLE,
                        'elementary_attendance_years': None,
                        'secondary_school': YES}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('secondary_school', form._errors)

    def test_secondary_attendance_years(self):
        cleaned_data = {'household_head': NO,
                        'profession': None,
                        'education_years': None,
                        'education_certificate': None,
                        'elementary_school': NOT_APPLICABLE,
                        'elementary_attendance_years': None,
                        'secondary_school': NOT_APPLICABLE,
                        'secondary_attendance_years': 11}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('secondary_attendance_years', form._errors)

    def test_higher_education(self):
        cleaned_data = {'household_head': NO,
                        'profession': None,
                        'education_years': None,
                        'education_certificate': None,
                        'elementary_school': NOT_APPLICABLE,
                        'elementary_attendance_years': None,
                        'secondary_school': NOT_APPLICABLE,
                        'secondary_attendance_years': None,
                        'higher_education': YES}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('higher_education', form._errors)

    def test_higher_attendance_years(self):
        cleaned_data = {'household_head': NO,
                        'profession': None,
                        'education_years': None,
                        'education_certificate': None,
                        'elementary_school': NOT_APPLICABLE,
                        'elementary_attendance_years': None,
                        'secondary_school': NOT_APPLICABLE,
                        'secondary_attendance_years': None,
                        'higher_education': NOT_APPLICABLE,
                        'higher_attendance_years': 11}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('higher_attendance_years', form._errors)

    def test_elementary_attendance_years2(self):
        cleaned_data = {'elementary_school': NO,
                        'elementary_attendance_years': 1}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('elementary_attendance_years', form._errors)

    def test_secondary_attendance_years2(self):
        cleaned_data = {'secondary_school': NO,
                        'secondary_attendance_years': 1}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('secondary_attendance_years', form._errors)

    def test_higher_attendance_years2(self):
        cleaned_data = {'higher_education': NO,
                        'higher_attendance_years': 1}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('higher_attendance_years', form._errors)

    def test_head_attendance_years(self):
        cleaned_data = {'head_elementary': NO,
                        'head_attendance_years': 1}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('head_attendance_years', form._errors)

    def test_head_secondary_years(self):
        cleaned_data = {'head_secondary': NO,
                        'head_secondary_years': 1}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('head_secondary_years', form._errors)

    def test_head_higher_education(self):
        cleaned_data = {'head_higher_education': NO,
                        'head_higher_years': 1}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('head_higher_years', form._errors)
