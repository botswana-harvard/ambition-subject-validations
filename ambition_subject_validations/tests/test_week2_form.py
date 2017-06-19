from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_base.utils import get_utcnow
from edc_constants.constants import YES

from ..form_validators import Week2FormValidator


class TestWeek2Form(TestCase):

    def test_discharged_yes_require_discharged_date(self):
        cleaned_data = {'discharged': YES,
                        'discharge_date': None}
        week2 = Week2FormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, week2.clean)

        cleaned_data = {'discharged': YES,
                        'discharge_date': get_utcnow()}
        week2 = Week2FormValidator(cleaned_data=cleaned_data)

        try:
            week2.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_died_yes_require_date_of_death(self):
        cleaned_data = {'died': YES,
                        'death_date': None}
        week2 = Week2FormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, week2.clean)

        cleaned_data = {'died': YES,
                        'death_date': get_utcnow()}
        week2 = Week2FormValidator(cleaned_data=cleaned_data)

        try:
            week2.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_blood_recieved_yes_requires_units(self):
        cleaned_data = {'blood_received': YES,
                        'units': None}
        week2 = Week2FormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, week2.clean)

        cleaned_data = {'blood_received': YES,
                        'units': 2}
        week2 = Week2FormValidator(cleaned_data=cleaned_data)

        try:
            week2.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
