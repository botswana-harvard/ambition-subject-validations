from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES


class EducationalBackgroundFormValidator(FormValidator):

    def clean(self):

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
