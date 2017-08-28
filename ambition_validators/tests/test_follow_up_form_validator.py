from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO, OTHER

from ..constants import WORKING
from ..form_validators import FollowUpFormValidator


class TestFollowUpFormValidator(TestCase):

    def test_rifampicin_started_yes_require_rifampicin_start_date(self):
        cleaned_data = {'rifampicin_started': YES,
                        'rifampicin_start_date': None}
        form_validator = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('rifampicin_start_date', form_validator._errors)

        cleaned_data = {'rifampicin_started': YES,
                        'rifampicin_start_date': get_utcnow()}
        form_validator = FollowUpFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_rifampicin_started_no_require_rifampicin_start_datee(self):
        cleaned_data = {'rifampicin_started': NO,
                        'rifampicin_start_date': get_utcnow()}
        form_validator = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('rifampicin_start_date', form_validator._errors)

        cleaned_data = {'rifampicin_started': NO,
                        'rifampicin_start_date': None}
        form_validator = FollowUpFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_fluconazole_dose_yes_require_other_fluconazole_dose_reason(self):
        cleaned_data = {'fluconazole_dose': YES,
                        'other_fluconazole_dose_reason': None}
        form_validator = FollowUpFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

        cleaned_data = {'fluconazole_dose': YES,
                        'other_fluconazole_dose_reason': 'reason'}
        form_validator = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('other_fluconazole_dose_reason', form_validator._errors)

    def test_fluconazole_dosed_no_require_rifampicin_start_datee(self):
        cleaned_data = {'fluconazole_dose': NO,
                        'other_fluconazole_dose_reason': 'reason'}
        form_validator = FollowUpFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

        cleaned_data = {'fluconazole_dose': NO,
                        'other_fluconazole_dose_reason': None}
        form_validator = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('other_fluconazole_dose_reason', form_validator._errors)

    def test_other_fluconazole_dose_yes_require_other_fluconazole_dose_reason(self):
        cleaned_data = {'other_fluconazole_dose': YES,
                        'other_fluconazole_dose_reason': None}
        form_validator = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('other_fluconazole_dose_reason', form_validator._errors)

        cleaned_data = {'other_fluconazole_dose': YES,
                        'other_fluconazole_dose_reason': 'reason'}
        form_validator = FollowUpFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_other_fluconazole_dose_no_require_rifampicin_start_datee(self):
        cleaned_data = {'other_fluconazole_dose': NO,
                        'other_fluconazole_dose_reason': 'reason'}
        form_validator = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('other_fluconazole_dose_reason', form_validator._errors)

        cleaned_data = {'other_fluconazole_dose': NO,
                        'other_fluconazole_dose_reason': None}
        form_validator = FollowUpFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_care_before_hospital_yes(self):
        cleaned_data = {'care_before_hospital': YES,
                        'location_care': None}
        form = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('location_care', form._errors)

    def test_care_before_hospital_no(self):
        cleaned_data = {'care_before_hospital': NO,
                        'location_care': 'healthcare'}
        form = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('location_care', form._errors)

    def test_care_before_hospital_other(self):
        cleaned_data = {'care_before_hospital': OTHER,
                        'care_before_hospital_other': None}
        form = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('care_before_hospital_other', form._errors)

    def test_location_care_other(self):
        cleaned_data = {'location_care': OTHER,
                        'location_care_other': None}
        form = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('location_care_other', form._errors)

    def test_medication_bought(self):
        cleaned_data = {'medication_bought': YES,
                        'medication_payment': None}
        form = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('medication_payment', form._errors)

    def test_activities_missed(self):
        cleaned_data = {'activities_missed': WORKING,
                        'time_off_work': None}
        form = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('time_off_work', form._errors)

    def test_activities_missed_other(self):
        cleaned_data = {'activities_missed': OTHER,
                        'activities_missed_other': None}
        form = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('activities_missed_other', form._errors)

    def test_loss_of_earnings_yes(self):
        cleaned_data = {'loss_of_earnings': YES,
                        'earnings_lost_amount': None}
        form = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('earnings_lost_amount', form._errors)

    def test_loss_of_earnings_no(self):
        cleaned_data = {'loss_of_earnings': NO,
                        'earnings_lost_amount': 100}
        form = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('earnings_lost_amount', form._errors)
