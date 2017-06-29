from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO

from ..form_validators import DeathFormValidator


class TestDeathFormValidations(TestCase):

    def test_death_inpatient_yes(self):
        cleaned_data = {
            'death_as_inpatient': YES, 'cause_of_death_study_doctor_opinion': None}
        form = DeathFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_death_inpatient_no(self):
        cleaned_data = {
            'death_as_inpatient': NO,
            'cause_of_death_study_doctor_opinion': 'cryptococcal_meningitis'}
        form = DeathFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_cause_of_death_study_doc_opinion_yes(self):
        cleaned_data = {
            'cause_of_death_study_doctor_opinion': YES,
            'cause_tb_study_doctor_opinion': None}
        form = DeathFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_cause_of_death_study_doc_opinion_no(self):
        cleaned_data = {
            'cause_of_death_study_doctor_opinion': NO,
            'cause_tb_study_doctor_opinion': 'bacteraemia'}
        form = DeathFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_cause_of_death_study_doc_opinion_other(self):
        cleaned_data = {
            'cause_of_death_study_doctor_opinion': YES,
            'cause_other_study_doctor_opinion': YES,
            'cause_tb_study_doctor_opinion': None}
        form = DeathFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_cause_of_death_study_doc_opinion_other_no(self):
        cleaned_data = {
            'cause_of_death_study_doctor_opinion': NO,
            'cause_other_study_doctor_opinion': None,
            'cause_tb_study_doctor_opinion': 'bacteraemia'}
        form = DeathFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)
