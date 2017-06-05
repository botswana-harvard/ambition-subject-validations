from django import forms

from ..models import LumbarPunctureCsf
from .form_mixins import SubjectModelFormMixin
from edc_constants.constants import YES


class LumbarPunctureCSFForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()

        self.required_if(YES, field='csf_culture',
                         field_required='other_csf_culture')

        if (cleaned_data.get('csf_wbc_cell_count') > 0
                and cleaned_data.get('csf_wbc_cell_count') < 3):
            raise forms.ValidationError({
                'csf_wbc_cell_count':
                'If the count is less than 2, a record of 0 is expected.'})

        self.not_required_if(0, field='csf_wbc_cell_count',
                             field_required='differential_lymphocyte_count')

        self.not_required_if(0, field='csf_wbc_cell_count',
                             field_required='differential_neutrophil_count')

    class Meta:
        model = LumbarPunctureCsf
        fields = '__all__'
