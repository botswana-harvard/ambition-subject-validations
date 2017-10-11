from ..constants import HEADACHE, VISUAL_LOSS
from django.forms import forms
from edc_base.modelform_validators import FormValidator
from edc_base.modelform_validators.base_form_validator import NOT_REQUIRED_ERROR
from edc_constants.constants import YES, NO, NONE, OTHER, NOT_APPLICABLE


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

        self.m2m_other_specify(
            OTHER,
            m2m_field='previous_non_tb_oi',
            field_other='previous_non_tb_oi_other')

        self.m2m_single_selection_if(
            NONE,
            m2m_field='previous_non_tb_oi'
        )

        self.applicable_if(
            NO,
            field='new_hiv_diagnosis',
            field_applicable='taking_arv')

        self.required_if(
            YES,
            field='taking_arv',
            field_required='arv_date')

        self.validate_other_specify(field='first_arv_regimen')

        self.validate_other_specify(field='second_arv_regimen')

        arv_req_fields = [
            'first_arv_regimen',
            'first_line_choice',
            'patient_adherence',
        ]
        for arv_req_field in arv_req_fields:
            self.applicable_if(
                YES,
                field='taking_arv',
                field_applicable=arv_req_field,
            )

        self.required_if(
            NO,
            field='patient_adherence',
            field_required='last_dose')

        self.required_if(
            NO,
            field='patient_adherence',
            field_required='days_missed')

        self.not_required_if(
            None,
            field='last_viral_load',
            field_required='viral_load_date')

        self.not_required_if(
            None,
            field='viral_load_date',
            field_required='vl_date_estimated')

        self.not_required_if(
            None,
            field='last_cd4',
            field_required='cd4_date')

        self.not_required_if(
            None,
            field='cd4_date',
            field_required='cd4_date_estimated')
#
        self.m2m_other_specify(
            'focal_neurologic_deficit',
            m2m_field='neurological',
            field_other='focal_neurologic_deficit')

        self.m2m_other_specify(
            OTHER,
            m2m_field='neurological',
            field_other='neurological_other')

        self.m2m_other_specify(
            OTHER,
            m2m_field='specify_medications',
            field_other='specify_medications_other')

# if self.cleaned_data.get('time_off_work') and
# self.cleaned_data.get('time_off_work')
