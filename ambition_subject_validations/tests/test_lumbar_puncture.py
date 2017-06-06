from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO

from ..validations import LumbarPunctureCSF


class TestLumbarPunctureValidations(TestCase):

    def test_csf_culture_yes(self):
        """
        Assert that the csf culture is yes
        """
        options = {
            'csf_culture': YES}
        form = LumbarPunctureCSF(cleaned_data=options)
        self.assertTrue(form.clean())
        
    def test_csf_culture_no(self):
        options = {
            'csf_culture': NO,
            'other_csf_culture': YES}
        form = LumbarPunctureCSF(cleaned_data=options)
        self.assertRaisesMessage(
            ValidationError, 'This field is not required.')
        
    def test_if_csf_wbc_cell_count_greater_than_zero(self):
        """
        Assert that the csf wbc count greater or equal to 0 and less than 3
        """
        options = {
            'csf_wbc_cell_count': 1}
        form = LumbarPunctureCSF(cleaned_data=options)
        self.assertTrue(form.clean()) 
        
    def test_if_csf_wbc_cell_count_less_than_zero(self):
        """
        Assert that the csf wbc count less than 0
        """
        options = {
            'csf_wbc_cell_count': 0}
        form = LumbarPunctureCSF(cleaned_data=options)
        self.assertRaisesMessage(
            ValidationError, 'This field is not required.')
        
    def test_differential_lymphocyte_count(self):
        """
        Assert that the differential lymphocyte count not required
        """
        options = {
            'csf_wbc_cell_count': 0,
            'differential_lymphocyte_count': None,
            'differential_neutrophil_count': 5}
        form = LumbarPunctureCSF(cleaned_data=options)
        self.assertTrue(form.clean())
        
    def test_differential_lymphocyte_count_greater_than_zero(self):
        """
        Assert that the differential lymphocyte count required
        """
        options = {
            'differential_lymphocyte_count': 4}
        form = LumbarPunctureCSF(cleaned_data=options)
        self.assertRaisesMessage(
            ValidationError, 'This field is required.')
        
    def differential_neutrophil_count(self):
        """
        Assert that the neutrophil count not required
        """
        options = {
            'csf_wbc_cell_count': 0,
            'differential_lymphocyte_count': 4,
            'differential_neutrophil_count': None}
        form = LumbarPunctureCSF(cleaned_data=options)
        self.assertTrue(form.clean())
        
    def test_neutrophil_count_greater_than_zero(self):
        """
        Assert that neutrophil count required
        """
        options = {
            'differential_neutrophil_count': 4}
        form = LumbarPunctureCSF(cleaned_data=options)
        self.assertRaisesMessage(
            ValidationError, 'This field is required.')
        