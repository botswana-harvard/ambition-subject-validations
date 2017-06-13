
class Death:

    def __init__(self, cleaned_data=None):
        self.cleaned_data = cleaned_data

    def clean(self):

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

        field_list_2 = ['cause_of_death_study_doctor_opinion',
                        'cause_of_death_tmg1_opinion',
                        'cause_of_death_tmg2_opinion']
        field_required_list_2 = ['cause_tb_study_doctor_opinion',
                                 'cause_tb_tmg1_opinion',
                                 'cause_tb_tmg2_opinion']

        for field, field_required in zip(field_list_2, field_required_list_2):
            self.required_if(
                'TB',
                field=field,
                field_required=field_required)
