from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO

from ..validations import LumbarPunctureCSF


class TestLumbarPunctureValidations(TestCase):

    def test_csf_culture_yes(self):
        options = {
            'csf_culture': YES}
        form = LumbarPunctureCSF(cleaned_data=options)
        self.assertTrue(form.clean())
        
    def test_ae_cause_no(self):
        options = {
            'csf_culture': NO,
            'other_csf_culture': YES}
        form = LumbarPunctureCSF(cleaned_data=options)
        self.assertRaisesMessage(
            ValidationError, 'This field is not required.')
