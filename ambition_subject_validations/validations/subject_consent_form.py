from dateutil.relativedelta import relativedelta
from django import forms


class SubjectConsent:

    def __init__(self, cleaned_data=None):
        self.cleaned_data = cleaned_data

    def clean(self):
        if 'consent_datetime' in self.cleaned_data:
            if not self.cleaned_data.get('consent_datetime'):
                raise forms.ValidationError(
                    'Please indicate the consent datetime.')
        cleaned_data = super().clean()
        self.validate_with_enrollment_checklist()
        return cleaned_data

    def validate_with_enrollment_checklist(self):
        dob = self.cleaned_data.get('dob')
        subject_screening = self.cleaned_data.get(
            'subject_screening')
        try:
            dob_age_at_screening = relativedelta(
                subject_screening.report_datetime.date(), dob).years
            if dob_age_at_screening != subject_screening.age_in_years:
                raise forms.ValidationError(
                    'The date of birth entered does not match the age at '
                    'screening.')
        except subject_screening.DoesNotExist:
            raise forms.ValidationError(
                'Complete the Subject screening form before proceeding.')
