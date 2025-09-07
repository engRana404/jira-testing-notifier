import requests
from requests.auth import HTTPBasicAuth
import time
import os
from dotenv import load_dotenv

load_dotenv()

JIRA_DOMAIN = os.getenv("JIRA_DOMAIN")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
PROJECT_KEY = os.getenv("PROJECT_KEY")

# JQL query for project FLED in Testing
JQL_QUERY = f'project = {PROJECT_KEY} AND status = "Testing" ORDER BY created DESC'

# Keep track of already posted issues
seen_issues = set()

def get_testing_issues():
    url = f"{JIRA_DOMAIN}/rest/api/3/search"
    headers = {"Accept": "application/json"}
    params = {"jql": JQL_QUERY, "maxResults": 10}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN),
    )

    if response.status_code != 200:
        print("Failed to fetch Jira issues:", response.text)
        return []

    data = response.json()
    return data.get("issues", [])

def send_to_discord(issue):
    issue_key = issue["key"]
    link = f"{JIRA_DOMAIN}/browse/{issue_key}"

    message = {
        "content": (
            f"📝 **{issue_key}** moved to **Testing**\n"
            f"🔗 {link}"
        )
    }

    requests.post(DISCORD_WEBHOOK_URL, json=message)

def main():
    while True:
        issues = get_testing_issues()
        for issue in issues:
            # Only notify once per issue
            if issue["key"] not in seen_issues:
                send_to_discord(issue)
                seen_issues.add(issue["key"])
        time.sleep(60)  # check every 1 minute

if __name__ == "__main__":
    main()
