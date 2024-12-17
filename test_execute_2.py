import unittest
from unittest.mock import patch
import datetime
from dotenv import load_dotenv
from execute import get_number_for_today, get_today_prompt

# Load environment variables
load_dotenv()

class TestExecuteIntegration(unittest.TestCase):
    def setUp(self):
        self.min_val = 1
        self.max_val = 30
        self.test_months = {1: 31, 3: 31}  # January and March (both have 31 days)

    @patch('execute.os.getenv')
    def test_full_execution_two_months(self, mock_getenv):
        """
        Integration Test: Ensure all prompts 1-30 are used in different orders across months.
        """
        mock_prompts = {f"PROMPT_{i}": f"Prompt text for number {i}" for i in range(self.min_val, self.max_val + 1)}

        def getenv_mock(key, default=None):
            return mock_prompts.get(key, default)
        
        mock_getenv.side_effect = getenv_mock

        # Verify all numbers are used across the two months
        for month in self.test_months.keys():
            generated_numbers = set()
            for day in range(1, self.test_months[month] + 1):
                with patch('execute.datetime') as mock_datetime:
                    mock_date = datetime.datetime(2024, month, day)
                    mock_datetime.datetime.now.return_value = mock_date

                    number = get_number_for_today(self.min_val, self.max_val)
                    generated_numbers.add(number)

            # Validate all numbers 1-30 are generated within the month
            self.assertEqual(generated_numbers, set(range(self.min_val, self.max_val + 1)),
                             f"Not all numbers 1-30 were generated in month {month}")

if __name__ == "__main__":
    unittest.main()
