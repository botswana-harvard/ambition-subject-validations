from django.core.exceptions import ValidationError
from django.test import TestCase
  
from edc_constants.constants import YES, NO
  
from ..form_validators import PatientHistoryFormValidator
from edc_base.utils import get_utcnow
  
  
class TestPatientHistoryFormValidator(TestCase):
  
    def test_first_line_choice_yes(self):
        """Assert that the first line choice is within the first_line_arvs
        """
        cleaned_data = {'first_line_arvs': 'AZT',
                   'first_line_choice': 'EFV'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)
  
    def test_first_line_choice_no(self):
        """Assert that the first line choice is not provided
        """
        cleaned_data = {'first_line_arvs': 'AZT + 3-TC + either EFV or NVP or DTG',
                   'first_line_choice': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)
  
    def test_if_focal_neurological_deficit_yes(self):
        """Assert that patient has focal neurological deficit
        """
        cleaned_data = {'neurological': YES, 'focal_neurologic_deficit': 'meningismus',
                   'first_line_choice': 'EFV'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)
  
    def test_if_focal_neurological_deficit_none(self):
        cleaned_data = {'first_line_arvs': 'AZT + 3-TC + either EFV or NVP or DTG',
                   'focal_neurologic_deficit': None,
                   'first_line_choice': None}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)
        
    def test_if_taking_tb_treatment_yes(self):
        cleaned_data = {'tb_treatment': YES, 'taking_rifampicin': YES, 'first_line_choice': 'EFV'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)    
        
    def test_if_taking_tb_treatment_no(self):
        cleaned_data = {'tb_treatment': NO, 'taking_rifampicin': YES,
                   'first_line_choice': 'EFV'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean) 
        
    def test_if_taking_rifampicin_yes(self):
        cleaned_data = {'taking_rifampicin': YES, 'rifampicin_started_date': get_utcnow().date(),
                        'first_line_choice': 'EFV'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean) 
        
    def test_if_taking_rifampicin_no(self):
        cleaned_data = {'taking_rifampicin': NO, 'rifampicin_started_date': get_utcnow().date(),
                        'first_line_choice': 'EFV'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)  
        
    def test_if_participant_previously_infected_yes(self):
        cleaned_data = {'previous_infection': YES, 'infection_date': get_utcnow().date(),
                        'first_line_choice': 'EFV'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean) 
    
    def test_if_participant_previously_infected_no(self):
        cleaned_data = {'previous_infection': NO, 'infection_date': get_utcnow().date(),
                        'first_line_choice': 'EFV'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean) 
        
    def test_if_participant_previous_infection_given_yes(self):
        """ Assert if the participant previous infection specified.
        """
        cleaned_data = {'previous_infection': YES, 'previous_infection_specify': 'pulmonary',
                        'first_line_choice': 'EFV'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)
        
    def test_if_participant_previous_infection_given_no(self):
        """ Assert if the participant previous infection not given / required.
        """
        cleaned_data = {'previous_infection': YES, 'previous_infection_specify': None,
                        'first_line_choice': 'EFV'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)
        
    def test_if_taking_arv_yes(self):
        cleaned_data = {'taking_arv': YES, 'arv_date': get_utcnow().date(),
                        'first_line_choice': 'EFV'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)  
        
    def test_if_taking_arv_no(self):
        cleaned_data = {'taking_arv': NO, 'arv_date': get_utcnow().date(),
                        'first_line_choice': 'EFV'}
        form = PatientHistoryFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean) 
