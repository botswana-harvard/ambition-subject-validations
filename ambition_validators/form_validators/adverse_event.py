from django.forms import forms

from edc_form_validators import FormValidator
from edc_constants.constants import YES, NO, UNKNOWN


class AdverseEventFormValidator(FormValidator):

    def clean(self):

        #         self.patient_regimen(
        #             cleaned_data=self.cleaned_data)

        single_dose_reg = (
            self.cleaned_data.get('regimen') == 'Single dose'
            and self.cleaned_data.get(
                'ae_study_relation_possibility') == YES
        )

        control_reg = (
            self.cleaned_data.get('regimen') == 'Control'
            and self.cleaned_data.get(
                'ae_study_relation_possibility') == YES
        )

        single_dose_or_control_reg = (
            self.cleaned_data.get('regimen') == 'Control'
            or self.cleaned_data.get('regimen') == 'Single dose'
            and self.cleaned_data.get(
                'ae_study_relation_possibility') == YES
        )

        single_dose_or_control_drugs = [
            'fluconazole_relation', 'flucytosine_relation']

        self.applicable_if_true(
            condition=single_dose_reg,
            field_applicable='ambisome_relation')

        self.applicable_if_true(
            condition=control_reg,
            field_applicable='amphotericin_b_relation')

        for drug in single_dose_or_control_drugs:
            self.applicable_if_true(
                condition=single_dose_or_control_reg,
                field_applicable=drug)

        self.required_if(
            YES,
            field='ae_cause',
            field_required='ae_cause_other')

        self.applicable_if(
            YES,
            field='sae',
            field_applicable='sae_reason')

        self.applicable_if(
            YES,
            field='susar',
            field_applicable='susar_reported')

#     def patient_regimen(self, cleaned_data=None):
#         """Raises an expcetion if the input doesn't match any of the
#         regimen
#         """
#         regimen = ['Single dose', 'Control']
#         if (self.cleaned_data.get('regimen')
#                 and self.cleaned_data.get('regimen') not in regimen):
#             raise forms.ValidationError({
#                 'regimen':
#                     f'the total years of education should be the sum of '
#                     'the years spent in primary/secondary/higher. '
#                     'Expecting {regimen[0]} or {regimen[1]}'
#             })
