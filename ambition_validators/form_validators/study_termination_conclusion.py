from edc_form_validators import FormValidator
from edc_constants.constants import YES, NOT_APPLICABLE


class StudyTerminationConclusionFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            YES,
            field='discharged_after_initial_admission',
            field_required='initial_discharge_date')

        self.required_if(
            YES,
            field='readmission_after_initial_discharge',
            field_required='readmission_date')

        self.required_if(
            'died',
            field='termination_reason',
            field_required='death_date')

        self.required_if(
            'withdrawal_of_subject_consent',
            field='termination_reason',
            field_required='consent_withdrawal_reason')

        self.applicable_if(
            'withdrawal_of_subject_consent',
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

        self.required_if(
            None,
            field='arvs_switch_date',
            field_required='arvs_delay_reason')
