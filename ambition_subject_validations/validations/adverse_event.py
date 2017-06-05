from edc_base.modelform_mixins import RequiredFieldValidationMixin
from edc_constants.constants import YES, NO, UNKNOWN


class AdverseEvent(RequiredFieldValidationMixin):

    def __init__(self, cleaned_data=None):
        self.cleaned_data = cleaned_data

    def clean(self):
        self.required_if(
            YES,
            field='ae_cause',
            field_required='ae_cause_other',
            cleaned_data=self.cleaned_data)

        self.required_if_true(
            condition=(self.cleaned_data.get(
                'ae_study_relation_possibility') in [NO, UNKNOWN]),
            field_required='possiblity_detail',
            cleaned_data=self.cleaned_data,)

        self.required_if(
            YES,
            field='ae_study_relation_possibility',
            field_required='ambisome_relation',
            cleaned_data=self.cleaned_data,)

        self.required_if(
            YES,
            field='ae_study_relation_possibility',
            field_required='fluconazole_relation',
            cleaned_data=self.cleaned_data,)

        self.required_if(
            YES,
            field='ae_study_relation_possibility',
            field_required='amphotericin_b_relation',
            cleaned_data=self.cleaned_data,)
        return self.cleaned_data
