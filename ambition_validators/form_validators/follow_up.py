from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, NO, OTHER

from ..constants import WORKING


class FollowUpFormValidator(FormValidator):

    def clean(self):
        self.required_if(
            NO,
            field='fluconazole_dose',
            field_required='other_fluconazole_dose_reason')
        self.required_if(
            YES,
            field='other_fluconazole_dose',
            field_required='other_fluconazole_dose_reason')
        self.required_if(
            YES,
            field='rifampicin_started',
            field_required='rifampicin_start_date')

        self.validate_other_specify(field='care_before_hospital')

        self.applicable_if(
            YES,
            field='care_before_hospital',
            field_applicable='location_care')

        self.validate_other_specify(field='location_care')

        self.validate_other_specify(field='care_provider')

        self.required_if(
            YES,
            field='paid_treatment',
            field_required='paid_treatment_amount')

        self.not_required_if(
            NO,
            field='medication_bought',
            field_required='medication_payment')

        self.required_if(
            YES,
            field='other_place_visited',
            field_required='duration_present_condition')

        self.required_if(
            WORKING,
            field='activities_missed',
            field_required='time_off_work')

        self.required_if(
            OTHER,
            field='activities_missed',
            field_required='activities_missed_other')

        self.not_required_if(
            NO,
            field='loss_of_earnings',
            field_required='earnings_lost_amount')
