from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_base.utils import get_utcnow

from edc_constants.constants import YES, NO, NOT_APPLICABLE, OTHER
from ambition_subject.constants import DEVIATION, VIOLATION

from ..form_validators import ProtocolDeviationViolationFormValidator
from pprint import pprint


class TestProtocolDeviationViolationFormValidator(TestCase):

    def test_date_violation_datetime_deviation(self):
        """ date_violation_datetime is not required if it's
        a protocol deviation
         """
        cleaned_data = {'deviation_or_violation': DEVIATION,
                        'date_violation_datetime': get_utcnow()}
        form_validator = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_date_violation_datetime_deviation_violation(self):
        """ date_violation_datetime is required if it's
        a protocol violation
         """
        cleaned_data = {'deviation_or_violation': VIOLATION,
                        'date_violation_datetime': None}
        form_validator = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_protocol_violation_type_deviation(self):
        """ protocol_violation_type is not required if it's
        a protocol deviation
         """
        cleaned_data = {'deviation_or_violation': DEVIATION,
                        'protocol_violation_type': 'type'}
        form_validator = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_protocol_violation_type_violation(self):
        """ protocol_violation_type is required if it's
        a protocol violation
         """
        cleaned_data = {'deviation_or_violation': VIOLATION,
                        'protocol_violation_type': None}
        form_validator = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_other_protocol_violation_type_deviation(self):
        """ other_protocol_violation_type is not required if it's
        a protocol deviation
         """
        cleaned_data = {'deviation_or_violation': DEVIATION,
                        'other_protocol_violation_type': 'other type'}
        form_validator = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_other_protocol_violation_type_violation(self):
        """ other_protocol_violation_type is required if it's
        a protocol violation
         """
        cleaned_data = {'deviation_or_violation': VIOLATION,
                        'other_protocol_violation_type': None}
        form_validator = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_violation_description_deviation(self):
        """ violation_description is not required if it's
        a protocol deviation
         """
        cleaned_data = {'deviation_or_violation': DEVIATION,
                        'violation_description': 'description'}
        form_validator = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_violation_description_violation(self):
        """ violation_description is required if it's
        a protocol violation
         """
        cleaned_data = {'deviation_or_violation': VIOLATION,
                        'violation_description': None}
        form_validator = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_violation_reason_deviation(self):
        """ violation_reason is not required if it's
        a protocol deviation
         """
        cleaned_data = {'deviation_or_violation': DEVIATION,
                        'violation_reason': 'reason'}
        form_validator = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_violation_reason_deviation_violation(self):
        """ violation_reason is required if it's
        a protocol violation
         """
        cleaned_data = {'deviation_or_violation': VIOLATION,
                        'violation_reason': None}
        form_validator = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_yes_participant_safety_impact_none_details(self):
        """ Asserts participant_safety_impact has valid
            participant_safety_impact_details provided.
         """
        cleaned_data = {'participant_safety_impact': YES,
                        'participant_safety_impact_details': None}
        protocol_dev = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, protocol_dev.clean)

    def test_yes_participant_safety_impact_with_details(self):
        """ Asserts participant_safety_impact has valid
            participant_safety_impact_details provided.
         """
        cleaned_data = {'participant_safety_impact': YES,
                        'participant_safety_impact_details': 'explanation'}
        protocol_dev = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        try:
            protocol_dev.clean()
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
            protocol_dev.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_no_participant_safety_impact_with_details(self):
        """ Asserts participant_safety_impact has valid
            participant_safety_impact_details provided.
         """
        cleaned_data = {'participant_safety_impact': NO,
                        'participant_safety_impact_details': 'details'}
        protocol_dev = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, protocol_dev.clean)

    def test_study_outcomes_impact_with_details(self):
        """ Asserts study_outcomes_impact has valid
            participant_safety_impact_details provided.
         """
        cleaned_data = {'study_outcomes_impact': YES,
                        'study_outcomes_impact_details': None}
        protocol_dev = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, protocol_dev.clean)

    def test_yes_study_outcomes_impact_with_details(self):
        """ Asserts study_outcomes_impact has valid
            participant_safety_impact_details provided.
         """
        cleaned_data = {'study_outcomes_impact': YES,
                        'study_outcomes_impact_details': 'explanation'}
        protocol_dev = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        try:
            protocol_dev.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_no_study_outcomes_impact_none_details(self):
        cleaned_data = {'study_outcomes_impact': NO,
                        'study_outcomes_impact_details': None}
        protocol_dev = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        try:
            protocol_dev.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_no_study_outcomes_impact_with_details(self):
        cleaned_data = {'study_outcomes_impact': NO,
                        'study_outcomes_impact_details': 'details'}
        protocol_dev = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, protocol_dev.clean)

    def test_other_protocol_violation_none_other_protocol_violation(self):
        cleaned_data = {'protocol_violation_type': OTHER,
                        'other_protocol_violation_type': None}
        protocol_dev = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, protocol_dev.clean)

    def test_other_protocol_violation_na_other_protocol_violation(self):
        cleaned_data = {'protocol_violation_type': OTHER,
                        'other_protocol_violation_type': NOT_APPLICABLE}
        protocol_dev = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, protocol_dev.clean)

    def test_other_protocol_violation_other_protocol_violation(self):
        cleaned_data = {'protocol_violation_type': OTHER,
                        'other_protocol_violation_type': 'some_violation'}
        protocol_dev = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data)
        try:
            protocol_dev.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
