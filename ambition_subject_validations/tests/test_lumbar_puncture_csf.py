from django.core.exceptions import ValidationError
from django.test import TestCase, tag

from edc_constants.constants import YES, NO

from ..validations.lumbar_puncture_csf import FormCleaner


class TestLumbarPunctureCSF(TestCase):

    def setUp(self):
        self.cleaned_data = {
            'csf_culture': None,
            'other_csf_culture': None,
            'csf_wbc_cell_count': None,
            'differential_lymphocyte_count': None,
            'differential_neutrophil_count': None}

    @tag('1')
    def test_other_csf_culture(self):
        cleaned_data = {'csf_culture': YES}
        for other_csf_culture in [None, 'blahblah']:
            with self.subTest(other_csf_culture=other_csf_culture):
                cleaned_data.update(other_csf_culture=other_csf_culture)
                validation = FormCleaner(cleaned_data=cleaned_data)
                self.assertRaises(ValidationError, validation.clean)
                try:
                    validation.clean()
                except ValidationError as e:
                    self.assertIn('This field is required.', e.messages)

    def test_default(self):
        validation = LumbarPunctureCSF(cleaned_data={})
        validation.clean()

    def test_csf_culture_other(self):

        obj = mommy.prepare_recipe(LumbarPunctureCsf._meta.label_lower,
                                   csf_culture=YES,
                                   other_csf_culture='blahblah')
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = LumbarPunctureCSFForm(data=data)
        self.assertTrue(form.is_valid())

    def test_csf_wbc_cell_count(self):
        obj = mommy.prepare_recipe(LumbarPunctureCsf._meta.label_lower,
                                   csf_wbc_cell_count=2)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = LumbarPunctureCSFForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(LumbarPunctureCsf._meta.label_lower,
                                   csf_wbc_cell_count=0,
                                   differential_lymphocyte_count=None,
                                   differential_neutrophil_count=None)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = LumbarPunctureCSFForm(data=data)
        self.assertTrue(form.is_valid())

    def test_differential_lymphocyte_count(self):
        obj = mommy.prepare_recipe(LumbarPunctureCsf._meta.label_lower,
                                   csf_wbc_cell_count=6,
                                   differential_lymphocyte_count=None,
                                   differential_neutrophil_count=4)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = LumbarPunctureCSFForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(LumbarPunctureCsf._meta.label_lower,
                                   csf_wbc_cell_count=6,
                                   differential_lymphocyte_count=4,
                                   differential_neutrophil_count=4)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = LumbarPunctureCSFForm(data=data)
        self.assertTrue(form.is_valid())

    def test_differential_neutrophil_count(self):
        obj = mommy.prepare_recipe(LumbarPunctureCsf._meta.label_lower,
                                   csf_wbc_cell_count=6,
                                   differential_lymphocyte_count=4,
                                   differential_neutrophil_count=None)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = LumbarPunctureCSFForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(LumbarPunctureCsf._meta.label_lower,
                                   csf_wbc_cell_count=6,
                                   differential_lymphocyte_count=4,
                                   differential_neutrophil_count=4)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = LumbarPunctureCSFForm(data=data)
        self.assertTrue(form.is_valid())
