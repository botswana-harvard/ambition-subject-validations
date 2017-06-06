from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO, NOT_APPLICABLE
from edc_base.utils import get_utcnow

from ..validations import FollowUpForm


class TestFollowUpValidations(TestCase):
    
    def setUp(self):
        pass
 
    def test_tb_pulmonary_dx_yes_require_tb_pulmonary_dx_date(self):
        """Test if tb_pulmonary_dx is Yes tb_pulmonary_dx_date is required.
        """
        cleaned_data = {'tb_pulmonary_dx': YES,
                        'tb_pulmonary_dx_date': None}
        follow_up = FollowUpForm(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)
         
        cleaned_data = {'tb_pulmonary_dx': YES,
                        'tb_pulmonary_dx_date': get_utcnow()}
        follow_up = FollowUpForm(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())        
          
    def test_tb_pulmonary_dx_no_require_tb_pulmonary_dx_date(self):
        cleaned_data = {'tb_pulmonary_dx': NO,
                        'tb_pulmonary_dx_date': get_utcnow()}
        follow_up = FollowUpForm(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)
          
        cleaned_data = {'tb_pulmonary_dx': NO,
                        'tb_pulmonary_dx_date': None}
        follow_up = FollowUpForm(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())
        
    def test_extra_pulmonary_tb_dx_yes_require_extra_tb_pulmonary_dx_date(self):
        cleaned_data = {'extra_pulmonary_tb_dx': YES,
                        'extra_tb_pulmonary_dx_date': None}
        follow_up = FollowUpForm(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, follow_up.clean)
        
        cleaned_data = {'extra_pulmonary_tb_dx': YES,
                        'extra_tb_pulmonary_dx_date': get_utcnow()}
        follow_up = FollowUpForm(cleaned_data=cleaned_data)
        self.assertTrue(follow_up.clean())
        
#     def test_extra_pulmonary_tb_dx_no_require_extra_tb_pulmonary_dx_date(self):
#         cleaned_data = {'extra_pulmonary_tb_dx': NO,
#                         'extra_tb_pulmonary_dx_date': get_utcnow()}
#         follow_up = FollowUpForm(cleaned_data=cleaned_data)
#         self.assertRaises(ValidationError, follow_up.clean)
#           
#         cleaned_data = {'extra_pulmonary_tb_dx': NO,
#                         'extra_tb_pulmonary_dx_date': None}
#         follow_up = FollowUpForm(cleaned_data=cleaned_data)
#         self.assertTrue(follow_up.clean())
#          
#          
#      
#          
#     
# 
#         
#         
#         
#     