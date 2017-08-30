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

#         self.applicable_if(
#             NO,
#             field='new_hiv_diagnosis',
#             field_applicable='taking_arv')

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

        arv_not_req_fields = [
            'first_arv_regimen',
            'second_arv_regimen',
            'first_line_choice',
            'patient_adherence',
        ]
        for arv_not_req_field in arv_not_req_fields:
            self.not_required_if(
                NO,
                field='taking_arv',
                field_required=arv_not_req_field,
            )

        self.required_if(
            NO,
            field='patient_adherence',
            field_required='last_dose')

        self.m2m_other_specify(
            'focal_neurologic_deficit',
            m2m_field='neurological',
            field_other='focal_neurologic_deficit')

        self.validate_other_specify(field='care_before_hospital')

        self.applicable_if(
            YES,
            field='care_before_hospital',
            field_applicable='location_care')

        self.validate_other_specify(field='location_care')

        self.validate_other_specify(field='care_provider')

        self.required_if(
            YES,
            field='paid_treatment',
            field_required='paid_treatment_amount')

        self.required_if(
            YES,
            field='other_place_visited',
            field_required='duration_present_condition')

        self.required_if(
            WORKING,
            field='activities_missed',
            field_required='time_off_work')

        self.required_if(
            OTHER,
            field='activities_missed',
            field_required='activities_missed_other')

        self.not_required_if(
            NO,
            field='loss_of_earnings',
            field_required='earnings_lost_amount')

        req_fields = [
            'profession',
            'education_years',
            'education_certificate',
        ]
        for req_field in req_fields:
            self.required_if(
                YES,
                field='household_head',
                field_required=req_field,
            )

        req_fields = [
            'elementary_school',
            'secondary_school',
            'higher_education',
        ]
        for req_field in req_fields:
            self.applicable_if(
                YES,
                field='household_head',
                field_applicable=req_field,
            )

        self.required_if(
            YES,
            field='elementary_school',
            field_required='elementary_attendance_years')

        self.required_if(
            YES,
            field='secondary_school',
            field_required='secondary_attendance_years')

        self.required_if(
            YES,
            field='higher_education',
            field_required='higher_attendance_years')

        not_req_fields = [
            'head_profession',
            'head_education_years',
            'head_education_certificate',
        ]
        for not_req_field in not_req_fields:
            self.required_if(
                NO,
                field='household_head',
                field_required=not_req_field,
            )

        req_fields = [
            'head_elementary',
            'head_secondary',
            'head_higher_education',
        ]
        for req_field in req_fields:
            self.applicable_if(
                NO,
                field='household_head',
                field_applicable=req_field,
            )

        self.required_if(
            YES,
            field='head_elementary',
            field_required='head_attendance_years')

        self.required_if(
            YES,
            field='head_secondary',
            field_required='head_secondary_years')

        self.required_if(
            YES,
            field='head_higher_education',
            field_required='head_higher_years')
