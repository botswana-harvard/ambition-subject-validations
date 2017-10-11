from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO, OTHER, NOT_APPLICABLE

from ..constants import WORKING
from ..form_validators import HealthEconomicsQuestionnaireFormValidator


class TestHealthEconomicsQuestionnaireFormValidatorFormValidator(TestCase):

    def test_total_money_spent_error(self):
        """Assert raises exception if personal money spent and
        proxy money spent doesn't equal total money spent"""
        cleaned_data = {
            'personal_he_spend': 10,
            'proxy_he_spend': 10,
            'he_spend_last_4weeks': 10
        }
        form_validator = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('he_spend_last_4weeks', form_validator._errors)

    def test_total_money_spent(self):
        """Assert validate that personal money spent and proxy money
        spent equal total money spent"""
        cleaned_data = {
            'personal_he_spend': 10,
            'proxy_he_spend': 10,
            'he_spend_last_4weeks': 20}
        form_validator = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_care_before_hospital_other(self):
        cleaned_data = {'care_before_hospital': OTHER,
                        'care_before_hospital_other': None}
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('care_before_hospital_other', form._errors)

    def test_activities_missed(self):
        cleaned_data = {'activities_missed': WORKING,
                        'time_off_work': None}
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('time_off_work', form._errors)

    def test_activities_missed_other(self):
        cleaned_data = {'activities_missed': OTHER,
                        'activities_missed_other': None}
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('activities_missed_other', form._errors)

    def test_loss_of_earnings_yes(self):
        cleaned_data = {'loss_of_earnings': YES,
                        'earnings_lost_amount': None}
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('earnings_lost_amount', form._errors)

    def test_loss_of_earnings_no(self):
        cleaned_data = {'loss_of_earnings': NO,
                        'earnings_lost_amount': 100}
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('earnings_lost_amount', form._errors)

    def test_profession(self):
        cleaned_data = {'household_head': NO,
                        'profession': 'teacher'}
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('profession', form._errors)

    def test_education_years(self):
        cleaned_data = {'household_head': NO,
                        'profession': None,
                        'education_years': 11}
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('education_years', form._errors)

    def test_education_certificate(self):
        cleaned_data = {'household_head': NO,
                        'profession': None,
                        'education_years': None,
                        'education_certificate': 'BGCSE'}
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('education_certificate', form._errors)

    def test_elementary_school(self):
        cleaned_data = {'household_head': NO,
                        'profession': None,
                        'education_years': None,
                        'education_certificate': None,
                        'elementary_school': YES}
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('elementary_school', form._errors)

    def test_attendance_years(self):
        cleaned_data = {'household_head': NO,
                        'profession': None,
                        'education_years': None,
                        'education_certificate': None,
                        'elementary_school': NOT_APPLICABLE,
                        'elementary_attendance_years': 10}
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
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
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
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
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
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
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
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
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('higher_attendance_years', form._errors)

    def test_elementary_attendance_years2(self):
        cleaned_data = {'elementary_school': NO,
                        'elementary_attendance_years': 1}
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('elementary_attendance_years', form._errors)

    def test_secondary_attendance_years2(self):
        cleaned_data = {'secondary_school': NO,
                        'secondary_attendance_years': 1}
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('secondary_attendance_years', form._errors)

    def test_higher_attendance_years2(self):
        cleaned_data = {'higher_education': NO,
                        'higher_attendance_years': 1}
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('higher_attendance_years', form._errors)

    def test_head_attendance_years(self):
        cleaned_data = {'head_elementary': NO,
                        'head_attendance_years': 1}
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('head_attendance_years', form._errors)

    def test_head_secondary_years(self):
        cleaned_data = {'head_secondary': NO,
                        'head_secondary_years': 1}
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('head_secondary_years', form._errors)

    def test_head_higher_education(self):
        cleaned_data = {'head_higher_education': NO,
                        'head_higher_years': 1}
        form = HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('head_higher_years', form._errors)
