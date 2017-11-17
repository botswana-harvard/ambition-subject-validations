from ..constants import WORKING
from django.forms import forms
from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, OTHER


class MedicalExpensesFormValidator(FormValidator):

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

        if ((cleaned_data.get('personal_he_spend') or 0)
                + (cleaned_data.get('proxy_he_spend') or 0)
                != (self.cleaned_data.get('he_spend_last_4weeks') or 0)):
            raise forms.ValidationError({
                'he_spend_last_4weeks':
                'The amount you spent and the amount someone else'
                ' spent should equal the total amount spent on your'
                ' healthcare'
            })
