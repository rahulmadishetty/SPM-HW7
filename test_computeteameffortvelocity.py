# test_computeteameffortvelocity.py

import unittest
from unittest.mock import patch
from computeteameffortvelocity import compute_capacity_for_sprint

class TestComputeCapacityForSprint(unittest.TestCase):

    @patch('builtins.input', side_effect=[5, 2, 2, 1, '8', 1, 0, '7-9'])
    @patch('builtins.print')
    def test_normal_operation(self, mock_print, mock_input):
        compute_capacity_for_sprint()
        mock_print.assert_called_with("\nTotal sprint capacity for the team is: 134.00 hours.")

    @patch('builtins.input', side_effect=[0, 1])
    @patch('builtins.print')
    def test_zero_sprint_days(self, mock_print, mock_input):
        compute_capacity_for_sprint()
        mock_print.assert_called_with("Input must be a positive integer representing sprint days.")

    @patch('builtins.input', side_effect=['five', 1])
    @patch('builtins.print')
    def test_invalid_sprint_days(self, mock_print, mock_input):
        compute_capacity_for_sprint()
        mock_print.assert_called_with("Please enter valid numerical inputs. Ensure proper formatting for all entries.")

    @patch('builtins.input', side_effect=[5, -1])
    @patch('builtins.print')
    def test_negative_team_members(self, mock_print, mock_input):
        compute_capacity_for_sprint()
        mock_print.assert_called_with("Input must be a positive integer representing team members.")

    # Additional test cases can be written for other paths as needed.

if __name__ == '__main__':
    unittest.main()
