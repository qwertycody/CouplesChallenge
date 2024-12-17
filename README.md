# **CouplesChallenge**

## **Overview**
CouplesChallenge is a daily reminder application inspired by the *30-Day Couples Challenge* from [meetthefreemans.com](https://meetthefreemans.com). It simplifies how couples can reconnect through small, actionable tasks that promote love, communication, and understanding.

---

## **Purpose**
Life gets busy, and relationships often take a back seat. CouplesChallenge helps couples:
- Refocus on their relationship through quick, daily prompts.
- Balance "love deposits" to prevent communication breakdowns.
- Foster more meaningful conversations and gestures in just a few minutes per day.

---

## **How It Works**
1. **Daily Prompts**: Couples receive a unique daily activity for 30 days, selected from one of the following categories:
   - **Love Deposit**: Small, playful gestures to build appreciation.
   - **Communication Tip**: Simple suggestions to improve listening and speaking.
   - **Conversation Starter**: Thought-provoking questions for deeper connection.

2. **Quick and Achievable**: Activities are designed to take just **1–5 minutes**, even for the busiest couples.

3. **Unique Daily Tasks**:  
   - Numbers for daily prompts are generated using a deterministic script that ensures non-repetition within a month and varied results each month.

---

## **Technical Features**
- **Script Logic**: Generates a unique daily number (1–30) based on:
   - Month-specific shuffled sequences.
   - Consistency for the same day across runs while ensuring monthly variation.
- **Automation**:  
   - GitHub Actions automates the script execution daily at **6 AM EST**.  
   - Results are posted to Slack and emailed to users for easy access.

---

## **Workflow Summary**
1. **Python Script Execution**:  
   Generates the unique daily number for prompt selection.

2. **Slack Notifications**:  
   Script results are sent to a designated Slack channel.

3. **Email Delivery**:  
   Users receive the same results via email and/or SMS text message for accessibility.  

4. **Manual Trigger**:  
   The workflow can also be triggered manually for testing or re-runs.

---

## **Benefits**
- **Reconnect Easily**: Small daily efforts lead to a significant positive impact.  
- **Designed for Busy Couples**: Prompts work even during travel, family activities, or hectic days.  
- **Reliability**: Automation ensures consistent and reliable delivery.

---

## **Getting Started**
1. Clone this repository.  
2. Set up GitHub Secrets:
   - `SLACK_API_TOKEN`: Slack Bot Token.  
   - `EMAIL_USER` and `EMAIL_PASS`: Credentials for email provider.  
3. Configure Slack and email details in the workflow file.  
4. Push the setup, and GitHub Actions will handle the rest!

---

## **Acknowledgments**
Inspired by [The Freemans](https://meetthefreemans.com). This application brings their proven methods to life through automation and consistency.

---