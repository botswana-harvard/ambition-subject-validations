from django.forms import ValidationError

from edc_base.modelform_validators import FormValidator
from edc_constants.constants import NO


class BloodResultFormValidator(FormValidator):

    def clean(self):
        self.required_if(
            NO,
            field='are_results_normal',
            field_required='abnormal_results_in_ae_range')

        creatinine_unit = self.cleaned_data.get('creatinine_unit')

        if ((creatinine_unit == 'umol/L')
                and len(str(self.cleaned_data.get('creatinine')).split('.')) == 2):
            raise ValidationError({
                'creatinine': 'Please provide a whole number for μmol/L units'})
