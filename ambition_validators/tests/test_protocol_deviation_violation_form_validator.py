from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO, OTHER

from ..constants import DEVIATION, VIOLATION, MEDICATION_NONCOMPLIANCE
from ..form_validators import ProtocolDeviationViolationFormValidator


@tag('deviation')
class TestDeviationViolationFormValidator(TestCase):

    def test_deviation_or_violation(self):
        """ date_violation_datetime is not required if it's
        a protocol deviation
         """
        field_required_list = [
            ('date_violation_datetime', get_utcnow()),
            ('protocol_violation_type', MEDICATION_NONCOMPLIANCE),
            ('violation_description', "test description"),
            ('violation_reason', "test violation reason")]
        for field_item in field_required_list:
            field, value = field_item
            cleaned_data = {
                'deviation_or_violation': DEVIATION, field: value}
            form_validator = ProtocolDeviationViolationFormValidator(
                cleaned_data=cleaned_data)
            self.assertRaises(ValidationError, form_validator.validate)
            self.assertIn(field, form_validator._errors)

    def test_deviation_or_violation1(self):
        """ deviation_or_violation is DEVIATION then
        (date_violation_datetime, protocol_violation_type, etc) should be None.
         """
        field_required_list = [
            ('date_violation_datetime', None),
            ('protocol_violation_type', None),
            ('violation_description', None),
            ('violation_reason', None)]
        for field_item in field_required_list:
            field, value = field_item
            cleaned_data = {'deviation_or_violation': DEVIATION, field: value}
            form_validator = ProtocolDeviationViolationFormValidator(
                cleaned_data=cleaned_data)
            self.assertFalse(form_validator._errors)
            
    def test_violation(self):
        """ date_violation_datetime is not required if it's
        a protocol deviation
         """
        field_required_list = [
            ('date_violation_datetime', get_utcnow()),
            ('protocol_violation_type', MEDICATION_NONCOMPLIANCE),
            ('violation_description', "test description"),
            ('violation_reason', "test violation reason")]
        for field_item in field_required_list:
            field, value = field_item
            cleaned_data = {
                'deviation_or_violation': VIOLATION, field: value}
            form_validator = ProtocolDeviationViolationFormValidator(
                cleaned_data=cleaned_data)
            self.assertFalse(form_validator._errors)
            
            
    def test_violation1(self):
        """ date_violation_datetime is not required if it's
        a protocol deviation
         """
        field_required_list = [
            ('date_violation_datetime', None),
            ('protocol_violation_type', None),
            ('violation_description', None),
            ('violation_reason', None)]
        for field_item in field_required_list:
            field, value = field_item
            cleaned_data = {
                'deviation_or_violation': VIOLATION, field: value}
            form_validator = ProtocolDeviationViolationFormValidator(
                cleaned_data=cleaned_data)
            self.assertRaises(ValidationError, form_validator.validate)
            self.assertIn(field, form_validator._errors)
 
    def test_yes_participant_safety_impact_none_details(self):
        """ Asserts participant_safety_impact has valid
            participant_safety_impact_details provided.
         """
        cleaned_data = {'participant_safety_impact': YES,
                        'participant_safety_impact_details': None}
        form_validator = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn(
            'participant_safety_impact_details', form_validator._errors)

    def test_yes_participant_safety_impact_with_details(self):
        """ Asserts participant_safety_impact has valid
            participant_safety_impact_details provided.
         """
        cleaned_data = {'participant_safety_impact': YES,
                        'participant_safety_impact_details': 'explanation'}
        protocol_dev = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        try:
            protocol_dev.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
 
    def test_no_participant_safety_impact_none_details(self):
        """ Asserts participant_safety_impact has valid
            participant_safety_impact_details provided.
         """
        cleaned_data = {'participant_safety_impact': NO,
                        'participant_safety_impact_details': None}
        protocol_dev = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        try:
            protocol_dev.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_no_participant_safety_impact_with_details(self):
        """ Asserts participant_safety_impact has valid
            participant_safety_impact_details provided.
         """
        cleaned_data = {'participant_safety_impact': NO,
                        'participant_safety_impact_details': 'details'}
        form_validator = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn(
            'participant_safety_impact_details', form_validator._errors)
 
    def test_study_outcomes_impact_with_details(self):
        """ Asserts study_outcomes_impact has valid
            participant_safety_impact_details provided.
         """
        cleaned_data = {'study_outcomes_impact': YES,
                        'study_outcomes_impact_details': None}
        form_validator = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn(
            'study_outcomes_impact_details', form_validator._errors)

    def test_yes_study_outcomes_impact_with_details(self):
        """ Asserts study_outcomes_impact has valid
            participant_safety_impact_details provided.
         """
        cleaned_data = {'study_outcomes_impact': YES,
                        'study_outcomes_impact_details': 'explanation'}
        protocol_dev = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        try:
            protocol_dev.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
 
    def test_no_study_outcomes_impact_none_details(self):
        cleaned_data = {'study_outcomes_impact': NO,
                        'study_outcomes_impact_details': None}
        protocol_dev = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        try:
            protocol_dev.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
 
    def test_no_study_outcomes_impact_with_details(self):
        cleaned_data = {'study_outcomes_impact': NO,
                        'study_outcomes_impact_details': 'details'}
        form_validator = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn(
            'study_outcomes_impact_details', form_validator._errors)
 
    def test_other_protocol_violation_none_other_protocol_violation(self):
        cleaned_data = {'protocol_violation_type': OTHER,
                        'protocol_violation_type_other': None}
        form_validator = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn(
            'protocol_violation_type_other', form_validator._errors)
 
    def test_other_protocol_violation_other_protocol_violation(self):
        cleaned_data = {'protocol_violation_type': OTHER,
                        'protocol_violation_type_other': 'some_violation'}
        protocol_dev = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        try:
            protocol_dev.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
