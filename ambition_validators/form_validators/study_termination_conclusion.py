from django import forms
from django.core.exceptions import ObjectDoesNotExist
from edc_constants.constants import YES, NOT_APPLICABLE
from edc_form_validators import FormValidator

from ..constants import CONSENT_WITHDRAWAL, DEAD


class StudyTerminationConclusionFormValidator(FormValidator):

    def __init__(self, patient_history_cls=None, death_report_cls=None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.patient_history_cls = patient_history_cls
        self.death_report_cls = death_report_cls

    def clean(self):
        if self.cleaned_data.get('termination_reason') == DEAD:
            try:
                self.death_report_cls.objects.get(
                    subject_visit__subject_identifier=self.cleaned_data.get(
                        'subject_identifier'))
            except ObjectDoesNotExist:
                raise forms.ValidationError('Cannot complete study termination.'
                                            'Please complete death form first.')

        self.required_if(
            YES,
            field='discharged_after_initial_admission',
            field_required='initial_discharge_date')

        self.applicable_if(
            YES,
            field='discharged_after_initial_admission',
            field_applicable='readmission_after_initial_discharge')

        self.required_if(
            YES,
            field='readmission_after_initial_discharge',
            field_required='readmission_date')

        self.required_if(
            DEAD,
            field='termination_reason',
            field_required='death_date')

        self.required_if(
            CONSENT_WITHDRAWAL,
            field='termination_reason',
            field_required='consent_withdrawal_reason')

        self.applicable_if(
            CONSENT_WITHDRAWAL,
            field='termination_reason',
            field_applicable='willing_to_complete_10w')

        self.applicable_if(
            'care_transferred_to_another_institution',
            field='termination_reason',
            field_applicable='willing_to_complete_centre')

        self.required_if_true(
            condition=(
                self.cleaned_data.get('willing_to_complete_10w') == YES
                or self.cleaned_data.get('willing_to_complete_centre') == YES),
            field_required='willing_to_complete_date')

        self.applicable_if(
            'late_exclusion_criteria_met',
            field='termination_reason',
            field_applicable='protocol_exclusion_criterion')

        self.required_if(
            'included_in_error',
            field='termination_reason',
            field_required='included_in_error')

        self.required_if(
            'included_in_error',
            field='termination_reason',
            field_required='included_in_error_date')

        self.validate_other_specify(field='first_line_regimen')

        self.validate_other_specify(field='second_line_regimen')

        self.not_applicable_if(
            NOT_APPLICABLE,
            field='first_line_regimen',
            field_applicable='first_line_choice')

        self.required_if_true(
            condition=(
                self.patient_history_obj() is not None
                and (self.patient_history_obj().first_arv_regimen == NOT_APPLICABLE
                     and self.cleaned_data.get('first_line_regimen') == NOT_APPLICABLE)),
            field_required='arvs_delay_reason')

    def patient_history_obj(self):

        subject_identifier = self.cleaned_data.get(
            'subject_identifier')
        try:
            patient_history = self.patient_history_cls.objects.get(
                subject_visit__subject_identifier=subject_identifier)
        except ObjectDoesNotExist:
            patient_history = None
        return patient_history
