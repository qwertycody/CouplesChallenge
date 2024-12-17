import unittest
from unittest.mock import patch
import datetime
from execute import get_today_prompt, clean_message, post_to_slack, send_email

class TestFullExecutionReal(unittest.TestCase):
    def setUp(self):
        self.test_month = 1  # January
        self.days_in_month = 31

    def test_full_execution_real_for_single_month(self):
        """
        Full End-to-End Test: Send real Slack and Email messages for all days in a single month.
        """
        for day in range(1, self.days_in_month + 1):
            with patch('execute.datetime') as mock_datetime:
                # Mock today's date
                mock_date = datetime.datetime(2024, self.test_month, day)
                mock_datetime.datetime.now.return_value = mock_date

                try:
                    # Execute the full program logic
                    number, prompt = get_today_prompt()
                    cleaned_message = clean_message(prompt)

                    # Send real Slack message
                    slack_url = post_to_slack(f"Today's Prompt:\n\n{cleaned_message}")
                    print(f"Day {day}: Slack Message Sent - URL: {slack_url}")

                    # Send real email
                    email_body = f"Today's Prompt:\n\n{cleaned_message}\n\nSlack Message Link (Mobile):\n{slack_url}"
                    send_email("Couples Challenge - Today's Prompt", email_body)
                    print(f"Day {day}: Email Sent")

                except Exception as e:
                    self.fail(f"Execution failed on day {day} with error: {e}")

if __name__ == "__main__":
    unittest.main()
