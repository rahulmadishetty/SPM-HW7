# test_computeteameffortvelocity.py
import unittest
from unittest.mock import patch
from computeteameffortvelocity import compute_capacity_for_sprint

class TestComputeTeamEffortVelocity(unittest.TestCase):

    @patch('builtins.input', side_effect=['2', '1', '0', '0', '8'])
    def test_happy_path_single_member_full_availability(self, mock_input):
        with patch('builtins.print') as mock_print:
            compute_capacity_for_sprint()
            mock_print.assert_called_with('\nTotal sprint capacity for the team is: 16.00 hours.')

    @patch('builtins.input', side_effect=['2', '1', '0', '0', '7-9'])
    def test_happy_path_single_member_range_availability(self, mock_input):
        with patch('builtins.print') as mock_print:
            compute_capacity_for_sprint()
            mock_print.assert_called_with('\nTotal sprint capacity for the team is: 16.00 hours.')

    @patch('builtins.input', side_effect=['0'])
    def test_negative_sprint_days(self, mock_input):
        with patch('builtins.print') as mock_print:
            compute_capacity_for_sprint()
            mock_print.assert_called_with("Input must be a positive integer representing sprint days.")

    @patch('builtins.input', side_effect=['2', '-1'])
    def test_negative_team_members(self, mock_input):
        with patch('builtins.print') as mock_print:
            compute_capacity_for_sprint()
            mock_print.assert_called_with("Input must be a positive integer representing team members.")

    # Additional tests can be added to cover more cases like handling ValueError, etc.

if __name__ == '__main__':
    unittest.main()
