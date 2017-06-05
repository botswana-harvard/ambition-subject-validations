from ..models import Week4
from .form_mixins import SubjectModelFormMixin


class Week4Form(SubjectModelFormMixin):

    class Meta:
        model = Week4
        fields = '__all__'
