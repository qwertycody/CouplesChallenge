import os
import datetime
import random
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from twilio.rest import Client
import requests
import html

# Load environment variables
load_dotenv()

# Function to generate today's deterministic number
def get_number_for_today(min_val=1, max_val=30):
    today = datetime.datetime.now()
    day_of_month = today.day
    month = today.month
    year = today.year

    # Seed with year and month for a consistent shuffle within the month
    random.seed(f"{year}-{month}")

    # Generate and shuffle numbers
    numbers = list(range(min_val, max_val + 1))
    random.shuffle(numbers)

    # Cycle through the shuffled list using the day of the month
    index = (day_of_month - 1) % len(numbers)
    return numbers[index]


# Function to retrieve today's prompt from environment variables
def get_today_prompt():
    number = get_number_for_today()
    prompt_key = f"PROMPT_{number}"
    prompt = os.getenv(prompt_key)
    if not prompt:
        raise ValueError(f"Missing environment variable for {prompt_key}")
    return number, prompt

# Function to sanitize Slack message text
def clean_message(text):
    """
    Clean up special characters, escape sequences, and newlines
    to display properly in Slack.
    """
    # Unescape HTML entities
    cleaned_text = html.unescape(text)

    # Replace escaped single and double quotes
    cleaned_text = cleaned_text.replace("\\'", "'").replace('\\"', '"')

    return cleaned_text

def get_slack_workspace_url(token):
    """
    Retrieve the Slack workspace URL dynamically using the Slack API.
    """
    response = requests.get(
        "https://slack.com/api/team.info",
        headers={"Authorization": f"Bearer {token}"}
    )
    if response.ok and response.json().get("ok"):
        return response.json()["team"]["domain"]  # Returns the workspace domain
    else:
        raise ValueError("Failed to retrieve workspace domain from Slack API")

def post_to_slack(message):
    slack_token = os.getenv("SLACK_TOKEN")
    slack_channel = os.getenv("SLACK_CHANNEL")
    slack_member_ids = os.getenv("SLACK_MEMBER_IDS")  # Comma-delimited member IDs

    if not slack_token or not slack_channel:
        print("Missing Slack credentials. Skipping Slack notification.")
        return "Link not available at this time"

    # Use the provided member IDs or default to @here if not set
    if not slack_member_ids or not slack_member_ids.strip():
        print("No Slack member IDs specified. Defaulting to @here.")
        member_mentions = "@here"
    else:
        # Prepare mentions using provided member IDs
        member_ids = [member_id.strip() for member_id in slack_member_ids.split(",")]
        member_mentions = " ".join([f"<@{member_id}>" for member_id in member_ids])

    # Dynamically retrieve the Slack workspace domain
    try:
        workspace_domain = get_slack_workspace_url(slack_token)
    except ValueError as e:
        print(e)
        return "Link not available at this time"

    cleaned_message = clean_message(message)

    # Add mentions to the message
    final_message = f"{cleaned_message}\n\n{member_mentions}"

    # Send the message to Slack
    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={"Authorization": f"Bearer {slack_token}", "Content-Type": "application/json"},
        json={"channel": slack_channel, "text": final_message},
    )

    if response.ok and response.json().get("ok"):
        ts = response.json().get("ts")  # Timestamp of the posted message
        channel_id = response.json().get("channel")  # Use channel ID returned by Slack API
        formatted_ts = ts.replace('.', '')

        # Construct the thread link for mobile and web
        slack_url = f"https://{workspace_domain}.slack.com/archives/{channel_id}/p{formatted_ts}"

        print("Slack message sent successfully.")

        # Post a thread reply
        thread_message = "Feel free to post your responses here as a reply to this thread!"
        requests.post(
            "https://slack.com/api/chat.postMessage",
            headers={"Authorization": f"Bearer {slack_token}", "Content-Type": "application/json"},
            json={"channel": slack_channel, "text": thread_message, "thread_ts": ts},
        )

        print("Thread reply sent successfully.")
        return slack_url
    else:
        print("Failed to send Slack message.", response.text)
        return "Link not available at this time"

# Function to send an email with the prompt and Slack link
def send_email(subject, body):
    smtp_server = os.getenv("EMAIL_SMTP_SERVER")
    smtp_port = os.getenv("EMAIL_SMTP_PORT")
    username = os.getenv("EMAIL_USERNAME")
    password = os.getenv("EMAIL_PASSWORD")
    recipients = os.getenv("EMAIL_RECIPIENTS", username)  # Use default sender as recipient if not set

    if not all([smtp_server, smtp_port, username, password, recipients]):
        print("Missing email credentials. Skipping email notification.")
        return

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = username
    msg['To'] = recipients

    try:
        with smtplib.SMTP_SSL(smtp_server, int(smtp_port)) as server:
            server.login(username, password)
            server.sendmail(username, recipients.split(","), msg.as_string())
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to send a text message via Twilio
def send_text_via_twilio(message):
    twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_from_number = os.getenv("TWILIO_FROM_NUMBER")
    twilio_to_numbers = os.getenv("TWILIO_TO_NUMBERS")  # Comma-delimited list

    if not all([twilio_account_sid, twilio_auth_token, twilio_from_number, twilio_to_numbers]):
        print("Missing Twilio credentials. Skipping text message notification.")
        return

    try:
        client = Client(twilio_account_sid, twilio_auth_token)
        to_numbers = [number.strip() for number in twilio_to_numbers.split(",")]

        for to_number in to_numbers:
            message_instance = client.messages.create(
                body=message,
                from_=twilio_from_number,
                to=to_number
            )
            print(f"Text message sent successfully to {to_number}: SID {message_instance.sid}")
    except Exception as e:
        print(f"Failed to send text message: {e}")

# Main logic
if __name__ == "__main__":
    try:
        # Retrieve today's prompt
        number, prompt = get_today_prompt()
        
        cleaned_prompt = clean_message(prompt)

        message = f"Garrett Couple's Challenge - Today's Prompt:\n\n{cleaned_prompt}"

        print(message)

        # Send to Slack and get the Slack mobile link
        slack_url = post_to_slack(message)

        # Prepare email body including Slack link
        email_body = f"{message}\n\nSlack Message Link (Mobile):\n{slack_url}"
        print(email_body)

        # Send via email
        send_email("Garrett Couples Challenge - Today's Prompt", email_body)

        # Send via text message using Twilio
        send_text_via_twilio(f"{message}\n\nSlack Link: {slack_url}")

    except Exception as e:
        print(f"An error occurred: {e}")
