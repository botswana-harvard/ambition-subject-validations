from django import forms

from edc_base.modelform_validators import FormValidator
from edc_base.modelform_validators.base_form_validator import (NOT_REQUIRED_ERROR,
                                                               REQUIRED_ERROR)
from edc_constants.constants import NOT_APPLICABLE, YES


class LumbarPunctureCSFFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            YES, field='csf_culture',
            field_required='other_csf_culture')

        if self.cleaned_data.get('csf_wbc_cell_count'):
            if (self.cleaned_data.get('csf_wbc_cell_count') > 0
                    and self.cleaned_data.get('csf_wbc_cell_count') < 3):
                raise forms.ValidationError({
                    'csf_wbc_cell_count':
                    'If the count is less than 2, a record of 0 is expected.'})

        if (self.cleaned_data.get('csf_cr_ag') == 'not_done'
                and self.cleaned_data.get('india_ink') == 'not_done'):
            message = {'csf_cr_ag': 'CSF CrAg and India Ink cannot both be Not Done.',
                       'india_ink': 'CSF CrAg and India Ink cannot both be Not Done.'}
            self._errors.update(message)
            self._error_codes.append(REQUIRED_ERROR)
            raise forms.ValidationError(message, code=REQUIRED_ERROR)

        self.only_required_if(
            0, field='csf_wbc_cell_count',
            field_required='differential_lymphocyte_count',
            cleaned_data=self.cleaned_data)

        self.only_required_if(
            0, field='csf_wbc_cell_count',
            field_required='differential_neutrophil_count',
            cleaned_data=self.cleaned_data)

        return self.cleaned_data

    def only_required_if(self, *responses, field=None, field_required=None,
                         cleaned_data=None):

        if (cleaned_data.get(field) == 0
            and ((cleaned_data.get(field_required)
                  and cleaned_data.get(field_required) != NOT_APPLICABLE))):
            message = {
                field_required: 'This field is not required.'}
            self._errors.update(message)
            self._error_codes.append(NOT_REQUIRED_ERROR)
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)
