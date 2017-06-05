from edc_constants.constants import OTHER, POS, YES

from ..constants import BACTERIA
from ..models import Microbiology

from .form_mixins import SubjectModelFormMixin


class MicrobiologyForm(SubjectModelFormMixin):

    def clean(self):

        self.required_if(
            YES,
            field='urine_culture_performed',
            field_required='urine_culture_results')

        self.required_if(
            POS,
            field='urine_culture_results',
            field_required='urine_culture_organism')

        self.required_if(
            OTHER,
            field='urine_culture_organism',
            field_required='urine_culture_organism_other')

        self.required_if(
            YES,
            field='blood_culture_performed',
            field_required='blood_culture_results')

        self.required_if(
            POS,
            field='blood_culture_results',
            field_required='date_blood_taken')

        self.required_if(
            POS,
            field='blood_culture_results',
            field_required='blood_culture_organism')

        self.required_if(
            OTHER,
            field='blood_culture_organism',
            field_required='blood_culture_organism_other')

        self.required_if(
            BACTERIA,
            field='blood_culture_organism',
            field_required='bacteria_identified')

        self.required_if(
            OTHER,
            field='bacteria_identified',
            field_required='bacteria_identified_other')

        self.required_if(
            POS,
            field='sputum_results_culture',
            field_required='sputum_results_positive')

        self.required_if(
            YES,
            field='tissue_biopsy_taken',
            field_required='tissue_biopsy_results')

        self.required_if(
            POS,
            field='tissue_biopsy_results',
            field_required='date_biopsy_taken')

        self.required_if(
            POS,
            field='tissue_biopsy_results',
            field_required='tissue_biopsy_organism')

        self.required_if(
            OTHER,
            field='tissue_biopsy_organism',
            field_required='tissue_biopsy_organism_other')

    class Meta:
        model = Microbiology
        fields = '__all__'
