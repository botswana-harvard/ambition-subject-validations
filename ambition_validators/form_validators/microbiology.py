from django.apps import apps as django_apps
from django.forms import forms
from edc_base.modelform_validators import FormValidator, NOT_REQUIRED_ERROR
from edc_constants.constants import POS, YES, OTHER


class MicrobiologyFormValidator(FormValidator):

    subject_consent_model = 'ambition_subject.subjectconsent'

    @property
    def subject_consent_model_cls(self):
        return django_apps.get_model(self.subject_consent_model)

    def clean(self):

        self.required_if(
            YES,
            field='urine_culture_performed',
            field_required='urine_taken_date')

        self.applicable_if(
            YES,
            field='urine_culture_performed',
            field_applicable='urine_culture_results')

        self.applicable_if(
            POS,
            field='urine_culture_results',
            field_applicable='urine_culture_organism')

        self.validate_other_specify(
            field='urine_culture_organism',
            other_specify_field='urine_culture_organism_other',
            other_stored_value=OTHER)

        self.applicable_if(
            YES,
            field='blood_culture_performed',
            field_applicable='blood_culture_results')

        self.required_if(
            YES,
            field='blood_culture_performed',
            field_required='blood_taken_date')

        self.required_if(
            POS,
            field='blood_culture_results',
            field_required='day_blood_taken')

        self.check_sample_study_day('blood_taken_date')

        self.applicable_if(
            POS,
            field='blood_culture_results',
            field_applicable='blood_culture_organism')

        self.validate_other_specify(
            field='blood_culture_organism',
            other_specify_field='blood_culture_organism_other',
            other_stored_value=OTHER)

        self.required_if(
            'bacteria',
            field='blood_culture_organism',
            field_required='bacteria_identified'
        )

        self.required_if(
            'bacteria_and_cryptococcus',
            field='blood_culture_organism',
            field_required='bacteria_identified'
        )

        self.validate_other_specify(
            field='bacteria_identified',
            other_specify_field='bacteria_identified_other',
            other_stored_value=OTHER)

        self.required_if(
            YES,
            field='sputum_afb_performed',
            field_required='sputum_afb_date')

        self.applicable_if(
            YES,
            field='sputum_afb_performed',
            field_applicable='sputum_results_afb')

        self.required_if(
            YES,
            field='sputum_performed',
            field_required='sputum_taken_date')

        self.applicable_if(
            YES,
            field='sputum_performed',
            field_applicable='sputum_results_culture')

        self.required_if(
            POS,
            field='sputum_results_culture',
            field_required='sputum_results_positive')

        self.required_if(
            YES,
            field='sputum_genexpert_performed',
            field_required='sputum_genexpert_date')

        self.required_if(
            POS,
            field='sputum_genexpert_performed',
            field_required='sputum_results_positive')

        self.applicable_if(
            YES,
            field='sputum_genexpert_performed',
            field_applicable='sputum_result_genexpert')

        self.applicable_if(
            YES,
            field='tissue_biopsy_taken',
            field_applicable='tissue_biopsy_results')

        self.required_if(
            YES,
            field='tissue_biopsy_taken',
            field_required='biopsy_date')

        self.required_if(
            POS,
            field='tissue_biopsy_results',
            field_required='day_biopsy_taken')

        self.applicable_if(
            POS,
            field='tissue_biopsy_results',
            field_applicable='tissue_biopsy_organism')

        self.validate_other_specify(
            field='tissue_biopsy_organism',
            other_specify_field='tissue_biopsy_organism_other',
            other_stored_value=OTHER)

    def check_sample_study_day(self, field):
        subject_identifier = self.cleaned_data.get(
            'subject_visit').appointment.subject_identifier
        consent = self.subject_consent_model_cls.objects.get(
            subject_identifier=subject_identifier)

        if self.cleaned_data.get(field):
            blood_taken_date = self.cleaned_data.get(field)
            study_days = (
                blood_taken_date - consent.consent_datetime.date()).days
            if self.cleaned_data.get('day_blood_taken'):
                if self.cleaned_data.get('day_blood_taken') > study_days:
                    message = {
                        'day_blood_taken': f'Randomization date is '
                        f'{consent.consent_datetime.date()}, blood sample study day should '
                        f'be {study_days} days or less.'}
                    self._errors.update(message)
                    self._error_codes.append(NOT_REQUIRED_ERROR)
                    raise forms.ValidationError(
                        message, code=NOT_REQUIRED_ERROR)
