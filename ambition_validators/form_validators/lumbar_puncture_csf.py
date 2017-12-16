from django import forms
from django.conf import settings
from edc_constants.constants import YES, NOT_DONE
from edc_form_validators import FormValidator
from edc_form_validators import REQUIRED_ERROR


class LumbarPunctureCsfFormValidator(FormValidator):

    def clean(self):

        self.validate_opening_closing_pressure()

        self.required_if(
            YES,
            field='csf_culture',
            field_required='other_csf_culture')

        try:
            if 0 < self.cleaned_data.get('csf_wbc_cell_count') < 3:
                raise forms.ValidationError({
                    'csf_wbc_cell_count':
                    'If the count is less than "2", a record of "0" is expected.'})
        except TypeError:
            pass

        # differential_lymphocyte_count
        self.require_together(
            field='csf_wbc_cell_count',
            field_required='differential_lymphocyte_count')

        self.require_together(
            field='differential_lymphocyte_count',
            field_required='differential_lymphocyte_unit')

        self.validate_percentage(
            field='differential_lymphocyte_count',
            unit='differential_lymphocyte_unit')

        # differential_neutrophil_count
        self.require_together(
            field='csf_wbc_cell_count',
            field_required='differential_neutrophil_count')

        self.require_together(
            field='differential_neutrophil_count',
            field_required='differential_neutrophil_unit')

        self.validate_percentage(
            field='differential_neutrophil_count',
            unit='differential_neutrophil_unit')

        # csf_glucose
        self.require_together(
            field='csf_glucose',
            field_required='csf_glucose_units')

        # csf_cr_ag
        self.not_required_if(
            NOT_DONE, field='csf_cr_ag',
            field_required='csf_cr_ag_lfa')

        # csf_cr_ag and india_ink
        if (self.cleaned_data.get('csf_cr_ag') == NOT_DONE
                and self.cleaned_data.get('india_ink') == NOT_DONE):
            error_msg = 'CSF CrAg and India Ink cannot both be "not done".'
            message = {'csf_cr_ag': error_msg, 'india_ink': error_msg}
            raise forms.ValidationError(message, code=REQUIRED_ERROR)

        condition = settings.COUNTRY == 'botswana' or settings.COUNTRY == 'malawi'
        self.applicable_if_true(
            condition=condition, field_applicable='bios_crag')

        self.applicable_if(
            YES,
            field='bios_crag',
            field_applicable='crag_control_result')

        self.applicable_if(
            YES,
            field='bios_crag',
            field_applicable='crag_t1_result')

        self.applicable_if(
            YES,
            field='bios_crag',
            field_applicable='crag_t2_result')

    def validate_percentage(self, field=None, unit=None):
        if self.cleaned_data.get(field):
            if self.cleaned_data.get(unit) == '%' and self.cleaned_data.get(field) > 100:
                raise forms.ValidationError({
                    field: 'Cannot be greater than 100%.'})

    def validate_opening_closing_pressure(self):
        opening_pressure = self.cleaned_data.get('opening_pressure')
        closing_pressure = self.cleaned_data.get('closing_pressure')
        try:
            if opening_pressure <= closing_pressure:
                raise forms.ValidationError({
                    'closing_pressure':
                    'Cannot be greater than the opening pressure.'})
        except TypeError:
            pass
