from edc_constants.constants import YES, NO
from edc_form_validators import FormValidator


class PkPdCrfFormValidator(FormValidator):

    def clean(self):

        for num in ['one', 'two', 'three', 'four']:
            self.required_if(
                YES,
                field=f'flucytosine_dose_{num}_given',
                field_required=f'flucytosine_dose_{num}_datetime')

            self.required_if(
                NO,
                field=f'flucytosine_dose_{num}_given',
                field_required=f'flucytosine_dose_reason_missed',
                inverse=False)

        self.required_if(
            NO,
            field='flucytosine_dose_1_missed',
            field_required='flucytosine_dose_one_datetime')

        self.required_if(
            NO,
            field='flucytosine_dose_2_missed',
            field_required='flucytosine_dose_two_datetime')

        self.required_if(
            NO,
            field='flucytosine_dose_3_missed',
            field_required='flucytosine_dose_three_datetime')

        self.required_if(
            NO,
            field='flucytosine_dose_4_missed',
            field_required='flucytosine_dose_four_datetime')

        condition = (self.cleaned_data.get('flucytosine_dose_1_missed') == YES or
                     self.cleaned_data.get('flucytosine_dose_2_missed') == YES or
                     self.cleaned_data.get('flucytosine_dose_3_missed') == YES or
                     self.cleaned_data.get('flucytosine_dose_4_missed') == YES)

        self.required_if_true(
            condition=condition,
            field_required='reason_flucytosine_dose_missed')

        self.required_if(
            YES,
            field='fluconazole_dose_given',
            field_required='fluconazole_dose_datetime')

        self.required_if(
            NO,
            field='fluconazole_dose_given',
            field_required='fluconazole_dose_reason_missed')

        self.required_if(
            YES,
            field='blood_sample_missed',
            field_required='blood_sample_reason_missed',
            inverse=False)

        self.required_if(
            NO,
            field='pre_dose_lp',
            field_required='post_dose_lp')
