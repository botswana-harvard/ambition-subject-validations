from django import forms
from django.test import TestCase

from edc_constants.constants import OTHER
from edc_base.modelform_validators import REQUIRED_ERROR

from ..form_validators import SubjectVisitFormValidator


class TestSubjectVisitFormValidator(TestCase):

    def test_reason_unscheduled_other(self):
        options = {
            'reason_unscheduled': OTHER,
            'reason_unscheduled_other': None}
        form_validator = SubjectVisitFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('reason_unscheduled_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)
