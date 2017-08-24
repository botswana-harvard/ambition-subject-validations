from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, NO, OTHER

from ..constants import HEADACHE, VISUAL_LOSS, WORKING


class PatientHistoryFormValidator(FormValidator):

    def clean(self):

        self.m2m_other_specify(
            HEADACHE, m2m_field='symptom', field_other='headache_duration', )

        self.m2m_other_specify(
            VISUAL_LOSS, m2m_field='symptom', field_other='visual_loss_duration', )

        self.applicable_if(
            YES,
            field='tb_history',
            field_applicable='tb_site')

        self.applicable_if(
            YES,
            field='tb_treatment',
            field_applicable='taking_rifampicin')

        self.required_if(
            YES,
            field='taking_rifampicin',
            field_required='rifampicin_started_date')

        self.required_if(
            YES,
            field='previous_non_tb_oi',
            field_required='previous_non_tb_oi_name')

        self.required_if(
            YES,
            field='previous_non_tb_oi',
            field_required='previous_non_tb_oi_date')

        self.applicable_if(
            YES,
            field='new_hiv_diagnosis',
            field_applicable='taking_arv')

        self.required_if(
            YES,
            field='taking_arv',
            field_required='arv_date')

        self.applicable_if(
            YES,
            field='taking_arv',
            field_applicable='first_arv_regimen')

        self.validate_other_specify(field='first_arv_regimen')

        self.validate_other_specify(field='second_arv_regimen')

        self.applicable_if(
            YES,
            field='first_arv_regimen',
            field_applicable='first_line_choice')

        self.required_if(
            NO,
            field='taking_arv',
            field_required='patient_adherence')

        self.required_if(
            NO,
            field='patient_adherence',
            field_required='last_dose')

        self.m2m_other_specify(
            'focal_neurologic_deficit',
            m2m_field='neurological',
            field_other='focal_neurologic_deficit')

        self.required_if(
            OTHER,
            field='care_before_hospital',
            field_required='care_before_hospital_other')

        self.required_if(
            YES,
            field='care_before_hospital',
            field_required='location_care')

        self.required_if(
            OTHER,
            field='location_care',
            field_required='location_care_other')

        self.required_if(
            WORKING,
            field='activities_missed',
            field_required='time_off_work')

        self.required_if(
            OTHER,
            field='activities_missed',
            field_required='activities_missed_other')
