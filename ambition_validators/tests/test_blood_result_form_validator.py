from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_constants.constants import YES, NO, POS, NOT_APPLICABLE
from django.test.utils import override_settings

from ..form_validators import BloodResultFormValidator
from .models import SubjectVisit, SubjectConsent
import uuid


class TestBloodResultFormValidator(TestCase):

    def setUp(self):
        self.subject_consent = SubjectConsent.objects.create(
            subject_identifier='11111111',
            gender='M')
        self.subject_visit = SubjectVisit.objects.create(
            subject_identifier='11111111',
            appointment_id=uuid.uuid4())

        self.cleaned_data = {
            'haemoglobin': 15,
            'alt': 10,
            'creatinine': 100,
            'creatinine_unit': 'umol/L',
            'absolute_neutrophil': 3,
            'sodium': 135,
            'potassium': 4.0,
            'platelets': 450,
            'subject_visit': self.subject_visit,
            'are_results_normal': YES
        }

    def test_haemoglobin_units_invalid_female(self):
        self.subject_consent.gender = 'F'
        self.subject_consent.save()
        self.cleaned_data.update(
            haemoglobin=6.4,
            are_results_normal=YES)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_haemoglobin_units_invalid_male(self):
        self.cleaned_data.update(
            haemoglobin=6.9,
            are_results_normal=YES)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_haemoglobin_units_male_valid(self):
        self.cleaned_data.update(
            haemoglobin=14,
            are_results_normal=YES)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data
        )
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_no_creatinine_mg_invalid(self):
        self.cleaned_data.update(
            creatinine=0.3,
            creatinine_unit='mg/dL',
            are_results_normal=YES)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_no_creatinine_mg_sodium_invalid(self):
        self.cleaned_data.update(
            creatinine=900,
            creatinine_unit='umol/L',
            are_results_normal=YES)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_creatinine_mg_invalid(self):
        self.cleaned_data.update(
            creatinine=2.48,
            creatinine_unit='mg/dL',
            are_results_normal=YES,)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_creatinine_mg(self):

        self.cleaned_data.update(
            creatinine=1.3,
            creatinine_unit='mg/dL',
            are_results_normal=NO,
            abnormal_results_in_ae_range=YES)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_creatinine_umol_invalid(self):
        self.cleaned_data.update(
            creatinine=217,
            creatinine_unit='umol/L',
            are_results_normal=YES)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_creatinine_umol(self):

        self.cleaned_data.update(
            creatinine=100,
            creatinine_unit='mg/dL',
            are_results_normal=NO,
            abnormal_results_in_ae_range=YES)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_magnesium_invalid(self):
        self.cleaned_data.update(
            magnesium=0.01,
            are_results_normal=YES)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_magnesium(self):
        self.cleaned_data.update(
            magnesium=0.35,
            are_results_normal=NO,
            abnormal_results_in_ae_range=YES)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_potassium_invalid(self):
        self.cleaned_data.update(
            potassium=1.0,
            are_results_normal=YES)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_potassium_high(self):

        self.cleaned_data.update(
            potassium=6.8,
            are_results_normal=YES,
            abnormal_results_in_ae_range=NO)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_potassium_low(self):

        self.cleaned_data.update(
            potassium=2.3,
            are_results_normal=YES,
            abnormal_results_in_ae_range=NO)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_sodium_invalid(self):
        self.cleaned_data.update(
            sodium=100,
            are_results_normal=YES)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_sodium_invalid_1(self):
        self.cleaned_data.update(
            sodium=119,
            are_results_normal=NO,
            abnormal_results_in_ae_range=NOT_APPLICABLE)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('abnormal_results_in_ae_range', form_validator._errors)

    def test_sodium_invalid_2(self):
        self.cleaned_data.update(
            sodium=119,
            are_results_normal=NO,
            abnormal_results_in_ae_range=NO)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('abnormal_results_in_ae_range', form_validator._errors)

    def test_sodium(self):

        self.cleaned_data.update(
            sodium=135,
            are_results_normal=NO,
            abnormal_results_in_ae_range=YES
        )
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_alt_invalid(self):
        self.cleaned_data.update(
            alt=201,
            are_results_normal=YES)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_alt(self):

        self.cleaned_data.update(
            alt=10,
            are_results_normal=YES)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_platelets_invalid(self):
        self.cleaned_data.update(
            platelets=50,
            are_results_normal=YES)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_platelets(self):

        self.cleaned_data.update(
            platelets=450,
            are_results_normal=YES)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_absolute_neutrophil_invalid(self):
        self.cleaned_data.update(
            absolute_neutrophil=0.5,
            are_results_normal=YES)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_absolute_neutrophil(self):

        self.cleaned_data.update(
            absolute_neutrophil=4,
            are_results_normal=YES)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_abnormal_results_in_ae_range_invalid(self):
        self.cleaned_data.update(
            sodium=1000,
            are_results_normal=NO,
            abnormal_results_in_ae_range=NO)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('abnormal_results_in_ae_range', form_validator._errors)

    def test_crag_country_botswana_crag_control_result_none(self):
        self.cleaned_data.update(
            absolute_neutrophil=4,
            are_results_normal=YES,
            bios_crag=YES
        )
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('crag_control_result', form_validator._errors)

    def test_crag_country_botswana_crag_t1_result_none(self):
        self.cleaned_data.update(
            absolute_neutrophil=4,
            are_results_normal=YES,
            bios_crag=YES,
            crag_control_result=POS
        )
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('crag_t1_result', form_validator._errors)

    def test_crag_country_botswana_crag_t2_result_none(self):
        self.cleaned_data.update(
            absolute_neutrophil=4,
            are_results_normal=YES,
            bios_crag=YES,
            crag_control_result=POS,
            crag_t1_result=POS)
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('crag_t2_result', form_validator._errors)

    @override_settings(COUNTRY='zimbabwe')
    def test_crag_country_zimbabwe_crag_control_result_yes(self):
        self.cleaned_data.update(
            absolute_neutrophil=4,
            are_results_normal=YES,
            bios_crag=YES
        )
        form_validator = BloodResultFormValidator(
            cleaned_data=self.cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('bios_crag', form_validator._errors)
