from edc_constants.constants import YES

from ..models import SubjectRandomization
from .form_mixins import SubjectModelFormMixin


class SubjectRandomizationForm(SubjectModelFormMixin):

    def clean(self):

        self.required_if(YES, field='already_on_arvs',
                         field_required='arv_start_date')

    class Meta:
        model = SubjectRandomization
        fields = '__all__'
