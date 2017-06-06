from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES

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