from dateutil.relativedelta import relativedelta
from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.test import TestCase
from edc_base.model_mixins import BaseUuidModel
from edc_base.utils import get_utcnow

from ..form_validators import SubjectConsentFormValidator


class SubjectScreening(BaseUuidModel):

    report_datetime = models.DateTimeField(
        default=get_utcnow)

    age_in_years = models.IntegerField()


class TestSubjectConsentForm(TestCase):

    def setUp(self):
        self.subject_screening = SubjectScreening()
        self.subject_screening.age_in_years = 20

    def test_no_subject_screening_invalid(self):
        cleaned_data = {'consent_datetime': None,
                        'dob': (get_utcnow() - relativedelta(years=20)).date()}
        subject_consent = SubjectConsentFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, subject_consent.clean)

        cleaned_data = {'consent_datetime': get_utcnow(),
                        'subject_screening': self.subject_screening,
                        'dob': (get_utcnow() - relativedelta(years=20)).date()}
        subject_consent = SubjectConsentFormValidator(
            cleaned_data=cleaned_data)

        try:
            subject_consent.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_consent_datetime_not_provided_invalid(self):
        cleaned_data = {'consent_datetime': None,
                        'subject_screening': self.subject_screening,
                        'dob': (get_utcnow() - relativedelta(years=20)).date()}
        subject_consent = SubjectConsentFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, subject_consent.clean)

        cleaned_data = {'consent_datetime': get_utcnow(),
                        'subject_screening': self.subject_screening,
                        'dob': (get_utcnow() - relativedelta(years=20)).date()}
        subject_consent = SubjectConsentFormValidator(
            cleaned_data=cleaned_data)

        try:
            subject_consent.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_consent_age_mismatch_with_screening_age_invalid(self):
        cleaned_data = {'consent_datetime': get_utcnow(),
                        'subject_screening': self.subject_screening,
                        'dob': (get_utcnow() - relativedelta(years=18)).date()}
        subject_consent = SubjectConsentFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, subject_consent.clean)

        cleaned_data = {'consent_datetime': get_utcnow(),
                        'subject_screening': self.subject_screening,
                        'dob': (get_utcnow() - relativedelta(years=20)).date()}
        subject_consent = SubjectConsentFormValidator(
            cleaned_data=cleaned_data)

        try:
            subject_consent.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
