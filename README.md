# **Garrett Couples Challenge**

## **Overview**
Garrett Couples Challenge is a daily reminder application inspired by the *30-Day Couples Challenge* from [meetthefreemans.com](https://meetthefreemans.com). It helps couples reconnect and strengthen their relationship through quick, actionable prompts delivered consistently every day.

## Categories
Daily prompts are thoughtfully designed and drawn from these categories:
- **Love Deposit**: Playful gestures to express love and gratitude.
- **Communication Tip**: Practical advice to improve relationship dynamics.
- **Conversation Starter**: Thought-provoking questions to spark deeper discussions.

## Purpose and Benefits
- **Foster Connection**: Small, consistent actions strengthen bonds and show appreciation.  
- **Improve Communication**: Practical tips and questions enhance listening, understanding, and expression.  
- **Effortless Engagement**: Automation ensures prompts are delivered daily without manual effort.  
- **Encourage Interaction**: Slack threads make it easy to share responses and stay connected.  
- **Ease of Use**: Prompts are quick and simple, making participation stress-free.

## Features
#### Daily Automation:
- Prompts are delivered at **6 AM EST** via **GitHub Actions**, ensuring reliability and consistency. Manual triggers are also available for testing or re-runs.

#### Deterministic Prompt Selection:
- A Python script selects prompts based on the **month** and **day**, ensuring:
  - **Non-repeating** outputs within the month.
  - **Varied** sequences each month through reshuffling.
  - **Consistency** for the same day when re-run.

#### Slack Integration:
- Prompts are posted to a designated Slack channel with a **threaded reply**, encouraging couples to share responses.

#### Email Integration:
- Prompts are also emailed to recipients, including a link to the Slack thread for easy engagement.

---

### **Setup - Add GitHub Secrets**
In your repository settings, add the following secrets:

| Secret Key         | Description                              |
|---------------------|------------------------------------------|
| `ENV_FILE`         | Full content of your `.env` file, see .env.example for format.        |

### **Setup - Create Prompts in `.env`**
Add 30 unique prompts as environment variables:
```plaintext
PROMPT_1="Send your partner a surprise hug."
PROMPT_2="Share a fond memory together."
PROMPT_3="Plan a fun weekend date."
...
PROMPT_30="End the day with a loving gesture or word."
```

### **Development - Test the Script Locally**
Run the script to test Slack and email delivery:
```bash
python execute.py
```

### **Information - Trigger vi GH Actions**
- The workflow will run automatically at **6 AM EST** (11 AM UTC).
- To run it manually:
   - Go to **Actions** in your GitHub repository.
   - Select **"Execute Daily Challenge Reminder"** and click **"Run workflow"**.

## **Acknowledgments**
Inspired by [The Freemans](https://meetthefreemans.com), this application brings their 30-day challenge to life through technology and automation.