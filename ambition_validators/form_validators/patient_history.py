from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, NO, NONE, OTHER, NOT_APPLICABLE

from ..constants import HEADACHE, VISUAL_LOSS, WORKING
from edc_base.modelform_validators.base_form_validator import NOT_REQUIRED_ERROR
from django.forms import forms


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

#         self.required_if(
#             YES,
#             field='previous_non_tb_oi',
#             field_required='previous_non_tb_oi_date')

#         self.applicable_if(
#             NO,
#             field='new_hiv_diagnosis',
#             field_applicable='taking_arv')

        self.required_if(
            YES,
            field='taking_arv',
            field_required='arv_date')

        self.validate_other_specify(field='first_arv_regimen')

        self.validate_other_specify(field='second_arv_regimen')

        arv_req_fields = [
            'first_arv_regimen',
            'second_arv_regimen',
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

        self.only_required_if(
            'last_viral_load',
            'viral_load_date',
            cleaned_data=self.cleaned_data)

        self.only_required_if(
            'last_viral_load',
            'vl_date_estimated',
            cleaned_data=self.cleaned_data)

        self.only_required_if(
            'last_cd4',
            'cd4_date',
            cleaned_data=self.cleaned_data)

        self.only_required_if(
            'last_cd4',
            'cd4_date_estimated',
            cleaned_data=self.cleaned_data)

        self.m2m_other_specify(
            'focal_neurologic_deficit',
            m2m_field='neurological',
            field_other='focal_neurologic_deficit')

        self.m2m_other_specify(
            OTHER,
            m2m_field='neurological',
            field_other='neurological_other')

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

        self.not_required_if(
            NO,
            field='medication_bought',
            field_required='medication_payment')

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

    def only_required_if(self, field=None, field_required=None, cleaned_data=None):

        if (cleaned_data.get(field) and not cleaned_data.get(field_required)):
            message = {
                field_required: 'This field is required.'}
            self._errors.update(message)
            self._error_codes.append(NOT_REQUIRED_ERROR)
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)
        else:
            if (not cleaned_data.get(field) and cleaned_data.get(field_required)):
                message = {
                    field_required: 'This field is not required.'}
                self._errors.update(message)
                self._error_codes.append(NOT_REQUIRED_ERROR)
                raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)
