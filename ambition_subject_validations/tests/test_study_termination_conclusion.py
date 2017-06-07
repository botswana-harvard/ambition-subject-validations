from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO
from edc_base.utils import get_utcnow


from ..validations import StudyTerminationConclusion


class TestStudyTerminationConclusionValidations(TestCase):

    def test_discharged_after_initial_admission_require_date_discharged(self):
        cleaned_data = {'discharged_after_initial_admission': YES,
                        'date_initial_discharge': None}
        form = StudyTerminationConclusion(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

        cleaned_data = {'discharged_after_initial_admission': YES,
                        'date_initial_discharge': get_utcnow}
        form = StudyTerminationConclusion(cleaned_data=cleaned_data)
        self.assertTrue(form.clean())

        cleaned_data = {'discharged_after_initial_admission': NO,
                        'date_initial_discharge': None}
        form = StudyTerminationConclusion(cleaned_data=cleaned_data)
        self.assertTrue(form.clean())

        cleaned_data = {'discharged_after_initial_admission': NO,
                        'date_initial_discharge': get_utcnow}
        form = StudyTerminationConclusion(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_readmission_require_readmission_date(self):
        cleaned_data = {'readmission_after_initial_discharge': YES,
                        'date_readmission': None}
        form = StudyTerminationConclusion(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

        cleaned_data = {'readmission_after_initial_discharge': YES,
                        'date_readmission': get_utcnow}
        form = StudyTerminationConclusion(cleaned_data=cleaned_data)
        self.assertTrue(form.clean())

        cleaned_data = {'readmission_after_initial_discharge': NO,
                        'date_readmission': None}
        form = StudyTerminationConclusion(cleaned_data=cleaned_data)
        self.assertTrue(form.clean())

        cleaned_data = {'readmission_after_initial_discharge': NO,
                        'date_readmission': get_utcnow}
        form = StudyTerminationConclusion(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_termination_reason_require_consent_withdrawal_reason(self):
        """ Asserts consent_withdrawal_reason when termination reason
            is withdrawal_of_subject_consent.
        """
        cleaned_data = {'termination_reason': 'withdrawal_of_subject_consent',
                        'consent_withdrawal_reason': None}
        form = StudyTerminationConclusion(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

        cleaned_data = {'termination_reason': 'withdrawal_of_subject_consent',
                        'consent_withdrawal_reason': 'reason is given'}
        form = StudyTerminationConclusion(cleaned_data=cleaned_data)
        self.assertTrue(form.clean())

        cleaned_data = {'termination_reason': '10_weeks_completed_followUp',
                        'consent_withdrawal_reason': None}
        form = StudyTerminationConclusion(cleaned_data=cleaned_data)
        self.assertTrue(form.clean())

        cleaned_data = {'termination_reason': '10_weeks_completed_followUp',
                        'consent_withdrawal_reason': 'reason is given'}
        form = StudyTerminationConclusion(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)
