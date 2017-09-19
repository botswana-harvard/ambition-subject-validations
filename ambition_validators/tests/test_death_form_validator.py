from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_constants.constants import OTHER

from ..form_validators import DeathReportFormValidator
from ..constants import TUBERCULOSIS


@tag('Death')
class TestDeathFormValidations(TestCase):

    def test_tb_site_missing(self):
        cleaned_data = {
            'cause_of_death': TUBERCULOSIS,
            'tb_site': None}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('tb_site', form_validator._errors)

    def test_tb_site_ok(self):
        cleaned_data = {
            'cause_of_death': TUBERCULOSIS,
            'tb_site': 'meningitis'}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cause_of_death_other_missing(self):
        cleaned_data = {
            'cause_of_death': OTHER,
            'cause_of_death_other': None}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cause_of_death_other', form_validator._errors)

    def test_cause_of_death_other_ok(self):
        cleaned_data = {
            'cause_of_death': OTHER,
            'cause_of_death_other': 'blah'}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cause_of_death_study_doc_opinion_death_narrative_none(self):
        cleaned_data = {
            'cause_of_death': OTHER,
            'cause_of_death_other': None}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cause_of_death_other', form_validator._errors)

    def test_cause_of_death_study_doctor_tb_no_site_specified_invalid(self):
        cleaned_data = {
            'cause_of_death': TUBERCULOSIS,
            'tb_site': None}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('tb_site', form_validator._errors)

    def test_cause_of_death_study_doc_opinion_no(self):
        cleaned_data = {
            'cause_of_death': TUBERCULOSIS,
            'tb_site': 'meningitis'}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cause_of_death_study_tmg1_tb_no_site_specified_invalid(self):
        cleaned_data = {
            'cause_of_death': TUBERCULOSIS,
            'tb_site': None}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('tb_site', form_validator._errors)

    def test_cause_of_death_study_tmg1_tb_site_specified_valid(self):
        cleaned_data = {
            'cause_of_death': TUBERCULOSIS,
            'tb_site': 'meningitis'}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cause_of_death_study_tmg2_tb_no_site_specified_invalid(self):
        cleaned_data = {
            'cause_of_death': TUBERCULOSIS,
            'tb_site': None}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('tb_site', form_validator._errors)

    def test_cause_of_death_study_tmg2_tb_site_specified_valid(self):
        cleaned_data = {
            'cause_of_death': TUBERCULOSIS,
            'tb_site': 'meningitis'}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
