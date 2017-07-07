from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO, OTHER

from ..form_validators import DeathFormValidator


class TestDeathFormValidations(TestCase):

    def test_death_inpatient_yes(self):
        cleaned_data = {
            'death_as_inpatient': YES,
            'cause_of_death_study_doctor_opinion': None}
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
            'cause_of_death_study_doctor_opinion': 'TB',
            'cause_tb_study_doctor_opinion': None}
        form = DeathFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_cause_of_death_study_doc_opinion_no(self):
        cleaned_data = {
            'cause_of_death_study_doctor_opinion': 'TB',
            'cause_tb_study_doctor_opinion': 'meningitis'}
        form = DeathFormValidator(cleaned_data=cleaned_data)
        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cause_of_death_study_doc_opinion_other(self):
        cleaned_data = {
            'cause_of_death_study_doctor_opinion': OTHER,
            'cause_other_study_doctor_opinion': None}
        form = DeathFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_cause_of_death_study_doc_opinion_other_no(self):
        cleaned_data = {
            'cause_of_death_study_doctor_opinion': OTHER,
            'cause_other_study_doctor_opinion': 'blah'}
        form = DeathFormValidator(cleaned_data=cleaned_data)
        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cause_of_death_study_doc_opinion_death_narrative_none(self):
        cleaned_data = {
            'cause_of_death_study_doctor_opinion': OTHER,
            'cause_other_study_doctor_opinion': None}
        form = DeathFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_cause_of_death_study_doc_opinion_death_narrative(self):
        cleaned_data = {
            'cause_of_death_study_doctor_opinion': OTHER,
            'cause_other_study_doctor_opinion': 'blah'}
        form = DeathFormValidator(cleaned_data=cleaned_data)
        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cause_of_death_study_doctor_tb_no_site_specified_invalid(self):
        cleaned_data = {
            'cause_of_death_study_doctor_opinion': 'TB',
            'cause_tb_study_doctor_opinion': None}
        form = DeathFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_cause_of_death_study_doctor_tb_site_specified_valid(self):
        cleaned_data = {
            'cause_of_death_study_doctor_opinion': 'TB',
            'cause_tb_study_doctor_opinion': 'meningitis'}
        form = DeathFormValidator(cleaned_data=cleaned_data)
        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cause_of_death_study_tmg1_tb_no_site_specified_invalid(self):
        cleaned_data = {
            'cause_of_death_tmg1_opinion': 'TB',
            'cause_tb_tmg1_opinion': None}
        form = DeathFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_cause_of_death_study_tmg1_tb_site_specified_valid(self):
        cleaned_data = {
            'cause_of_death_tmg1_opinion': 'TB',
            'cause_tb_tmg1_opinion': 'meningitis'}
        form = DeathFormValidator(cleaned_data=cleaned_data)
        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cause_of_death_study_tmg2_tb_no_site_specified_invalid(self):
        cleaned_data = {
            'cause_of_death_tmg2_opinion': 'TB',
            'cause_tb_tmg2_opinion': None}
        form = DeathFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_cause_of_death_study_tmg2_tb_site_specified_valid(self):
        cleaned_data = {
            'cause_of_death_tmg2_opinion': 'TB',
            'cause_tb_tmg2_opinion': 'meningitis'}
        form = DeathFormValidator(cleaned_data=cleaned_data)
        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
