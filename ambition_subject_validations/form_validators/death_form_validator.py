from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, OTHER


class DeathFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            YES,
            field='death_as_inpatient',
            field_required='cause_of_death_study_doctor_opinion')

        self.required_if(
            YES,
            field='cause_of_death_study_doctor_opinion',
            field_required='cause_tb_study_doctor_opinion')

        self.required_if(
            OTHER,
            field='cause_of_death_study_doctor_opinion',
            field_required='cause_other_study_doctor_opinion')

        self.required_if(
            YES,
            field='cause_of_death_study_doctor_opinion',
            field_required='death_narrative')

        return self.cleaned_data
