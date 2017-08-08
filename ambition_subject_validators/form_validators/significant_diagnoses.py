from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER, YES


class SignificantDiagnosesFormValidator(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='other_significant_diagnoses',
            field_required='possible_diagnoses')

        significant_dx_list = [
            'pulmonary_tb', 'extra_pulmonary_tb',
            'kaposi_sarcoma', 'malaria',
            'bacteraemia', 'pneumonia',
            'diarrhoeal_wasting', OTHER]
        possible_diagnoses = self.cleaned_data.get('possible_diagnoses')
        self.required_if_true(
            condition=possible_diagnoses in significant_dx_list,
            field_required='dx_date')

        self.required_if(
            OTHER,
            field='possible_diagnoses',
            field_required='dx_other')
