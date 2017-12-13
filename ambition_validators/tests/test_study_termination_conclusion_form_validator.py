import uuid
from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import YES, NO, OTHER, NOT_APPLICABLE
from edc_base.utils import get_utcnow

from ..constants import CONSENT_WITHDRAWAL
from ..form_validators import StudyTerminationConclusionFormValidator
from .models import PatientHistory, SubjectVisit, TestModel


class TestStudyTerminationConclusionFormValidator(TestCase):

    def setUp(self):
        self.subject_visit = SubjectVisit.objects.create(
            subject_identifier='11111111',
            appointment_id=uuid.uuid4())

        PatientHistory.objects.create(
            subject_visit=self.subject_visit,
            first_arv_regimen=NOT_APPLICABLE)

        TestModel.objects.create(
            subject_visit=self.subject_visit)

    def test_termination_reason_death_no_death_form_invalid(self):
        cleaned_data = {'termination_reason': 'dead',
                        'death_date': get_utcnow()}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data, patient_history_cls=PatientHistory)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('__all__', form_validator._errors)

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

    def test_no_discharged_after_initial_admission_readmission_invalid(self):
        cleaned_data = {'discharged_after_initial_admission': NO,
                        'initial_discharge_date': None,
                        'readmission_after_initial_discharge': YES}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn(
            'readmission_after_initial_discharge', form_validator._errors)

    def ttest_no_discharged_after_initial_admission_no_readmission_valid(self):
        cleaned_data = {'discharged_after_initial_admission': NO,
                        'initial_discharge_date': None,
                        'readmission_after_initial_discharge': NOT_APPLICABLE}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

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

    def test_died_no_death_date_invalid(self):
        cleaned_data = {'subject_identifier': '11111111',
                        'termination_reason': 'dead',
                        'death_date': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data, patient_history_cls=PatientHistory,
            death_report_cls=TestModel)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('death_date', form_validator._errors)

    def test_twilling_to_complete_10w_withdrawal_of_consent(self):
        """ Asserts willing_to_complete_10w when termination reason
            is consent_withdrawn.
        """
        cleaned_data = {'termination_reason': 'consent_withdrawn',
                        'consent_withdrawal_reason': 'Reason',
                        'willing_to_complete_10w': NOT_APPLICABLE}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('willing_to_complete_10w', form_validator._errors)

    def test_centre_care_transfer_willing_to_complete_in_centre_given(self):
        """ Asserts willing_to_complete_centre when termination reason
            is care_transferred_to_another_institution.
        """
        cleaned_data = {
            'subject_identifier': '11111111',
            'termination_reason': 'care_transferred_to_another_institution',
            'willing_to_complete_centre': NOT_APPLICABLE}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data, patient_history_cls=PatientHistory)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('willing_to_complete_centre', form_validator._errors)

        cleaned_data = {
            'subject_identifier': '11111111',
            'termination_reason': 'care_transferred_to_another_institution',
            'willing_to_complete_centre': NO}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data, patient_history_cls=PatientHistory)
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

    def test_no_willing_tocomplete_10WFU_with_date_to_complete(self):
        cleaned_data = {'willing_to_complete_10w': NO,
                        'willing_to_complete_date': get_utcnow()}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('willing_to_complete_date', form_validator._errors)

    def test_yes_willing_to_complete_centre_none_date_to_complete(self):
        cleaned_data = {'willing_to_complete_centre': YES,
                        'willing_to_complete_date': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('willing_to_complete_date', form_validator._errors)

    def test_no_willing_to_complete_centre_none_date_to_complete(self):
        cleaned_data = {'subject_identifier': '11111111',
                        'willing_to_complete_centre': NO,
                        'willing_to_complete_date': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data, patient_history_cls=PatientHistory)
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
        self.assertIn('willing_to_complete_date', form_validator._errors)

    def test_included_in_error_reason_date_provided(self):
        """ Asserts included_in_error_date when termination reason
            is error_description.
        """
        cleaned_data = {'subject_identifier': '11111111',
                        'termination_reason': 'included_in_error',
                        'included_in_error': 'blah blah blah blah',
                        'included_in_error_date': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data, patient_history_cls=PatientHistory)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('included_in_error_date', form_validator._errors)

        cleaned_data = {'subject_identifier': '11111111',
                        'termination_reason': 'included_in_error',
                        'included_in_error': 'blah blah blah blah',
                        'included_in_error_date': get_utcnow()}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data, patient_history_cls=PatientHistory)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_included_in_error_reason_narrative_provided(self):
        """ Asserts included_in_error_date when termination reason
            is included_in_error.
        """
        cleaned_data = {'subject_identifier': '11111111',
                        'termination_reason': 'included_in_error',
                        'included_in_error_date': get_utcnow(),
                        'included_in_error': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data, patient_history_cls=PatientHistory)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('included_in_error', form_validator._errors)

        cleaned_data = {'subject_identifier': '11111111',
                        'termination_reason': 'included_in_error',
                        'included_in_error_date': get_utcnow(),
                        'included_in_error': 'blah blah blah blah'}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data, patient_history_cls=PatientHistory)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_other_late_protocol_exclusion_none_date_to_complete(self):
        cleaned_data = {
            'first_line_regimen': OTHER,
            'first_line_regimen_other': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('first_line_regimen_other', form_validator._errors)

    def test_other_second_line_regimen_none_second_line_regime_other(self):
        cleaned_data = {
            'second_line_regimen': OTHER,
            'second_line_regimen_other': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('second_line_regimen_other', form_validator._errors)

    def test_date_arvs_started_or_switched_none_arvs_delay_reason(self):

        cleaned_data = {
            'subject_identifier': '11111111',
            'first_line_regimen': NOT_APPLICABLE,
            'arvs_delay_reason': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data, patient_history_cls=PatientHistory)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('arvs_delay_reason', form_validator._errors)

    def test_na_date_arvs_started_or_switched_with_arvs_delay_reason(self):
        cleaned_data = {
            'subject_identifier': '11111111',
            'first_line_regimen': NOT_APPLICABLE,
            'arvs_delay_reason': 'bahblah'}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data, patient_history_cls=PatientHistory)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_consent_withdrawal_reason_invalid(self):
        cleaned_data = {'termination_reason': CONSENT_WITHDRAWAL,
                        'consent_withdrawal_reason': None}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('consent_withdrawal_reason', form_validator._errors)

    def test_consent_withdrawal_reason_valid(self):
        cleaned_data = {'termination_reason': CONSENT_WITHDRAWAL,
                        'consent_withdrawal_reason': 'Reason'}
        form_validator = StudyTerminationConclusionFormValidator(
            cleaned_data=cleaned_data, patient_history_cls=PatientHistory)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
