from edc_form_validators import FormValidator
from edc_constants.constants import OTHER, YES


class RadiologyFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            YES,
            field='cxr_done',
            field_required='cxr_date')

        self.applicable_if(
            YES,
            field='cxr_done',
            field_applicable='cxr_type')

        self.applicable_if(
            'infiltrates',
            field='cxr_type',
            field_applicable='infiltrate_location')

        self.required_if(
            YES,
            field='ct_performed',
            field_required='ct_performed_date')

        self.applicable_if(
            YES,
            field='ct_performed',
            field_applicable='scanned_with_contrast')

        self.applicable_if(
            YES,
            field='ct_performed',
            field_applicable='brain_imaging_reason')

        self.validate_other_specify(
            field='brain_imaging_reason',
            other_specify_field='brain_imaging_reason_other',
            other_stored_value=OTHER)

        self.required_if(
            YES,
            field='ct_performed',
            field_required='are_results_abnormal')

        self.applicable_if(
            YES,
            field='are_results_abnormal',
            field_applicable='abnormal_results_reason')

        self.validate_other_specify(
            field='abnormal_results_reason',
            other_specify_field='abnormal_results_reason_other',
            other_stored_value=OTHER)

        self.required_if(
            'infarcts',
            field='abnormal_results_reason',
            field_required='infarcts_location')
