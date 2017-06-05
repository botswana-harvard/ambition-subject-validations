from django import forms
from ..models import Week2, AmphotericinMissedDoses, FluconazoleMissedDoses
from .form_mixins import SubjectModelFormMixin


class Week2Form(SubjectModelFormMixin):

    class Meta:
        model = Week2
        fields = '__all__'


class FluconazoleMissedDosesForm(forms.ModelForm):

    class Meta:
        model = FluconazoleMissedDoses
        fields = '__all__'


class AmphotericinMissedDosesForm(forms.ModelForm):

    class Meta:
        model = AmphotericinMissedDoses
        fields = '__all__'
