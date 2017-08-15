from dateutil.relativedelta import relativedelta
from django import forms
from django.apps import apps as django_apps
from edc_base.modelform_validators import FormValidator
from django.core.exceptions import ObjectDoesNotExist


class SubjectConsentFormValidator(FormValidator):

    subject_screening_model = 'ambition_subject.subjectscreening'

    @property
    def subject_screening_model_cls(self):
        return django_apps.get_model(self.subject_screening_model)

    def clean(self):

        if 'consent_datetime' in self.cleaned_data:
            if not self.cleaned_data.get('consent_datetime'):
                raise forms.ValidationError(
                    'Please indicate the consent datetime.')

        screening_identifier = self.cleaned_data.get('screening_identifier')
        try:
            subject_screening = self.subject_screening_model_cls.objects.get(
                screening_identifier=screening_identifier)
        except ObjectDoesNotExist:
            raise forms.ValidationError(
                'Complete the Subject screening form before proceeding.')

        dob = self.cleaned_data.get('dob')
        dob_age_at_screening = relativedelta(
            subject_screening.report_datetime.date(), dob).years
        if dob_age_at_screening != subject_screening.age_in_years:
            raise forms.ValidationError(
                {'dob':
                 'The date of birth entered does not match the age at '
                 f'screening. Expected {subject_screening.age_in_years}. '
                 f'Got {dob_age_at_screening}.'})
