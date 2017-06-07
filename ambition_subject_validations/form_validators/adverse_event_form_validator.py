from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, NO, UNKNOWN


class AdverseEventFormValidator(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='ae_cause',
            field_required='ae_cause_other',
        )

        self.required_if_true(
            condition=(self.cleaned_data.get(
                'ae_study_relation_possibility') in [NO, UNKNOWN]),
            field_required='possiblity_detail'
        )

        self.required_if(
            YES,
            field='ae_study_relation_possibility',
            field_required='ambisome_relation',
        )

        self.required_if(
            YES,
            field='ae_study_relation_possibility',
            field_required='fluconazole_relation',
        )

        self.required_if(
            YES,
            field='ae_study_relation_possibility',
            field_required='amphotericin_b_relation',
        )
        return self.cleaned_data
