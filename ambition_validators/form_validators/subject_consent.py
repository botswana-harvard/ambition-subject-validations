from dateutil.relativedelta import relativedelta
from django import forms
from django.apps import apps as django_apps
from edc_base.modelform_validators import FormValidator
from django.core.exceptions import ObjectDoesNotExist


class SubjectConsentFormValidator(FormValidator):

    subject_screening_model = 'ambition_subject.subjectscreening'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dob = self.cleaned_data.get('dob')
        self.consent_datetime = self.cleaned_data.get('consent_datetime')
        self.screening_identifier = self.cleaned_data.get(
            'screening_identifier')

    @property
    def subject_screening_model_cls(self):
        return django_apps.get_model(self.subject_screening_model)

    def clean(self):
        try:
            subject_screening = self.subject_screening_model_cls.objects.get(
                screening_identifier=self.screening_identifier)
        except ObjectDoesNotExist:
            raise forms.ValidationError(
                'Complete the Subject screening form before proceeding.',
                code='missing_subject_screening')

        if not self.consent_datetime:
            raise forms.ValidationError(
                {'consent_datetime': 'This field is required.'})

        screening_age_in_years = relativedelta(
            subject_screening.report_datetime.date(), self.dob).years
        if screening_age_in_years != subject_screening.age_in_years:
            raise forms.ValidationError(
                {'dob':
                 'The date of birth entered does not match the age at '
                 f'screening. Expected {subject_screening.age_in_years}. '
                 f'Got {screening_age_in_years}.'})
