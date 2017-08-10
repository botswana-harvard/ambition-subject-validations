from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER, YES


class RecurrenceSymptomFormValidator(FormValidator):

    def clean(self):

        self.m2m_other_specify(
            OTHER,
            m2m_field='meningitis_symptom',
            field_other='meningitis_symptom_other')

        self.required_if(
            YES,
            field='neurological',
            field_required='focal_neurologic_deficit')

        self.m2m_other_specify(
            OTHER,
            m2m_field='neurological',
            field_other='other_cn_palsy_chosen')

        self.required_if(
            YES,
            field='amb_administered',
            field_required='amb_duration')

        self.required_if(
            YES,
            field='steroids_administered',
            field_required='steroids_duration')

        self.required_if(
            YES,
            field='steroids_administered',
            field_required='steroids_choices')

        self.required_if(
            OTHER,
            field='steroids_choices',
            field_required='steroids_choices_other')

        self.m2m_other_specify(
            OTHER,
            m2m_field='antibiotic_treatment',
            field_other='antibiotic_treatment_other')

        self.required_if(
            YES,
            field='on_arvs',
            field_required='arv_date')
