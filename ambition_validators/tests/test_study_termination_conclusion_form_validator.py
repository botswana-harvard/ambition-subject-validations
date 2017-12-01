from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import YES, NO, OTHER, NOT_APPLICABLE
from edc_base.utils import get_utcnow

from ..form_validators import StudyTerminationConclusionFormValidator


class TestStudyTerminationConclusionFormValidator(TestCase):

    def test_yes_discharged_after_initial_admission_none_date_discharged(self):
        cleaned_data = {'discharged_after_initial_admission': YES,
                        'initial_discharge_date': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('initial_discharge_date', form_validator._errors)

    def test_no_discharged_after_initial_admission_with_date_discharged(self):
        cleaned_data = {'discharged_after_initial_admission': NO,
                        'initial_discharge_date': get_utcnow}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('initial_discharge_date', form_validator._errors)

    def test_yes_readmission_none_readmission_date(self):
        cleaned_data = {'readmission_after_initial_discharge': YES,
                        'readmission_date': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('readmission_date', form_validator._errors)

    def test_no_readmission_with_readmission_date(self):
        cleaned_data = {'readmission_after_initial_discharge': NO,
                        'readmission_date': get_utcnow}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('readmission_date', form_validator._errors)

    def test_termination_reason_require_consent_withdrawal_reason(self):
        """ Asserts consent_withdrawal_reason when termination reason
            is withdrawal_of_subject_consent.
        """
        cleaned_data = {'termination_reason': 'withdrawal_of_subject_consent',
                        'consent_withdrawal_reason': None,
                        'willing_to_complete_10w': NO}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('consent_withdrawal_reason', form_validator._errors)

        cleaned_data = {'termination_reason': 'withdrawal_of_subject_consent',
                        'consent_withdrawal_reason': 'blah',
                        'willing_to_complete_10w': NO}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
        self.assertNotIn('consent_withdrawal_reason', form_validator._errors)

    def test_twilling_to_complete_10w_withdrawal_of_consent(self):
        """ Asserts willing_to_complete_10w when termination reason
            is withdrawal_of_subject_consent.
        """
        cleaned_data = {'termination_reason': 'withdrawal_of_subject_consent',
                        'consent_withdrawal_reason': 'blah',
                        'willing_to_complete_10w': NOT_APPLICABLE}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn(
            'willing_to_complete_10w', form_validator._errors)

    def test_included_in_error_reason_date_provided(self):
        """ Asserts included_in_error_date when termination reason
            is error_description.
        """
        cleaned_data = {'termination_reason': 'included_in_error',
                        'included_in_error': 'blah blah blah blah',
                        'included_in_error_date': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

        cleaned_data = {'termination_reason': 'included_in_error',
                        'included_in_error': 'blah blah blah blah',
                        'included_in_error_date': get_utcnow()}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_included_in_error_reason_narrative_provided(self):
        """ Asserts included_in_error_date when termination reason
            is included_in_error.
        """
        cleaned_data = {'termination_reason': 'included_in_error',
                        'included_in_error_date': get_utcnow(),
                        'included_in_error': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

        cleaned_data = {'termination_reason': 'included_in_error',
                        'included_in_error_date': get_utcnow(),
                        'included_in_error': 'blah blah blah blah'}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_centre_care_transfer_willing_to_complete_in_centre_given(self):
        """ Asserts willing_to_complete_centre when termination reason
            is care_transferred_to_another_institution.
        """
        cleaned_data = {'termination_reason': 'care_transferred_to_another_institution',
                        'willing_to_complete_centre': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

        cleaned_data = {'termination_reason': 'care_transferred_to_another_institution',
                        'willing_to_complete_centre': NO}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_yes_willing_to_complete_willing_to_complete_date(self):
        cleaned_data = {'willing_to_complete_10w': YES,
                        'willing_to_complete_date': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('willing_to_complete_date', form_validator._errors)

    def test_non_consent_termination_reason(self):
        cleaned_data = {'termination_reason': '10_weeks_completed_followUp',
                        'consent_withdrawal_reason': 'reason is given'}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

    def test_yes_willing_tocomplete_10WFU_none_date_to_complete(self):
        cleaned_data = {'willing_to_complete_10w': YES,
                        'date_willing_to_complete': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

    def test_no_willing_tocomplete_10WFU_none_date_to_complete(self):
        cleaned_data = {'willing_to_complete_10w': NO,
                        'date_willing_to_complete': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_no_willing_tocomplete_10WFU_with_date_to_complete(self):
        cleaned_data = {'willing_to_complete_10w': NO,
                        'willing_to_complete_date': get_utcnow()}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

    def test_yes_willing_to_complete_centre_none_date_to_complete(self):
        cleaned_data = {'willing_to_complete_centre': YES,
                        'date_willing_to_complete': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

    def test_no_willing_to_complete_centre_none_date_to_complete(self):
        cleaned_data = {'willing_to_complete_centre': NO,
                        'date_willing_to_complete': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_no_willing_to_complete_centreU_with_date_to_complete(self):
        cleaned_data = {'willing_to_complete_centre': NO,
                        'willing_to_complete_date': get_utcnow()}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

    def test_other_late_protocol_exclusion_none_date_to_complete(self):
        cleaned_data = {
            'first_line_regimen': OTHER,
            'first_line_regimen_other': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn(
            'first_line_regimen_other', form_validator._errors)

    def test_other_first_line_regimen_none_first_line_regime_other(self):
        cleaned_data = {
            'first_line_regimen_patients': OTHER,
            'first_line_regimen_patients_other':
            'TDF +3TC/FTC + either EFZ or NVP'}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_other_second_line_regimen_none_second_line_regime_other(self):
        cleaned_data = {
            'second_line_regimen': OTHER,
            'second_line_regimen_other': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn(
            'second_line_regimen_other', form_validator._errors)

    def test_other_first_line_regimen_with_second_line_regime_other(self):
        cleaned_data = {
            'second_line_regimen_patients': OTHER,
            'second_line_regimen_patients_other': 'regime'}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_date_arvs_started_or_switched_none_arvs_delay_reason(self):
        cleaned_data = {
            'arvs_switch_date': None,
            'arvs_delay_reason': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

    def test_date_arvs_started_or_switched_with_arvs_delay_reason(self):
        cleaned_data = {
            'date_arvs_started_or_switched': None,
            'arvs_delay_reason': 'unavailability'}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_na_date_arvs_started_or_switched_with_arvs_delay_reason(self):
        cleaned_data = {
            'arvs_switch_date': get_utcnow(),
            'arvs_delay_reason': 'unavailability'}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
