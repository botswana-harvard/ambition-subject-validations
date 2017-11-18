from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES


class EducationFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            YES,
            field='elementary',
            field_required='attendance_years')

        self.required_if(
            YES,
            field='secondary',
            field_required='secondary_years')

        self.required_if(
            YES,
            field='higher_education',
            field_required='higher_years')
