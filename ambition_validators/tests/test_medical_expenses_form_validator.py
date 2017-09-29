from django.db import models
from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_base.model_mixins import BaseUuidModel
from edc_constants.choices import YES_NO
from edc_constants.constants import YES, NO, OTHER, NOT_APPLICABLE

from ..form_validators import MedicalExpensesFormValidator


class PatientHistory(BaseUuidModel):

    care_before_hospital = models.CharField(
        verbose_name='Have you received any treatment or care '
        'for your present condition, before coming to the hospital?',
        max_length=5,
        choices=YES_NO)


class TestPatientHistoryFormValidator(TestCase):

    def setUp(self):
        self.patient_history = PatientHistory()

    def test_care_before_hospital_yes(self):
        self.patient_history.care_before_hospital = YES

        cleaned_data = {'patient_history': self.patient_history,
                        'location_care': NOT_APPLICABLE}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('location_care', form._errors)

    def test_no_care_before_hospital_transport_form_invalid(self):
        self.patient_history.care_before_hospital = YES

        cleaned_data = {'patient_history': self.patient_history,
                        'transport_form': NOT_APPLICABLE}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('transport_form', form._errors)

    def test_no_care_before_hospital_care_provider_invalid(self):
        self.patient_history.care_before_hospital = YES

        cleaned_data = {'patient_history': self.patient_history,
                        'care_provider': NOT_APPLICABLE}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('care_provider', form._errors)

    def test_no_care_before_hospital_paid_treatment_invalid(self):
        self.patient_history.care_before_hospital = YES

        cleaned_data = {'patient_history': self.patient_history,
                        'paid_treatment': NOT_APPLICABLE}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('paid_treatment', form._errors)

    def test_no_care_before_hospital_medication_bought_invalid(self):
        self.patient_history.care_before_hospital = YES

        cleaned_data = {'patient_history': self.patient_history,
                        'medication_bought': NOT_APPLICABLE}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('medication_bought', form._errors)

    def test_no_care_before_hospital_other_place_visited_invalid(self):
        self.patient_history.care_before_hospital = YES

        cleaned_data = {'patient_history': self.patient_history,
                        'other_place_visited': NOT_APPLICABLE}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('other_place_visited', form._errors)

    def test_no_care_before_hospital_transport_cost_invalid(self):
        self.patient_history.care_before_hospital = NO

        cleaned_data = {'patient_history': self.patient_history,
                        'transport_cost': 3.50}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('transport_cost', form._errors)

    def test_no_care_before_hospital_transport_duration_invalid(self):
        self.patient_history.care_before_hospital = NO

        cleaned_data = {'patient_history': self.patient_history,
                        'transport_duration': 'blah'}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('transport_duration', form._errors)

    def test_no_care_before_hospital_paid_treatment_amount_invalid(self):
        self.patient_history.care_before_hospital = NO

        cleaned_data = {'patient_history': self.patient_history,
                        'paid_treatment_amount': NO}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('paid_treatment_amount', form._errors)

    def test_no_care_before_hospital_medication_payment_invalid(self):
        self.patient_history.care_before_hospital = NO

        cleaned_data = {'patient_history': self.patient_history,
                        'medication_payment': 150.0}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('medication_payment', form._errors)

    def test_care_before_hospital_no(self):
        self.patient_history.care_before_hospital = NO

        cleaned_data = {'patient_history': self.patient_history,
                        'location_care': 'healthcare'}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('location_care', form._errors)

    def test_location_care_other(self):
        self.patient_history.care_before_hospital = YES

        cleaned_data = {'patient_history': self.patient_history,
                        'location_care': OTHER,
                        'location_care_other': None}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('location_care_other', form._errors)

    def test_med_bought_no(self):
        self.patient_history.care_before_hospital = YES

        cleaned_data = {'patient_history': self.patient_history,
                        'medication_bought': NO,
                        'medication_payment': 100}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('medication_payment', form._errors)

    def test_med_bought_yes(self):
        self.patient_history.care_before_hospital = YES

        cleaned_data = {'patient_history': self.patient_history,
                        'medication_bought': YES,
                        'medication_payment': None}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('medication_payment', form._errors)
