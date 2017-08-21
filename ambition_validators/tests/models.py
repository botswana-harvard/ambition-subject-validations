from django.db import models
from edc_base.model_mixins import ListModelMixin, BaseUuidModel
from edc_base.utils import get_utcnow


class ListModel(ListModelMixin, BaseUuidModel):
    pass


class SubjectScreening(BaseUuidModel):

    screening_identifier = models.CharField(max_length=25, unique=True)

    report_datetime = models.DateTimeField(
        default=get_utcnow)

    age_in_years = models.IntegerField()
