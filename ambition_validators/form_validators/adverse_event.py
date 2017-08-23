from edc_base.modelform_validators import FormValidator
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
            self.cleaned_data.get('regimen') == 'regimen_1' and
            self.cleaned_data.get('ae_study_relation_possibility') == YES)

        self.applicable_if_true(
            condition=regimen_1_condition,
            field_applicable='ambisome_relation')

        self.applicable_if_true(
            condition=regimen_1_condition,
            field_applicable='fluconazole_relation')

        regimen_2_condition = (
            self.cleaned_data.get('regimen') == 'regimen_2' and
            self.cleaned_data.get('ae_study_relation_possibility') == YES)

        self.applicable_if_true(
            condition=regimen_2_condition,
            field_applicable='amphotericin_b_relation')

        self.applicable_if(
            YES,
            field='ae_study_relation_possibility',
            field_applicable='flucytosine_relation')
