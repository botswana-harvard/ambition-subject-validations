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

        self.required_if(
            OTHER,
            field='care_before_hospital',
            field_required='care_before_hospital_other')

        self.required_if(
            YES,
            field='care_before_hospital',
            field_required='location_care')

        self.required_if(
            OTHER,
            field='location_care',
            field_required='location_care_other')

        self.required_if(
            YES,
            field='medication_bought',
            field_required='medication_payment')

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
