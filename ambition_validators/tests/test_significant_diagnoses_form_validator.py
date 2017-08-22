from django import forms
from django.test import TestCase

from edc_constants.constants import YES, OTHER
from edc_base.modelform_validators import REQUIRED_ERROR

from ..form_validators import SignificantDiagnosesFormValidator


class TestSignificantDiagnosesFormValidator(TestCase):

    def test_other_significant_diagnoses(self):
        options = {
            'other_significant_diagnoses': YES,
            'possible_diagnoses': None}
        form_validator = SignificantDiagnosesFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('possible_diagnoses',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_possible_diagnoses_pulmonary_tb(self):
        options = {
            'possible_diagnoses': 'pulmonary_tb',
            'dx_date': None}
        form_validator = SignificantDiagnosesFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('dx_date',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_possible_diagnoses_extra_pulmonary_tb(self):
        options = {
            'possible_diagnoses': 'extra_pulmonary_tb',
            'dx_date': None}
        form_validator = SignificantDiagnosesFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('dx_date',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_possible_diagnoses_kaposi_sarcoma(self):
        options = {
            'possible_diagnoses': 'kaposi_sarcoma',
            'dx_date': None}
        form_validator = SignificantDiagnosesFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('dx_date',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_possible_diagnoses_malaria(self):
        options = {
            'possible_diagnoses': 'malaria',
            'dx_date': None}
        form_validator = SignificantDiagnosesFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('dx_date',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_possible_diagnoses_bacteraemia(self):
        options = {
            'possible_diagnoses': 'bacteraemia',
            'dx_date': None}
        form_validator = SignificantDiagnosesFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('dx_date',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_possible_diagnoses_pneumonia(self):
        options = {
            'possible_diagnoses': 'pneumonia',
            'dx_date': None}
        form_validator = SignificantDiagnosesFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('dx_date',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_possible_diagnoses_diarrhoeal_wasting(self):
        options = {
            'possible_diagnoses': 'diarrhoeal_wasting',
            'dx_date': None}
        form_validator = SignificantDiagnosesFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('dx_date',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_possible_diagnoses_dx_other(self):
        options = {
            'possible_diagnoses': OTHER,
            'dx_other': None}
        form_validator = SignificantDiagnosesFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('dx_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)
