from edc_base.modelform_mixins import RequiredFieldValidationMixin
from edc_constants.constants import OTHER, YES


class Radiology(RequiredFieldValidationMixin):

    def __init__(self, cleaned_data=None):
        self.cleaned_data = cleaned_data

    def clean(self):

        self.required_if(
            YES,
            field='is_cxr_done',
            field_required='cxr_type',
            cleaned_data=self.cleaned_data)

        self.required_if(
            YES,
            field='is_cxr_done',
            field_required='cxr_date',
            cleaned_data=self.cleaned_data)

        self.required_if(
            'infiltrate_location',
            field='cxr_type',
            field_required='infiltrate_location',
            cleaned_data=self.cleaned_data)

        self.required_if(
            YES,
            field='is_cxr_done',
            field_required='cxr_description',
            cleaned_data=self.cleaned_data)

        self.required_if(
            YES,
            field='is_ct_performed',
            field_required='is_scanned_with_contrast',
            cleaned_data=self.cleaned_data)

        self.required_if(
            YES,
            field='is_ct_performed',
            field_required='date_ct_performed',
            cleaned_data=self.cleaned_data)

        self.required_if(
            YES,
            field='is_ct_performed',
            field_required='brain_imaging_reason',
            cleaned_data=self.cleaned_data)

        self.required_if(
            OTHER,
            field='brain_imaging_reason',
            field_required='brain_imaging_reason_other',
            cleaned_data=self.cleaned_data)

        self.required_if(
            YES,
            field='is_cxr_done',
            field_required='are_results_abnormal',
            cleaned_data=self.cleaned_data)

        self.required_if(
            YES,
            field='are_results_abnormal',
            field_required='abnormal_results_reason',
            cleaned_data=self.cleaned_data)

        self.required_if(
            OTHER,
            field='abnormal_results_reason',
            field_required='abnormal_results_reason_other',
            cleaned_data=self.cleaned_data)

        self.required_if(
            'infarcts',
            field='abnormal_results_reason',
            field_required='if_infarcts_location',
            cleaned_data=self.cleaned_data)
        return self.cleaned_data
