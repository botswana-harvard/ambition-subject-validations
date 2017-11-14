from ..constants import WORKING
from django.forms import forms
from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, OTHER


class HealthEconomicsQuestionnaireFormValidator(FormValidator):

    def clean(self):

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

    def total_money_spent(self, cleaned_data=None):

        personal_he = cleaned_data.get('personal_he_spend')
        proxy_he = cleaned_data.get('personal_he_spend')
        he_spend_4_weeks = self.cleaned_data.get('he_spend_last_4weeks')
        if not personal_he:
            personal_he = 0
        if not proxy_he:
            proxy_he = 0
        if not he_spend_4_weeks:
            he_spend_4_weeks = 0

        if (personal_he + proxy_he) != he_spend_4_weeks:
            raise forms.ValidationError({
                'he_spend_last_4weeks':
                'The amount you spent and the amount someone else'
                ' spent should equal the total amount spent on your'
                ' healthcare'
            })
