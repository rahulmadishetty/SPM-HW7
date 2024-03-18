# test_computeteamsvelocity.py
import unittest
from unittest.mock import patch
from computeteamsvelocity import compute_team_velocity

class TestComputeTeamsVelocity(unittest.TestCase):

    @patch('builtins.input', side_effect=['3', '10', '20', '30'])
    def test_positive_case(self, mock_input):
        with patch('builtins.print') as mock_print:
            compute_team_velocity()
            mock_print.assert_called_with("\nAverage team velocity over 3 sprints is: 20.00(Happy Path)")

    @patch('builtins.input', side_effect=['2', '15', '-5'])
    def test_negative_sprint_points(self, mock_input):
        with patch('builtins.print') as mock_print:
            compute_team_velocity()
            mock_print.assert_called_with("Negative values for points are not allowed. Restart the program and input valid data.")

    @patch('builtins.input', side_effect=['0'])
    def test_zero_sprints(self, mock_input):
        with patch('builtins.print') as mock_print:
            compute_team_velocity()
            mock_print.assert_called_with("Please enter a positive integer for the number of sprints.")

    @patch('builtins.input', side_effect=['two', '10', '20'])
    def test_non_numeric_input_for_sprints(self, mock_input):
        with patch('builtins.print') as mock_print:
            compute_team_velocity()
            mock_print.assert_called_with("Please enter valid numerical inputs.")

    @patch('builtins.input', side_effect=['2', 'ten', 'twenty'])
    def test_non_numeric_input_for_points(self, mock_input):
        with patch('builtins.print') as mock_print:
            compute_team_velocity()
            mock_print.assert_called_with("Please enter valid numerical inputs.")

    # Additional tests can be added for other scenarios like extremely large numbers, etc.

if __name__ == '__main__':
    unittest.main()
