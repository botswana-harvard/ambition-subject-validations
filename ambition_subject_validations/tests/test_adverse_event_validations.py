from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO

from .adverse_event_validations import AdverseEvent


class TestAdverseEventValidations(TestCase):

    def test_1(self):
        options = {
            'ae_cause': YES}
        form = AdverseEvent(cleaned_data=options)
        self.assertTrue(form.clean())

    def test_2(self):
        options = {
            'ae_cause': NO,
            'ae_cause_other': YES}
        form = AdverseEvent(cleaned_data=options)
        self.assertRaisesMessage(
            ValidationError, 'This field is not required.')
