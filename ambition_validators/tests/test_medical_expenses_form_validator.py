from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import YES, NO, OTHER

from ..constants import WORKING
from ..form_validators import MedicalExpensesFormValidator


class TestMedicalExpensesFormValidator(TestCase):

    def test_total_money_spent_error(self):
        """Assert raises exception if personal money spent and
        proxy money spent doesn't equal total money spent"""
        cleaned_data = {
            'personal_he_spend': 10,
            'proxy_he_spend': 10,
            'he_spend_last_4weeks': 10
        }
        form_validator = MedicalExpensesFormValidator(
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
        form_validator = MedicalExpensesFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_care_before_hospital_other(self):
        cleaned_data = {'care_before_hospital': OTHER,
                        'care_before_hospital_other': None}
        form = MedicalExpensesFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('care_before_hospital_other', form._errors)

    def test_activities_missed(self):
        cleaned_data = {'activities_missed': WORKING,
                        'time_off_work': None}
        form = MedicalExpensesFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('time_off_work', form._errors)

    def test_activities_missed_other(self):
        cleaned_data = {'activities_missed': OTHER,
                        'activities_missed_other': None}
        form = MedicalExpensesFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('activities_missed_other', form._errors)

    def test_loss_of_earnings_yes(self):
        cleaned_data = {'loss_of_earnings': YES,
                        'earnings_lost_amount': None}
        form = MedicalExpensesFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('earnings_lost_amount', form._errors)

    def test_loss_of_earnings_no(self):
        cleaned_data = {'loss_of_earnings': NO,
                        'earnings_lost_amount': 100}
        form = MedicalExpensesFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('earnings_lost_amount', form._errors)
