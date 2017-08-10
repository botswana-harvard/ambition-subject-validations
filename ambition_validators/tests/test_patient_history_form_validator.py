from dateutil.relativedelta import relativedelta
from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO, OTHER

from ..form_validators import PatientHistoryFormValidator


# class Neurological(ListModelMixin):
#
#     class Meta:
#         app_label = 'ambition_validators'


class TestPatientHistoryFormValidator(TestCase):

    #     def setUp(self):
    #         self.obj_one = Neurological.objects.create(
    #             id=2, name='focal_neurologic_deficit')
    #
    #         self.obj_two = Neurological.objects.create(id=3, name='blah blah blah')
    #
    #         self.qs = QuerySet(Neurological)

    def test_first_line_choice_yes(self):
        """Assert that the first line choice is within the first_line_arvs
        """
        cleaned_data = {'arv_regimen': 'TDF +3TC/FTC + either EFZ or NVP',
                        'first_line_choice': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_first_line_choice_no(self):
        """Assert that the first line choice is not provided
        """
        cleaned_data = {'arv_regimen': 'AZT + 3-TC + either EFV or NVP or DTG',
                        'first_line_choice': 'DTG'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)

        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

#     def test_if_focal_neurological_deficit_yes(self):
#         """Assert that patient has focal neurological deficit
#         """
#          print('I am here', QuerySet(self.obj_one, self.obj_two))
#
#         cleaned_data = {'neurological': self.qs,
#                         'focal_neurologic_deficit': None}
#         form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
#         self.assertRaises(ValidationError, form.clean)

#     def test_if_focal_neurological_deficit_none(self):
#         cleaned_data = {'neurological': [obj_one, obj_two],
#                         'focal_neurologic_deficit': 'meningismus', }
#         form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
#
#         try:
#             form.clean()
#         except forms.ValidationError as e:
#             self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_med_history_yes_tb_site_none_invalid(self):
        cleaned_data = {'med_history': YES,
                        'tb_site': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_med_history_yes_tb_site_no_valid(self):
        cleaned_data = {'med_history': YES,
                        'tb_site': 'pulmonary'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)

        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_tb_treatment_taking_rifapicin_none_invalid(self):
        cleaned_data = {'tb_treatment': YES,
                        'taking_rifampicin': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_tb_treatment_taking_rifapicin_no_valid(self):
        cleaned_data = {'tb_treatment': YES,
                        'taking_rifampicin': NO}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)

        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_previous_infection_date_none_invalid(self):
        cleaned_data = {'previous_infection': YES,
                        'previous_infection_specify': 'blah',
                        'infection_date': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_previous_infection_date_valid(self):
        cleaned_data = {'previous_infection': YES,
                        'previous_infection_specify': 'blah',
                        'infection_date': get_utcnow() - relativedelta(years=2)}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)

        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_previous_infection_specify_none_invalid(self):
        cleaned_data = {'previous_infection': YES,
                        'previous_infection_specify': None,
                        'infection_date': get_utcnow() - relativedelta(years=2)}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_previous_infection_specify_valid(self):
        cleaned_data = {'previous_infection': YES,
                        'previous_infection_specify': 'blah',
                        'infection_date': get_utcnow() - relativedelta(years=2)}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)

        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_taking_arv_date_none_invalid(self):
        cleaned_data = {'taking_arv': YES,
                        'arv_date': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_taking_arv_date_sepcified_valid(self):
        cleaned_data = {'taking_arv': YES,
                        'arv_date': get_utcnow() - relativedelta(years=2)}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)

        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_arv_regimen_other_none_invalid(self):
        cleaned_data = {'arv_regimen': OTHER,
                        'arv_regimen_other': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_first_line_arvs_other_specified_valid(self):
        cleaned_data = {'arv_regimen': OTHER,
                        'arv_regimen_other': 'blah'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)

        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_patient_adherence_last_dose_none_invalid(self):
        cleaned_data = {'patient_adherence': NO,
                        'last_dose': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_patient_adherence_last_dose_valid(self):
        cleaned_data = {'patient_adherence': NO,
                        'last_dose': 2}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)

        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

#     def test_specify_medications_other_none_invalid(self):
#         cleaned_data = {'specify_medications_other': OTHER,
#                         'specify_medications': None}
#         form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
#         self.assertRaises(ValidationError, form.clean)
#
#     def test_specify_medications_other_valid(self):
#         cleaned_data = {'specify_medications_other': OTHER,
#                         'specify_medications': 'blah'}
#         form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
#
#         try:
#             form.clean()
#         except forms.ValidationError as e:
#             self.fail(f'ValidationError unexpectedly raised. Got{e}')
