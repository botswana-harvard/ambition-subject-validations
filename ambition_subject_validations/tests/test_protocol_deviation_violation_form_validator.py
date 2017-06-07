from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO, NOT_APPLICABLE, OTHER

from ..form_validators import ProtocolDeviationViolationFormValidator


class TestProtocolDeviationViolationFormValidator(TestCase):

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
