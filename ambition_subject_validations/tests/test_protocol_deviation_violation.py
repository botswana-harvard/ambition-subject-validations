from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO, POS, NOT_APPLICABLE, OTHER
from edc_base.utils import get_utcnow

from ..validations import ProtocolDeviationViolation


class TestProtocolDeviationViolationValidations(TestCase):

    def test_participant_safety_impact_with_details(self):
        """ Asserts participant_safety_impact has valid
            participant_safety_impact_details provided.
         """
        cleaned_data = {'participant_safety_impact': YES,
                        'participant_safety_impact_details': None}
        protocol_dev = ProtocolDeviationViolation(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, protocol_dev.clean)

        cleaned_data = {'participant_safety_impact': YES,
                        'participant_safety_impact_details': 'explanation'}
        protocol_dev = ProtocolDeviationViolation(cleaned_data=cleaned_data)
        self.assertTrue(protocol_dev.clean())

        cleaned_data = {'participant_safety_impact': NO,
                        'participant_safety_impact_details': None}
        protocol_dev = ProtocolDeviationViolation(cleaned_data=cleaned_data)
        self.assertTrue(protocol_dev.clean())

        cleaned_data = {'participant_safety_impact': NO,
                        'participant_safety_impact_details': 'details'}
        protocol_dev = ProtocolDeviationViolation(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, protocol_dev.clean)

    def test_study_outcomes_impact_with_details(self):
        """ Asserts study_outcomes_impact has valid
            participant_safety_impact_details provided.
         """
        cleaned_data = {'study_outcomes_impact': YES,
                        'study_outcomes_impact_details': None}
        protocol_dev = ProtocolDeviationViolation(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, protocol_dev.clean)

        cleaned_data = {'study_outcomes_impact': YES,
                        'study_outcomes_impact_details': 'explanation'}
        protocol_dev = ProtocolDeviationViolation(cleaned_data=cleaned_data)
        self.assertTrue(protocol_dev.clean())

        cleaned_data = {'study_outcomes_impact': NO,
                        'study_outcomes_impact_details': None}
        protocol_dev = ProtocolDeviationViolation(cleaned_data=cleaned_data)
        self.assertTrue(protocol_dev.clean())

        cleaned_data = {'study_outcomes_impact': NO,
                        'study_outcomes_impact_details': 'details'}
        protocol_dev = ProtocolDeviationViolation(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, protocol_dev.clean)

    def test_other_protocol_violation_require_other_protocol_violation(self):
        cleaned_data = {'protocol_violation_type': OTHER,
                        'other_protocol_violation_type': None}
        protocol_dev = ProtocolDeviationViolation(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, protocol_dev.clean)

        cleaned_data = {'protocol_violation_type': OTHER,
                        'other_protocol_violation_type': NOT_APPLICABLE}
        protocol_dev = ProtocolDeviationViolation(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, protocol_dev.clean)

        cleaned_data = {'protocol_violation_type': OTHER,
                        'other_protocol_violation_type': 'some_violation'}
        protocol_dev = ProtocolDeviationViolation(cleaned_data=cleaned_data)
        self.assertTrue(protocol_dev.clean())
