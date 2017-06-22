from edc_base.modelform_validators import FormValidator
from edc_constants.constants import NO


class BloodResultFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            NO,
            field='are_results_normal',
            field_required='abnormal_results_in_ae_range')

        return self.cleaned_data
