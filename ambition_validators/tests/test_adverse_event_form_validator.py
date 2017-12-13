from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_constants.constants import YES, NO, UNKNOWN, NOT_APPLICABLE
from edc_form_validators import NOT_REQUIRED_ERROR

from ..form_validators import AdverseEventFormValidator


class TestAdverseEventFormValidator(TestCase):

    def test_ae_cause_yes(self):
        options = {
            'ae_cause': YES,
            'ae_cause_other': None}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('ae_cause_other', form_validator._errors)

    def test_ae_cause_no(self):
        options = {
            'ae_cause': NO,
            'ae_cause_other': YES}
        form_validator = AdverseEventFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('ae_cause_other',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_single_dose_drug_relation_invalid(self):
        options = {
            'regimen': 'Single dose',
            'ae_study_relation_possibility': YES,
            'ambisome_relation': NOT_APPLICABLE,
        }
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('ambisome_relation', form_validator._errors)

    def test_sae_reason_not_applicable(self):
        options = {
            'sae': YES,
            'sae_reason': NOT_APPLICABLE}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('sae_reason', form_validator._errors)

    def test_susar_reported_not_applicable(self):
        options = {
            'susar': YES,
            'susar_reported': NOT_APPLICABLE}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('susar_reported', form_validator._errors)
