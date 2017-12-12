from django.forms import forms
from edc_form_validators import FormValidator
from edc_form_validators import NOT_REQUIRED_ERROR
from edc_constants.constants import YES, NO, OTHER, NOT_APPLICABLE

from ..constants import WORKING


class FollowUpFormValidator(FormValidator):

    def clean(self):

        self.validate_other_specify(
            field='fluconazole_dose',
            other_specify_field='fluconazole_dose_other',
            other_stored_value=OTHER)

        self.required_if(
            YES,
            field='rifampicin_started',
            field_required='rifampicin_start_date')

        for field_applicable in ['location_care', 'transport_form',
                                 'care_provider', 'paid_treatment',
                                 'medication_bought', 'other_place_visited']:
            self.not_applicable_if(
                NO,
                field='care_before_hospital',
                field_applicable=field_applicable,
            )

        for field_required in ['transport_cost', 'transport_duration',
                               'paid_treatment_amount', 'medication_payment']:
            self.only_not_required_if(
                NO,
                field='care_before_hospital',
                field_required=field_required,
                cleaned_data=self.cleaned_data
            )

        self.validate_other_specify(field='care_before_hospital')

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

        self.validate_other_specify(
            field='activities_missed',
            other_specify_field='activities_missed_other',
            other_stored_value=OTHER)

        self.not_required_if(
            NO,
            field='loss_of_earnings',
            field_required='earnings_lost_amount')

    def only_not_required_if(self, *responses, field=None, field_required=None,
                             cleaned_data=None):

        if (cleaned_data.get(field) in responses
            and ((cleaned_data.get(field_required)
                  and cleaned_data.get(field_required) != NOT_APPLICABLE))):
            message = {
                field_required: 'This field is not required.'}
            self._errors.update(message)
            self._error_codes.append(NOT_REQUIRED_ERROR)
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)
