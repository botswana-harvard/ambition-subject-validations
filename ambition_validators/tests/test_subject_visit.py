from django import forms
from django.test import TestCase

from edc_constants.constants import OTHER
from edc_base.modelform_validators import REQUIRED_ERROR
from edc_visit_tracking.constants import MISSED_VISIT, UNSCHEDULED, SCHEDULED

from ..form_validators import SubjectVisitFormValidator
from .models import Appointment


class TestSubjectVisitFormValidator(TestCase):

    def setUp(self):
        self.appointment = Appointment()

    def test_visit_code_reason_valid(self):
        self.appointment.visit_code_sequence = 0

        options = {
            'appointment': self.appointment,
            'reason': UNSCHEDULED}
        form_validator = SubjectVisitFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('reason',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_reason_missed(self):
        options = {
            'reason': MISSED_VISIT,
            'reason_missed': None}
        form_validator = SubjectVisitFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('reason_missed',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_reason_unscheduled(self):
        options = {
            'reason': UNSCHEDULED,
            'reason_unscheduled': None}
        form_validator = SubjectVisitFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('reason_unscheduled',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_reason_unscheduled_other(self):
        options = {
            'reason_unscheduled': OTHER,
            'reason_unscheduled_other': None}
        form_validator = SubjectVisitFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('reason_unscheduled_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_info_source_other(self):
        options = {
            'info_source': OTHER,
            'info_source_other': None}
        form_validator = SubjectVisitFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('info_source_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)
