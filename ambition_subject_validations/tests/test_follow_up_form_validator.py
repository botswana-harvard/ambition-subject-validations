from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO
from edc_base.utils import get_utcnow

from ..form_validators import FollowUpFormValidator


class TestFollowUpFormValidator(TestCase):

    def test_rifampicin_started_yes_require_rifampicin_start_date(self):
        cleaned_data = {'rifampicin_started': YES,
                        'rifampicin_start_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'rifampicin_started': YES,
                        'rifampicin_start_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        try:
            follow_up.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_rifampicin_started_no_require_rifampicin_start_datee(self):
        cleaned_data = {'rifampicin_started': NO,
                        'rifampicin_start_date': get_utcnow()}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'rifampicin_started': NO,
                        'rifampicin_start_date': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        try:
            follow_up.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_fluconazole_dose_yes_require_other_fluconazole_dose_reason(self):
        cleaned_data = {'fluconazole_dose': YES,
                        'other_fluconazole_dose_reason': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        try:
            follow_up.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

        cleaned_data = {'fluconazole_dose': YES,
                        'other_fluconazole_dose_reason': 'reason'}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

    def test_fluconazole_dosed_no_require_rifampicin_start_datee(self):
        cleaned_data = {'fluconazole_dose': NO,
                        'other_fluconazole_dose_reason': 'reason'}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        try:
            follow_up.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

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
        try:
            follow_up.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def other_fluconazole_dose_no_require_rifampicin_start_datee(self):
        cleaned_data = {'other_fluconazole_dose': NO,
                        'other_fluconazole_dose_reason': 'reason'}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)

        cleaned_data = {'other_fluconazole_dose': NO,
                        'other_fluconazole_dose_reason': None}
        follow_up = FollowUpFormValidator(cleaned_data=cleaned_data)
        try:
            follow_up.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
