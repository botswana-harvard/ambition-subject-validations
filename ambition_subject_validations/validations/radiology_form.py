from edc_constants.constants import OTHER, YES

from ..constants import INFILTRATE_LOCATION
from ..models import Radiology
from .form_mixins import SubjectModelFormMixin


class RadiologyForm(SubjectModelFormMixin):

    def clean(self):
        pass

        self.required_if(
            YES,
            field='is_cxr_done',
            field_required='cxr_type')

        self.required_if(
            YES,
            field='is_cxr_done',
            field_required='when_cxr_done')

        self.required_if(
            INFILTRATE_LOCATION,
            field='cxr_type',
            field_required='infiltrate_location')

        self.required_if(
            YES,
            field='is_cxr_done',
            field_required='cxr_description')

        self.required_if(
            YES,
            field='is_ct_performed',
            field_required='is_scanned_with_contrast')

        self.required_if(
            YES,
            field='is_ct_performed',
            field_required='date_ct_performed')

        self.required_if(
            YES,
            field='is_ct_performed',
            field_required='brain_imaging_reason')

        self.required_if(
            OTHER,
            field='brain_imaging_reason',
            field_required='brain_imaging_reason_other')

        self.required_if(
            YES,
            field='is_cxr_done',
            field_required='are_results_abnormal')

        self.required_if(
            YES,
            field='are_results_abnormal',
            field_required='abnormal_results_reason')

        self.required_if(
            OTHER,
            field='abnormal_results_reason',
            field_required='abnormal_results_reason_other')

        self.required_if(
            'infarcts',
            field='abnormal_results_reason',
            field_required='if_infarcts_location')

    class Meta:
        model = Radiology
        fields = '__all__'
