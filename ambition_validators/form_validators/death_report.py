from django.apps import apps as django_apps
from django.forms import forms
from edc_form_validators import FormValidator, NOT_REQUIRED_ERROR
from edc_constants.constants import OTHER

from ..constants import TUBERCULOSIS


class DeathReportFormValidator(FormValidator):

    subject_consent_model = 'ambition_subject.subjectconsent'

    @property
    def subject_consent_model_cls(self):
        return django_apps.get_model(self.subject_consent_model)

    def clean(self):

        self.study_day('death_datetime')

        self.validate_other_specify(
            field='cause_of_death',
            other_specify_field='cause_of_death_other',
            other_stored_value=OTHER)

        self.required_if(
            TUBERCULOSIS,
            field='cause_of_death',
            field_required='tb_site')

    def study_day(self, field):
        if self.cleaned_data.get(field):
            subject_identifier = self.cleaned_data.get(
                'subject_visit').appointment.subject_identifier
            consent = self.subject_consent_model_cls.objects.get(
                subject_identifier=subject_identifier)

        if self.cleaned_data.get(field):
            death_date = self.cleaned_data.get(field).date()
            study_days = (
                death_date - consent.consent_datetime.date()).days
            if self.cleaned_data.get('study_day'):
                if self.cleaned_data.get('study_day') > study_days:
                    message = {
                        'study_day': f'Randomization date is '
                        f'{consent.consent_datetime.date()}, death on study day should '
                        f'be {study_days} days or less.'}
                self._errors.update(message)
                self._error_codes.append(NOT_REQUIRED_ERROR)
                raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)
