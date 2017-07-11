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


class FluconazoleMissedDosesFormValidator(FormValidator):

    def clean(self):

        field = self.cleaned_data.get('flucon_day_missed')

        self.required_if_true(
            condition=field in range(1, 15),
            field_required='flucon_missed_reason',
        )

        self.required_if(
            OTHER,
            field='flucon_missed_reason',
            field_required='missed_reason_other',
        )

        return self.cleaned_data


class AmphotericinMissedDosesFormValidator(FormValidator):

    def clean(self):

        field = self.cleaned_data.get('ampho_day_missed')

        self.required_if_true(
            condition=field in range(1, 15),
            field_required='ampho_missed_reason',
        )

        self.required_if(
            OTHER,
            field='ampho_missed_reason',
            field_required='missed_reason_other',
        )

        return self.cleaned_data


class FlucytosineMissedDosesFormValidator(FormValidator):

    def clean(self):

        field = self.cleaned_data.get('flucy_day_missed')

        self.required_if_true(
            condition=field in range(1, 15),
            field_required='flucy_missed_reason',
        )

        self.required_if(
            OTHER,
            field='flucy_missed_reason',
            field_required='missed_reason_other',
        )

        return self.cleaned_data
