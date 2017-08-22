from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO, NORMAL, OTHER

from ..form_validators import RadiologyFormValidator


class TestRadiolodyFormValidator(TestCase):

    def test_cxr_type_none(self):
        options = {'is_cxr_done': YES, 'cxr_type': None}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cxr_type', form_validator._errors)

    def test_cxr_type_normal(self):
        options = {'is_cxr_done': NO, 'cxr_type': NORMAL}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cxr_type', form_validator._errors)

    def test_cxr_date_none(self):
        options = {'is_cxr_done': YES,
                   'cxr_type': 'blah',
                   'cxr_date': None}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cxr_date', form_validator._errors)

    def test_cxr_date_not_none(self):
        options = {'is_cxr_done': NO, 'cxr_date': get_utcnow().date}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cxr_date', form_validator._errors)

    def test_infiltrate_location_none(self):
        options = {
            'cxr_type': 'infiltrates', 'infiltrate_location': None}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('infiltrate_location', form_validator._errors)

    def test_infiltrate_location_not_none(self):
        options = {
            'cxr_type': NORMAL, 'infiltrate_location': 'lul'}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('infiltrate_location', form_validator._errors)

    def test_is_scanned_with_contrast_none(self):
        options = {
            'is_ct_performed': YES, 'is_scanned_with_contrast': None}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('is_scanned_with_contrast', form_validator._errors)

    def test_is_scanned_with_contrast_no(self):
        options = {
            'is_ct_performed': NO, 'is_scanned_with_contrast': NO}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('is_scanned_with_contrast', form_validator._errors)

    def test_date_ct_performed_none(self):
        options = {
            'is_ct_performed': YES,
            'is_scanned_with_contrast': YES,
            'date_ct_performed': None}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('date_ct_performed', form_validator._errors)

    def test_date_ct_performed_not_none(self):
        options = {
            'is_ct_performed': NO, 'date_ct_performed': get_utcnow().date}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('date_ct_performed', form_validator._errors)

    def test_brain_imaging_reason_none(self):
        options = {
            'is_ct_performed': YES,
            'is_scanned_with_contrast': YES,
            'date_ct_performed': get_utcnow(),
            'are_results_abnormal': NO,
            'brain_imaging_reason': None}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('brain_imaging_reason', form_validator._errors)

    def test_brain_imaging_reason_not_none(self):
        options = {
            'is_ct_performed': NO, 'brain_imaging_reason': 'new_neurology'}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('brain_imaging_reason', form_validator._errors)

    def test_brain_imaging_reason_other_none(self):
        options = {
            'brain_imaging_reason': OTHER,
            'brain_imaging_reason_other': None}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('brain_imaging_reason_other', form_validator._errors)

    def test_brain_imaging_reason_other_not_none(self):
        options = {
            'brain_imaging_reason': 'new_neurology',
            'brain_imaging_reason_other': 'tumor'}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('brain_imaging_reason_other', form_validator._errors)

    def test_are_results_abnormal_none(self):
        options = {
            'is_ct_performed': YES,
            'is_scanned_with_contrast': YES,
            'date_ct_performed': get_utcnow(),
            'brain_imaging_reason': 'blah',
            'are_results_abnormal': None}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_abnormal', form_validator._errors)

    def test_are_results_abnormal_not_none(self):
        options = {
            'is_ct_performed': NO,
            'are_results_abnormal': NO}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_abnormal', form_validator._errors)

    def test_abnormal_results_reason_none(self):
        options = {
            'are_results_abnormal': YES,
            'abnormal_results_reason': None}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('abnormal_results_reason', form_validator._errors)

    def test_abnormal_results_reason_not_none(self):
        options = {
            'are_results_abnormal': NO,
            'abnormal_results_reason': 'tumor'}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('abnormal_results_reason', form_validator._errors)

    def test_abnormal_results_reason_other_none(self):
        options = {
            'abnormal_results_reason': OTHER,
            'abnormal_results_reason_other': None}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('abnormal_results_reason_other', form_validator._errors)

    def test_abnormal_results_reason_other_not_none(self):
        options = {
            'abnormal_results_reason': 'cerebral_oedema',
            'abnormal_results_reason_other': 'tumor'}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('abnormal_results_reason_other', form_validator._errors)

    def test_if_infarcts_location_none(self):
        options = {
            'abnormal_results_reason': 'infarcts',
            'if_infarcts_location': None}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('if_infarcts_location', form_validator._errors)

    def test_if_infarcts_location_not_none(self):
        options = {
            'abnormal_results_reason': 'cerebral_oedema',
            'if_infarcts_location': 'chest'}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('if_infarcts_location', form_validator._errors)
