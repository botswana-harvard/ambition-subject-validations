from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, OTHER


class Week2FormValidator(FormValidator):

    def clean(self):

        self.required_if(
            YES,
            field='discharged',
            field_required='discharge_date')

        self.required_if(
            YES,
            field='died',
            field_required='death_date')

        self.m2m_other_specify(
            OTHER,
            m2m_field='drug_interventions',
            field_other='drug_interventions_other')

        self.m2m_other_specify(
            OTHER,
            m2m_field='antibiotic',
            field_other='antibiotic_other')

        self.required_if(
            YES,
            field='blood_received',
            field_required='units')
