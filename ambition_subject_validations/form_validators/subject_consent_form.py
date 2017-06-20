from dateutil.relativedelta import relativedelta
from django import forms
from edc_base.modelform_validators import FormValidator


class SubjectConsentFormValidator(FormValidator):

    def clean(self):
        if 'consent_datetime' in self.cleaned_data:
            if not self.cleaned_data.get('consent_datetime'):
                raise forms.ValidationError(
                    'Please indicate the consent datetime.')
        self.validate_age_with_screening(self.cleaned_data)
        self.validate_gender_with_screening(self.cleaned_data)

        return self.cleaned_data

    def validate_age_with_screening(self, cleaned_data):
        dob = cleaned_data.get('dob')
        subject_screening = cleaned_data.get(
            'subject_screening')
        try:
            dob_age_at_screening = relativedelta(
                subject_screening.report_datetime.date(), dob).years
            if dob_age_at_screening != subject_screening.age_in_years:
                raise forms.ValidationError(
                    {'dob':
                     'The date of birth entered does not match the age at '
                     'screening.'})
        except subject_screening.DoesNotExist:
            raise forms.ValidationError(
                'Complete the Subject screening form before proceeding.')

    def validate_gender_with_screening(self, cleaned_data):
        subject_screening = cleaned_data.get(
            'subject_screening')
        consent_gender = cleaned_data.get('gender')
        try:
            if subject_screening.gender != cleaned_data.get('gender'):
                raise forms.ValidationError(
                    {'gender':
                     f'Gender mismatch, Screening gender: {subject_screening.gender}, '
                     f'Consent gender: {consent_gender}'})
        except subject_screening.DoesNotExist:
            raise forms.ValidationError(
                'Complete the Subject screening form before proceeding.')
