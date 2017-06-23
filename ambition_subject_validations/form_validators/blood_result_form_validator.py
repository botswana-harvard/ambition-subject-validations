from django.forms import ValidationError

from edc_base.modelform_validators import FormValidator
from edc_constants.constants import NO


class BloodResultFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            NO,
            field='are_results_normal',
            field_required='abnormal_results_in_ae_range')

        creatinine_field = 'creatinine'
        creatinine_unit = self.cleaned_data.get('creatinine_unit')

        self.validate_non_decimal_values(field=creatinine_field,
                                         field_unit=creatinine_unit)

        return self.cleaned_data

    def validate_non_decimal_values(self, field=None, field_unit=None):
        if ((field_unit == 'umol/L')
                and len(str(self.cleaned_data.get(field)).split('.')) == 2):
            raise ValidationError({
                field: 'Please provide a whole number for μmol/L units'})
