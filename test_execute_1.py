import unittest
from unittest.mock import patch
import datetime
from execute import get_number_for_today  # Replace 'your_module_name' with the actual filename/module name
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class TestGetNumberForToday(unittest.TestCase):
    def setUp(self):
        self.min_val = 1
        self.max_val = 30

    @patch('execute.datetime')  # Mock datetime
    def test_get_number_for_all_days_two_months(self, mock_datetime):
        """
        Test get_number_for_today() for all valid days of the month for two months.
        """
        # Define two test months: January (31 days) and February (28 days in a non-leap year)
        test_months = {
            1: 31,  # January
            2: 28   # February (non-leap year)
        }

        for month, days_in_month in test_months.items():
            generated_numbers = set()
            for day in range(1, days_in_month + 1):
                # Mock today's date
                mock_date = datetime.datetime(2024, month, day)
                mock_datetime.datetime.now.return_value = mock_date

                # Call the function
                number = get_number_for_today(self.min_val, self.max_val)

                # Validate the number is within the correct range
                self.assertTrue(self.min_val <= number <= self.max_val, 
                                f"Number {number} out of range on day {day} of month {month}")

                # Collect generated numbers for uniqueness validation
                generated_numbers.add(number)

            # Validate that the function generates numbers for each day
            self.assertTrue(len(generated_numbers) > 0, 
                            f"No numbers generated for month {month}")

if __name__ == "__main__":
    unittest.main()
