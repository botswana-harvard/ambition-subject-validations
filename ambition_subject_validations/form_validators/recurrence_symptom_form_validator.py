from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER, YES


class RecurrenceSymptomFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            OTHER,
            field='meningitis_symptom',
            field_required='meningitis_symptom_other')

        self.required_if(
            YES,
            field='neurological',
            field_required='focal_neurologic_deficit')

        self.required_if(
            OTHER,
            field='neurological',
            field_required='cn_palsy')

        self.required_if(
            YES,
            field='amb_administered',
            field_required='amb_duration')

        self.required_if(
            YES,
            field='steroids_administered',
            field_required='steroids_duration')

        self.required_if(
            OTHER,
            field='steroids_administered',
            field_required='steroids_choices_other')

        self.required_if(
            OTHER,
            field='antibiotic_treatment',
            field_required='antibiotic_treatment_other')

        self.required_if(
            YES,
            field='on_arvs',
            field_required='arv_date')

        return self.cleaned_data
