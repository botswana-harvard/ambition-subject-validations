from ..constants import WORKING
from django.forms import forms
from edc_base.modelform_validators import FormValidator
from edc_base.modelform_validators.base_form_validator import NOT_REQUIRED_ERROR
from edc_constants.constants import YES, NO, NONE, OTHER, NOT_APPLICABLE


class HealthEconomicsQuestionnaireFormValidator(FormValidator):

    def clean(self):

        #         self.required_if(
        #             YES,
        #             field='other_place_visited',
        #             field_required='duration_present_condition')

        self.total_money_spent(cleaned_data=self.cleaned_data)

        self.validate_other_specify(field='care_before_hospital')

        self.required_if(
            WORKING,
            field='activities_missed',
            field_required='time_off_work')

        self.validate_other_specify(
            field='activities_missed',
            other_specify_field='activities_missed_other',
            other_stored_value=OTHER)

        self.required_if(
            YES,
            field='loss_of_earnings',
            field_required='earnings_lost_amount')

        req_fields = [
            'profession',
            'education_years',
            'education_certificate',
        ]
        for req_field in req_fields:
            self.required_if(
                YES,
                field='household_head',
                field_required=req_field,
            )

        self.required_if(
            YES,
            field='household_head',
            field_required='elementary_school')

        self.required_if(
            YES,
            field='elementary_school',
            field_required='elementary_attendance_years')

        self.required_if(
            YES,
            field='household_head',
            field_required='higher_education',
        )

        self.required_if(
            YES,
            field='household_head',
            field_required='secondary_school')

        self.required_if(
            YES,
            field='secondary_school',
            field_required='secondary_attendance_years')

        self.required_if(
            YES,
            field='higher_education',
            field_required='higher_attendance_years')

        req_fields = [
            'head_profession',
            'head_education_years',
            'head_education_certificate',
            'head_elementary',
            'head_secondary',
            'head_higher_education'
        ]
        for req_field in req_fields:
            self.required_if(
                NO,
                field='household_head',
                field_required=req_field,
            )

        self.required_if(
            YES,
            field='head_elementary',
            field_required='head_attendance_years')

        self.required_if(
            YES,
            field='head_secondary',
            field_required='head_secondary_years')

        self.required_if(
            YES,
            field='head_higher_education',
            field_required='head_higher_years')

    def total_money_spent(self, cleaned_data=None):
        if (cleaned_data.get('personal_he_spend') and
                cleaned_data.get('proxy_he_spend')):
            if (self.cleaned_data.get('personal_he_spend') + self.cleaned_data.get(
                    'proxy_he_spend')) != self.cleaned_data.get('he_spend_last_4weeks'):
                raise forms.ValidationError({
                    'he_spend_last_4weeks':
                    'The amount you spent and the amount someone else'
                    ' spent should equal the total amount spent on your'
                    ' healthcare'
                })
