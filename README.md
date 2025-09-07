# jira-testing-notifier

## Overview
jira-testing-notifier is a Python tool designed to send notifications about JIRA tickets, especially for testing or QA workflows. It can be integrated into CI/CD pipelines or used as a standalone script to alert users about ticket status changes, assignments, or other JIRA events.

## Features
- Connects to JIRA using API credentials
- Monitors ticket status and updates
- Sends notifications (email, Slack, etc.)
- Customizable notification rules

## Requirements
- Python 3.7+
- JIRA account and API token

## Installation
Clone the repository:

```powershell
git clone https://github.com/engRana404/jira-testing-notifier.git
cd jira-testing-notifier
```

## Configuration
Edit `jira.py` to add your JIRA credentials and notification settings. You may need to set environment variables or update configuration sections as needed.

## Usage
Run the notifier script:

```powershell
python jira.py
```

## Example
The script will connect to JIRA, check for relevant tickets, and send notifications based on your configuration.


## Author

### **Rana Gamal**  
- 🌐 [LinkedIn](https://www.linkedin.com/in/rana-gamal-daif)
- 💻 [GitHub](https://github.com/engRana404)
- ✉️ [Email](mailto:RanaGamalDaif@gmail.com) 

