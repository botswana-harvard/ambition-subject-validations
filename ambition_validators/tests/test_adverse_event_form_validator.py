from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO, UNKNOWN, NOT_APPLICABLE
from edc_base.modelform_validators import NOT_REQUIRED_ERROR

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

    def test_ae_study_relation_possibility_no(self):
        options = {
            'ae_study_relation_possibility': NO,
            'possiblity_detail': None}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('possiblity_detail', form_validator._errors)

    def test_ae_study_relation_possibility_unknown(self):
        options = {
            'ae_study_relation_possibility': UNKNOWN,
            'possiblity_detail': None}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('possiblity_detail', form_validator._errors)

    def test_ae_study_relation_possibility_yes(self):
        options = {
            'ae_study_relation_possibility': YES,
            'possiblity_detail': NO}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('possiblity_detail', form_validator._errors)

    def test_ambisome_relation_NA_regimen_1(self):
        options = {
            'regimen': 'regimen_1',
            'ae_study_relation_possibility': YES,
            'ambisome_relation': NOT_APPLICABLE}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('ambisome_relation', form_validator._errors)

    def test_ambisome_relation_regimen_1_valid(self):
        options = {
            'ae_study_relation_possibility': YES,
            'regimen': 'regimen_1',
            'flucytosine_relation': 'possibly_related',
            'ambisome_relation': 'possibly_related'}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_fluconazole_relation_NA_regimen_1(self):
        options = {
            'ae_study_relation_possibility': YES,
            'regimen': 'regimen_1',
            'flucytosine_relation': 'possibly_related',
            'fluconazole_relation': NOT_APPLICABLE}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('fluconazole_relation', form_validator._errors)

    def test_fluconazole_relation_regimen_1_valid(self):
        options = {
            'ae_study_relation_possibility': YES,
            'regimen': 'regimen_1',
            'flucytosine_relation': 'possibly_related',
            'fluconazole_relation': 'possibly_related'}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_amphotericin_b_relation_NA_regimen_2(self):
        options = {
            'ae_study_relation_possibility': YES,
            'regimen': 'regimen_2',
            'flucytosine_relation': 'possibly_related',
            'amphotericin_b_relation': NOT_APPLICABLE}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('amphotericin_b_relation', form_validator._errors)

    def test_amphotericin_b_relation_regimen_2_valid(self):
        options = {
            'ae_study_relation_possibility': YES,
            'regimen': 'regimen_2',
            'flucytosine_relation': 'possibly_related',
            'amphotericin_b_relation': 'possibly_related'}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_flucytosine_relation_NA_invalid(self):
        options = {
            'ae_study_relation_possibility': YES,
            'flucytosine_relation': NOT_APPLICABLE}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('flucytosine_relation', form_validator._errors)

    def test_flucytosine_relation_valid(self):
        options = {
            'ae_study_relation_possibility': YES,
            'flucytosine_relation': 'possibly_related'}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
