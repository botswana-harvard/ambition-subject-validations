from django.db import models
from edc_base.model_mixins import ListModelMixin, BaseUuidModel
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO


class ListModel(ListModelMixin, BaseUuidModel):
    pass


class Appointment(BaseUuidModel):

    visit_code_sequence = models.IntegerField(
        verbose_name=('Sequence'),
        default=0,
        null=True,
        blank=True)


class PatientHistory(BaseUuidModel):

    previous_oi = models.CharField(
        verbose_name='Previous opportunistic infection other than TB?',
        max_length=5,
        choices=YES_NO)


class SubjectScreening(BaseUuidModel):

    screening_identifier = models.CharField(max_length=25, unique=True)

    report_datetime = models.DateTimeField(
        default=get_utcnow)

    mental_status = models.CharField(
        max_length=10)

    age_in_years = models.IntegerField()
