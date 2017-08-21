from django.forms import ValidationError

from edc_base.modelform_validators import FormValidator
from edc_constants.constants import NO


class BloodResultFormValidator(FormValidator):

    def clean(self):
        self.applicable_if(
            NO,
            field='are_results_normal',
            field_applicable='abnormal_results_in_ae_range')

        creatinine_unit = self.cleaned_data.get('creatinine_unit')
        if ((creatinine_unit == 'umol/L')
                and '.' in str(self.cleaned_data.get('creatinine'))):
            raise ValidationError({
                'creatinine': 'Please provide a whole number for μmol/L units'})
