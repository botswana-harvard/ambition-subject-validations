from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, NO


class FollowUpFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            NO,
            field='fluconazole_dose',
            field_required='other_fluconazole_dose_reason',
        )

        self.required_if(
            YES,
            field='other_fluconazole_dose',
            field_required='other_fluconazole_dose_reason',
        )

        self.required_if(
            YES,
            field='rifampicin_started',
            field_required='rifampicin_start_date',
        )

        return self.cleaned_data
