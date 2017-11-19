from edc_form_validators import FormValidator
from edc_constants.constants import YES, NO


class Week16FormValidator(FormValidator):

    def clean(self):
        self.required_if(
            NO,
            field='patient_alive',
            field_required='death_datetime')

        self.applicable_if(
            YES,
            field='patient_alive',
            field_applicable='activities_help')

        self.applicable_if(
            YES,
            field='patient_alive',
            field_applicable='illness_problems')

        self.required_if(
            YES,
            field='patient_alive',
            field_required='ranking_score')
