from edc_form_validators import FormValidator
from edc_constants.constants import YES, NO, UNKNOWN


class AdverseEventFormValidator(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='ae_cause',
            field_required='ae_cause_other')

        self.required_if_true(
            condition=(self.cleaned_data.get(
                'ae_study_relation_possibility') in [NO, UNKNOWN]),
            field_required='possiblity_detail')

        regimen_1_condition = (
            self.cleaned_data.get('regimen') == 'Single Dose' and
            self.cleaned_data.get('ae_study_relation_possibility') == YES)

        regimen_1_condition_control = (
            self.cleaned_data.get('regimen') == 'Control' and
            self.cleaned_data.get('ae_study_relation_possibility') == YES
        )

        self.applicable_if_true(
            condition=regimen_1_condition,
            field_applicable='ambisome_relation')

        self.applicable_if_true(
            condition=regimen_1_condition or regimen_1_condition_control,
            field_applicable='fluconazole_relation')

        regimen_2_condition = (
            self.cleaned_data.get('regimen') == 'Control' and
            self.cleaned_data.get('ae_study_relation_possibility') == YES)

        self.applicable_if_true(
            condition=regimen_2_condition,
            field_applicable='amphotericin_b_relation')

        self.applicable_if(
            YES,
            field='ae_study_relation_possibility',
            field_applicable='flucytosine_relation')

        self.applicable_if(
            YES,
            field='ae_study_relation_possibility',
            field_applicable='fluconazole_relation')

        self.applicable_if(
            YES,
            field='sae',
            field_applicable='sae_reason')

        self.applicable_if(
            YES,
            field='susar',
            field_applicable='susar_reported')
