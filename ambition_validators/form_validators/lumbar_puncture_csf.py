from django import forms
from django.conf import settings
from edc_form_validators import FormValidator
from edc_form_validators import NOT_REQUIRED_ERROR, REQUIRED_ERROR
from edc_constants.constants import NOT_APPLICABLE, YES


class LumbarPunctureCSFFormValidator(FormValidator):

    # TODO: WHAT IS THIS, why not use "required_if"??
    def only_required_if(self, field=None, field_required=None, cleaned_data=None):
        if (cleaned_data.get(field) == 0
            and ((cleaned_data.get(field_required)
                  and cleaned_data.get(field_required) != NOT_APPLICABLE))):
            message = {
                field_required: 'This field is not required.'}
            self._errors.update(message)
            self._error_codes.append(NOT_REQUIRED_ERROR)
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)

    def clean(self):

        self.validate_opening_closing_pressure()

        self.required_if(
            YES,
            field='csf_culture',
            field_required='other_csf_culture')

        if self.cleaned_data.get('csf_wbc_cell_count'):
            if (self.cleaned_data.get('csf_wbc_cell_count') > 0
                    and self.cleaned_data.get('csf_wbc_cell_count') < 3):
                raise forms.ValidationError({
                    'csf_wbc_cell_count':
                    'If the count is less than 2, a record of 0 is expected.'})

        self.only_required_if(
            field='csf_wbc_cell_count',
            field_required='differential_lymphocyte_count',
            cleaned_data=self.cleaned_data)

        if (self.cleaned_data.get('differential_lymphocyte_count') and not
                self.cleaned_data.get('differential_lymphocyte_unit')):
            message = {
                'differential_lymphocyte_unit': 'This field is required'}
            self._errors.update(message)
            self._error_codes.append(REQUIRED_ERROR)
            raise forms.ValidationError(message, code=REQUIRED_ERROR)
        else:
            if (not self.cleaned_data.get('differential_lymphocyte_count') and
                    self.cleaned_data.get('differential_lymphocyte_unit') and
                    self.cleaned_data.get('differential_lymphocyte_unit') != NOT_APPLICABLE):
                message = {
                    'differential_lymphocyte_unit': 'This field is not applicable'}
                self._errors.update(message)
                self._error_codes.append(REQUIRED_ERROR)
                raise forms.ValidationError(message, code=REQUIRED_ERROR)

        self.percentage_limit_validation(
            field='differential_lymphocyte_count',
            unit='differential_lymphocyte_unit')

        self.only_required_if(
            field='csf_wbc_cell_count',
            field_required='differential_neutrophil_count',
            cleaned_data=self.cleaned_data)

        if (self.cleaned_data.get('differential_neutrophil_count') and not
                self.cleaned_data.get('differential_neutrophil_unit')):
            message = {
                'differential_neutrophil_unit': 'This field is required'}
            self._errors.update(message)
            self._error_codes.append(REQUIRED_ERROR)
            raise forms.ValidationError(message, code=REQUIRED_ERROR)
        else:
            if (not self.cleaned_data.get('differential_neutrophil_count') and
                    self.cleaned_data.get('differential_neutrophil_unit')and
                    self.cleaned_data.get('differential_neutrophil_unit') != NOT_APPLICABLE):
                message = {
                    'differential_neutrophil_unit': 'This field is not applicable'}
                self._errors.update(message)
                self._error_codes.append(REQUIRED_ERROR)
                raise forms.ValidationError(message, code=REQUIRED_ERROR)

        self.percentage_limit_validation(
            field='differential_neutrophil_count',
            unit='differential_neutrophil_unit')

        if (self.cleaned_data.get('csf_glucose') and not
                self.cleaned_data.get('csf_glucose_units')):
            message = {'csf_glucose_units': 'This field is required'}
            self._errors.update(message)
            self._error_codes.append(REQUIRED_ERROR)
            raise forms.ValidationError(message, code=REQUIRED_ERROR)

        if (self.cleaned_data.get('csf_cr_ag') == 'not_done'
                and self.cleaned_data.get('india_ink') == 'not_done'):
            message = {'csf_cr_ag': 'CSF CrAg and India Ink cannot both be Not Done.',
                       'india_ink': 'CSF CrAg and India Ink cannot both be Not Done.'}
            self._errors.update(message)
            self._error_codes.append(REQUIRED_ERROR)
            raise forms.ValidationError(message, code=REQUIRED_ERROR)

        self.not_required_if(
            'not_done', field='csf_cr_ag',
            field_required='csf_cr_ag_lfa')

        # TODO: Use site code to validate not country, Gaborone & Blantyre
        condition = settings.COUNTRY == 'botswana' or settings.COUNTRY == 'malawi'
        self.applicable_if_true(
            condition=condition, field_applicable='bios_crag')

        self.required_if(
            YES,
            field='bios_crag',
            field_required='crag_control_result')

        self.required_if(
            YES,
            field='bios_crag',
            field_required='crag_t1_result')

        self.required_if(
            YES,
            field='bios_crag',
            field_required='crag_t2_result')

    def percentage_limit_validation(self, field=None, unit=None):
        if self.cleaned_data.get(field):
            if (self.cleaned_data.get(unit) == '%' and self.cleaned_data.get(field) > 100):
                raise forms.ValidationError({
                    field: 'Percent cannot be greater than 100'})

    def validate_opening_closing_pressure(self):
        if (self.cleaned_data.get('opening_pressure')
                and self.cleaned_data.get('closing_pressure')):
            if (self.cleaned_data.get('opening_pressure')
                    <= self.cleaned_data.get('closing_pressure')):
                raise forms.ValidationError({
                    'closing_pressure':
                    'Closing pressure should be lower than opening pressure'})
