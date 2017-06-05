from ..models import MissedVisit
from .form_mixins import SubjectModelFormMixin


class MissedVisitForm(SubjectModelFormMixin):

    class Meta:
        model = MissedVisit
        fields = '__all__'
