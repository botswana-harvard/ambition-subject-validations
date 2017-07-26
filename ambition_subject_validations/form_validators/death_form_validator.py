from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER


class DeathFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            OTHER,
            field='cause_of_death_study_doctor_opinion',
            field_required='cause_other_study_doctor_opinion')

        field_list = ['cause_of_death_study_doctor_opinion',
                      'cause_of_death_tmg1_opinion',
                      'cause_of_death_tmg2_opinion']
        field_required_list = ['cause_tb_study_doctor_opinion',
                               'cause_tb_tmg1_opinion',
                               'cause_tb_tmg2_opinion']

        for field, field_required in zip(field_list, field_required_list):
            self.required_if(
                'TB',
                field=field,
                field_required=field_required)

        return self.cleaned_data
