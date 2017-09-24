from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_constants.constants import YES, NO, OTHER, NOT_APPLICABLE

from ..form_validators import MedicalExpensesFormValidator


@tag('me')
class TestPatientHistoryFormValidator(TestCase):

    def test_care_before_hospital_yes(self):
        cleaned_data = {'care_before_hospital': YES,
                        'location_care': NOT_APPLICABLE}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('location_care', form._errors)

    def test_no_care_before_hospital_transport_form_invalid(self):
        cleaned_data = {'care_before_hospital': NO,
                        'transport_form': 'bus'}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('transport_form', form._errors)

    def test_no_care_before_hospital_care_provider_invalid(self):
        cleaned_data = {'care_before_hospital': NO,
                        'care_provider': 'doctor'}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('care_provider', form._errors)

    def test_no_care_before_hospital_paid_treatment_invalid(self):
        cleaned_data = {'care_before_hospital': NO,
                        'paid_treatment': YES}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('paid_treatment', form._errors)

    def test_no_care_before_hospital_medication_bought_invalid(self):
        cleaned_data = {'care_before_hospital': NO,
                        'medication_bought': YES}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('medication_bought', form._errors)

    def test_no_care_before_hospital_other_place_visited_invalid(self):
        cleaned_data = {'care_before_hospital': NO,
                        'other_place_visited': NO}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('other_place_visited', form._errors)

    def test_no_care_before_hospital_transport_cost_invalid(self):
        cleaned_data = {'care_before_hospital': NO,
                        'transport_cost': 3.50}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('transport_cost', form._errors)

    def test_no_care_before_hospital_transport_duration_invalid(self):
        cleaned_data = {'care_before_hospital': NO,
                        'transport_duration': 'blah'}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('transport_duration', form._errors)

    def test_no_care_before_hospital_paid_treatment_amount_invalid(self):
        cleaned_data = {'care_before_hospital': NO,
                        'paid_treatment_amount': NO}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('paid_treatment_amount', form._errors)

    def test_no_care_before_hospital_medication_payment_invalid(self):
        cleaned_data = {'care_before_hospital': NO,
                        'medication_payment': 150.0}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('medication_payment', form._errors)

    def test_care_before_hospital_no(self):
        cleaned_data = {'care_before_hospital': NO,
                        'location_care': 'healthcare'}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('location_care', form._errors)

    def test_care_before_hospital_other(self):
        cleaned_data = {'care_before_hospital': OTHER,
                        'care_before_hospital_other': None}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('care_before_hospital_other', form._errors)

    def test_location_care_other(self):
        cleaned_data = {'location_care': OTHER,
                        'location_care_other': None}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('location_care_other', form._errors)

    def test_med_bought_no(self):
        cleaned_data = {'medication_bought': NO,
                        'medication_payment': 100}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('medication_payment', form._errors)

    def test_med_bought_yes(self):
        cleaned_data = {'medication_bought': YES,
                        'medication_payment': None}
        form = MedicalExpensesFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('medication_payment', form._errors)
