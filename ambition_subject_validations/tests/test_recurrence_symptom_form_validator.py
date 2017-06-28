from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_base.utils import get_utcnow
from edc_constants.constants import OTHER, YES

from ..form_validators import RecurrenceSymptomFormValidator


class TestRecurrenceSymptomFormValidator(TestCase):

    def test_meningitis_symptom_other_none(self):
        options = {
            'meningitis_symptom': OTHER,
            'meningitis_symptom_other': None}
        form_validator = RecurrenceSymptomFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_meningitis_symptom_other_valid(self):
        options = {
            'meningitis_symptom': OTHER,
            'meningitis_symptom_other': 'blah'}
        form_validator = RecurrenceSymptomFormValidator(cleaned_data=options)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_neurological_focal_neurologic_deficit_none(self):
        options = {
            'neurological': YES,
            'focal_neurologic_deficit': None}
        form_validator = RecurrenceSymptomFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_neurological_focal_neurologic_deficit_valid(self):
        options = {
            'neurological': YES,
            'focal_neurologic_deficit': 'blah'}
        form_validator = RecurrenceSymptomFormValidator(cleaned_data=options)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_amb_administered_no_duration_invalid(self):
        options = {
            'amb_administered': YES,
            'amb_duration': None}
        form_validator = RecurrenceSymptomFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_amb_administered_duration_valid(self):
        options = {
            'amb_administered': YES,
            'amb_duration': 5}
        form_validator = RecurrenceSymptomFormValidator(cleaned_data=options)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_steroids_administered_no_duration_invalid(self):
        options = {
            'steroids_administered': YES,
            'steroids_duration': None}
        form_validator = RecurrenceSymptomFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_steroids_administered_duration_valid(self):
        options = {
            'steroids_administered': YES,
            'steroids_duration': 5}
        form_validator = RecurrenceSymptomFormValidator(cleaned_data=options)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_steroids_administered_no_other_invalid(self):
        options = {
            'steroids_administered': OTHER,
            'steroids_choices_other': None}
        form_validator = RecurrenceSymptomFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_steroids_administered_other_valid(self):
        options = {
            'steroids_administered': OTHER,
            'steroids_choices_other': 'blah'}
        form_validator = RecurrenceSymptomFormValidator(cleaned_data=options)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_antibiotic_treatment_no_other_invalid(self):
        options = {
            'antibiotic_treatment': OTHER,
            'antibiotic_treatment_other': None}
        form_validator = RecurrenceSymptomFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_antibiotic_treatment_other_valid(self):
        options = {
            'antibiotic_treatment': OTHER,
            'antibiotic_treatment_other': 'blah'}
        form_validator = RecurrenceSymptomFormValidator(cleaned_data=options)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_on_arvs_no_date_invalid(self):
        options = {
            'on_arvs': YES,
            'arv_date': None}
        form_validator = RecurrenceSymptomFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_on_arvs_with_date_valid(self):
        options = {
            'on_arvs': YES,
            'arv_date': get_utcnow()}
        form_validator = RecurrenceSymptomFormValidator(cleaned_data=options)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
