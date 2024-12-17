Here’s an **updated version** of your `README.md` that reflects the latest context, improves clarity, and incorporates the deterministic prompt selection, Slack threading, and manual trigger features:

---

# **CouplesChallenge**

## **Overview**
CouplesChallenge is a daily reminder application inspired by the *30-Day Couples Challenge* from [meetthefreemans.com](https://meetthefreemans.com). It helps couples reconnect and strengthen their relationship through quick, actionable prompts delivered consistently every day.

---

## **Purpose**
Modern life is busy, and relationships can easily take a back seat. CouplesChallenge provides daily, meaningful activities to:
- Foster connection and appreciation.
- Improve communication skills.
- Initiate deeper conversations in just **1–5 minutes** per day.

---

## **How It Works**

1. **Daily Prompts**:  
   Each day, a unique prompt is selected from one of the following categories:
   - **Love Deposit**: Small, playful gestures to express love and gratitude.
   - **Communication Tip**: Practical tips to improve listening, understanding, and speaking.
   - **Conversation Starter**: Thoughtful questions to spark meaningful discussions.

2. **Deterministic Logic**:  
   A Python script generates a daily prompt number (1–30) based on:
   - The **month** and **day**, ensuring deterministic but non-repeating outputs within a month.
   - A **reshuffled order** every month to add variety while maintaining predictability.

3. **Automation**:
   - The script runs **daily at 6 AM EST** using **GitHub Actions**.
   - Results are posted to **Slack** and sent via **email** for easy accessibility.

4. **Manual Trigger Support**:  
   The workflow can also be triggered manually for testing or re-runs.

---

## **Features**

### **Daily Automation**
- Prompts are delivered consistently every day using GitHub Actions.
- Ensures reliable execution without manual intervention.

### **Slack Integration**
- The daily prompt is posted to a specified Slack channel.
- A **threaded reply** is added suggesting participants post their responses in the thread, keeping the discussion organized.

### **Email Integration**
- Daily prompts are emailed to recipients, including a link to the Slack thread for engagement.

### **Deterministic Prompt Generation**
- Prompts are:
   - **Non-repeating** within the month.
   - **Varied** every month using a reshuffled sequence.
   - **Consistent** for the same day when re-run (deterministic logic).

---

## **Workflow Summary**

1. **Python Script Execution**:  
   Generates a daily prompt number based on the current day and month.

2. **Slack Notification**:  
   - Posts the daily prompt to Slack.
   - Adds a threaded reply:  
     _"Feel free to post your responses here as a reply to this thread!"_

3. **Email Delivery**:  
   Sends an email with:
   - The daily prompt.
   - A link to the Slack message for easy navigation.

4. **Manual Trigger**:  
   The workflow supports manual execution through the GitHub Actions UI for testing or reruns.

---

## **Technical Overview**

1. **Python Script**:
   - Deterministically generates a daily number between 1–30.
   - Posts to Slack using the Slack API and constructs a thread for responses.
   - Sends email notifications using SMTP.

2. **GitHub Actions**:
   - Automates the script execution at **6 AM EST** every day.
   - Dynamically generates a `.env` file from GitHub Secrets containing:
     - Prompts (`PROMPT_1` through `PROMPT_30`).
     - Slack credentials.
     - Email credentials.

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/CouplesChallenge.git
cd CouplesChallenge
```

### **2. Add GitHub Secrets**
In your repository settings, add the following secrets:

| Secret Key         | Description                              |
|---------------------|------------------------------------------|
| `ENV_FILE`         | Full content of your `.env` file.        |
| `SLACK_TOKEN`      | Slack Bot Token for posting messages.    |
| `SLACK_CHANNEL`    | Slack channel ID for notifications.      |
| `EMAIL_USERNAME`   | Email sender's username.                 |
| `EMAIL_PASSWORD`   | Email sender's password.                 |
| `EMAIL_SMTP_SERVER`| SMTP server address (e.g., smtp.gmail.com). |
| `EMAIL_SMTP_PORT`  | SMTP port (e.g., 465 for SSL).           |
| `EMAIL_RECIPIENTS` | Comma-separated list of email recipients.|

### **3. Create Prompts in `.env`**
Add 30 unique prompts as environment variables:
```plaintext
PROMPT_1="Send your partner a surprise hug."
PROMPT_2="Share a fond memory together."
PROMPT_3="Plan a fun weekend date."
...
PROMPT_30="End the day with a loving gesture or word."
```

### **4. Test the Script Locally**
Run the script to test Slack and email delivery:
```bash
python script.py
```

### **5. Schedule and Manual Trigger**
- The workflow will run automatically at **6 AM EST** (11 AM UTC).
- To run it manually:
   - Go to **Actions** in your GitHub repository.
   - Select **"Daily Python Script Execution"** and click **"Run workflow"**.

---

## **Benefits**
- **Reconnect Effortlessly**: Small daily activities lead to stronger, healthier relationships.
- **Consistency**: Automation ensures delivery without manual effort.
- **Engagement**: Slack threads encourage couples to share their responses.
- **Ease of Use**: The prompts require just a few minutes per day.

---

## **Acknowledgments**
Inspired by [The Freemans](https://meetthefreemans.com), this application brings their 30-day challenge to life through technology and automation.