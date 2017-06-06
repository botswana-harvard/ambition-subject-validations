from edc_base.modelform_mixins import RequiredFieldValidationMixin
from edc_constants.constants import YES, NO


class FollowUpForm(RequiredFieldValidationMixin):

    def __init__(self, cleaned_data=None):
        self.cleaned_data = cleaned_data

    def clean(self):
        self.required_if(
            YES,
            field='tb_pulmonary_dx',
            field_required='tb_pulmonary_dx_date',
            cleaned_data=self.cleaned_data)

        self.required_if(
            YES,
            field='extra_pulmonary_tb_dx',
            field_required='extra_tb_pulmonary_dx_date',
            cleaned_data=self.cleaned_data)
        
        return self.cleaned_data

# # 
#         self.required_if(
#             YES,
#             field='kaposi_sarcoma_dx',
#             field_required='kaposi_sarcoma_dx_date')
# 
#         self.required_if(
#             YES,
#             field='malaria_dx',
#             field_required='malaria_dx_date')
# 
#         self.required_if(
#             YES,
#             field='bacteraemia_dx',
#             field_required='bacteraemia_dx_date')
# 
#         self.required_if(
#             YES,
#             field='pneumonia_dx',
#             field_required='pneumonia_dx_date')
# 
#         self.required_if(
#             YES,
#             field='diarrhoeal_wasting_dx',
#             field_required='diarrhoeal_wasting_dx_date')
# 
#         self.required_if(
#             YES,
#             field='other_significant_new_diagnosis',
#             field_required='diagnosis_date')
# 
#         self.required_if(
#             YES,
#             field='other_significant_new_diagnosis',
#             field_required='diagnosis_date')
# 
#         self.required_if(
#             NO,
#             field='fluconazole_dose',
#             field_required='other_fluconazole_dose_reason')
# 
#         self.required_if(
#             YES,
#             field='other_fluconazole_dose',
#             field_required='other_fluconazole_dose_reason')
# 
#         self.required_if(
#             YES,
#             field='rifampicin_started',
#             field_required='rifampicin_start_date')

#         return self.cleaned_data
