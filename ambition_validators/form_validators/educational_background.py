from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES


class EducationalBackgroundFormValidator(FormValidator):

    def clean(self):

        #         req_fields = [
        #             'head_profession',
        #             'head_education_years',
        #             'head_education_certificate',
        #             'head_elementary',
        #             'head_secondary',
        #             'head_higher_education'
        #         ]
        #         for req_field in req_fields:
        #             self.required_if(
        #                 YES,
        #                 field='household_head',
        #                 field_required=req_field,
        #             )

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
