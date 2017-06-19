from dateutil.relativedelta import relativedelta
from django import forms

from edc_base.modelform_validators import FormValidator


class SubjectConsentFormValidator(FormValidator):

    def clean(self):
        cleaned_data = super().clean()
        subject_screening = self.cleaned_data.get('subject_screening')
        if not subject_screening:
            raise forms.ValidationError(
                'Complete the Subject screening form before proceeding.')

        if 'consent_datetime' in self.cleaned_data:
            if not cleaned_data.get('consent_datetime'):
                raise forms.ValidationError(
                    'Please indicate the consent datetime.')
        dob = self.cleaned_data.get('dob')
        dob_age_at_screening = relativedelta(
            subject_screening.report_datetime.date(), dob).years
        if dob_age_at_screening != subject_screening.age_in_years:
            raise forms.ValidationError(
                {'dob': 'The date of birth entered does not match the age at '
                 'screening.'})
        return cleaned_data
