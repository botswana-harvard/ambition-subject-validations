from django.forms import forms

from edc_form_validators import FormValidator
from edc_constants.constants import YES


class EducationFormValidator(FormValidator):

    def clean(self):

        self.education_years(
            cleaned_data=self.cleaned_data)

        self.required_if(
            YES,
            field='elementary',
            field_required='attendance_years')

        self.required_if(
            YES,
            field='secondary',
            field_required='secondary_years')

        self.required_if(
            YES,
            field='higher_education',
            field_required='higher_years')

    def education_years(self, cleaned_data=None):
        """Raises an expcetion if the total years of education is not
        the sum of the years spent in primary/secondary/higher
        """
        if(self.cleaned_data.get('attendance_years')
           and self.cleaned_data.get('secondary_years')
           and self.cleaned_data.get('higher_years')):
            education_sum = (self.cleaned_data.get('attendance_years')
                             + self.cleaned_data.get('secondary_years')
                             + self.cleaned_data.get('higher_years'))
            if(education_sum != self.cleaned_data.get('education_years')):
                raise forms.ValidationError({
                    'education_years':
                    'the total years of education should be the sum of '
                    'the years spent in primary/secondary/higher.'
                    'Expecting %d' % (education_sum)
                })
