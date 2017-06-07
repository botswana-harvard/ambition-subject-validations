from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES


class StudyTerminationConclusionFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            YES,
            field='discharged_after_initial_admission',
            field_required='date_initial_discharge',
        )

        self.required_if(
            YES,
            field='readmission_after_initial_discharge',
            field_required='date_readmission',
        )

        self.required_if(
            'withdrawal_of_subject_consent',
            field='termination_reason',
            field_required='consent_withdrawal_reason',
        )
#
#         self.required_if(
#             YES,
#             field='rifampicin_started_since_week4',
#             field_required='rifampicin_started_study_day')
#
#         self.required_if(
#             YES,
#             field='willing_to_complete_10W_FU',
#             field_required='date_willing_to_complete')
#
#         self.required_if(
#             YES,
#             field='willing_to_complete_centre',
#             field_required='date_willing_to_complete')
#
#         self.required_if(
#             YES,
#             field='late_protocol_exclusion',
#             field_required='rifampicin_started')
#
#         self.required_if(
#             OTHER,
#             field='first_line_regimen_patients',
#             field_required='first_line_regimen_patients_other')
#
#         self.required_if(
#             OTHER,
#             field='second_line_regimen_patients',
#             field_required='second_line_regimen_patients_other')
#
#         self.required_if(
#             NOT_APPLICABLE,
#             field='date_arvs_started_or_switched',
#             field_required='arvs_delay_reason')

        return self.cleaned_data
