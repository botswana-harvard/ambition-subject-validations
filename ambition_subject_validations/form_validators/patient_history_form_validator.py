from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, NO, OTHER


class PatientHistoryFormValidator(FormValidator):

    def clean(self):
        if self.cleaned_data.get('arv_regimen'):
            first_line = ('EFZ', 'NVP', 'DTG')
            condition = False
            for a in first_line:
                if a in self.cleaned_data.get('arv_regimen'):
                    condition = True

            self.required_if_true(
                condition=condition,
                field_required='first_line_choice')

        self.required_if(
            YES,
            field='med_history',
            field_required='tb_site')

        self.required_if(
            YES,
            field='tb_treatment',
            field_required='taking_rifampicin')

        self.required_if(
            YES,
            field='taking_rifampicin',
            field_required='rifampicin_started_date')

        self.required_if(
            YES,
            field='previous_infection',
            field_required='infection_date')

        self.required_if(
            YES,
            field='previous_infection',
            field_required='previous_infection_specify')

        self.required_if(
            YES,
            field='taking_arv',
            field_required='arv_date')

        self.required_if(
            OTHER,
            field='arv_regimen',
            field_required='arv_regimen_other')

        self.required_if(
            NO,
            field='patient_adherence',
            field_required='last_dose')

        return self.cleaned_data
