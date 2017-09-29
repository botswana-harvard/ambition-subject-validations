from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER, YES


class SignificantDiagnosesFormValidator(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='other_significant_diagnoses',
            field_required='possible_diagnoses')

        self.not_required_if(
            None,
            field='possible_diagnoses',
            field_required='dx_date')

        self.required_if(
            OTHER,
            field='possible_diagnoses',
            field_required='dx_other')
