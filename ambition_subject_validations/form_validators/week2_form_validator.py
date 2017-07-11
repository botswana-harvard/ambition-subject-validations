from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, OTHER


class Week2FormValidator(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='discharged',
            field_required='discharge_date',
        )

        self.required_if(
            YES,
            field='died',
            field_required='death_date',
        )

        self.required_if(
            YES,
            field='blood_received',
            field_required='units',
        )

        return self.cleaned_data


class SignificantDiagnosesFormValidator(FormValidator):

    def clean(self):
        significant_dx_list = ['pulmonary_tb', 'extra_pulmonary_tb',
                               'kaposi_sarcoma', 'malaria',
                               'bacteraemia', 'pneumonia',
                               'diarrhoeal_wasting', OTHER]

        field = self.cleaned_data.get('possible_diagnoses')

        self.required_if(
            YES,
            field='other_significant_diagnoses',
            field_required='possible_diagnoses',
        )

        self.required_if_true(
            condition=field in significant_dx_list,
            field_required='dx_date',
        )

        self.required_if(
            OTHER,
            field='possible_diagnoses',
            field_required='dx_other',
        )

        return self.cleaned_data
