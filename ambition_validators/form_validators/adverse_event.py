from django.forms import forms

from edc_form_validators import FormValidator
from edc_constants.constants import YES, NO, UNKNOWN


class AdverseEventFormValidator(FormValidator):

    def clean(self):

        #         self.patient_regimen(
        #             cleaned_data=self.cleaned_data)

        drugs = ['ambisome_relation', 'fluconazole_relation',
                 'amphotericin_b_relation', 'flucytosine_relation']

        for drug in drugs:
            self.applicable_if(
                YES,
                field='ae_study_relation_possibility',
                field_applicable=drug
            )

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
