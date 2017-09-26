from ..constants import HEADACHE, VISUAL_LOSS, WORKING
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

#         self.required_if(
#             YES,
#             field='other_place_visited',
#             field_required='duration_present_condition')

        self.required_if(
            WORKING,
            field='activities_missed',
            field_required='time_off_work')

        self.validate_other_specify(
            field='activities_missed',
            other_specify_field='activities_missed_other',
            other_stored_value=OTHER)

        self.required_if(
            YES,
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

        self.required_if(
            YES,
            field='household_head',
            field_required='elementary_school')

        self.required_if(
            YES,
            field='elementary_school',
            field_required='elementary_attendance_years')

        self.required_if(
            YES,
            field='household_head',
            field_required='higher_education',
        )

        self.required_if(
            YES,
            field='household_head',
            field_required='secondary_school')

        self.required_if(
            YES,
            field='secondary_school',
            field_required='secondary_attendance_years')

        self.required_if(
            YES,
            field='higher_education',
            field_required='higher_attendance_years')

        req_fields = [
            'head_profession',
            'head_education_years',
            'head_education_certificate',
            'head_elementary',
            'head_secondary',
            'head_higher_education'
        ]
        for req_field in req_fields:
            self.required_if(
                NO,
                field='household_head',
                field_required=req_field,
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

# if self.cleaned_data.get('time_off_work') and
# self.cleaned_data.get('time_off_work')

    def only_not_required_if(self, *responses, field=None, field_required=None,
                             cleaned_data=None):

        if (cleaned_data.get(field) in responses
            and ((cleaned_data.get(field_required)
                  and cleaned_data.get(field_required) != NOT_APPLICABLE))):
            message = {
                field_required: 'This field is not required.'}
            self._errors.update(message)
            self._error_codes.append(NOT_REQUIRED_ERROR)
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)

    def total_money_spent(self, he_spend=None, proxy_spend=None,
                          total_spend=None, cleaned_data=None):
        if (cleaned_data.get(he_spend) and
                cleaned_data.get(proxy_spend)):
            if (self.cleaned_data.get(he_spend) + self.cleaned_data.get(
                    proxy_spend)) != self.cleaned_data.get(total_spend):
                raise forms.ValidationError({
                    total_spend:
                    'The amount you spent and the amount someone else'
                    ' spent should equal the total amount spent on your'
                    ' healthcare'
                })
