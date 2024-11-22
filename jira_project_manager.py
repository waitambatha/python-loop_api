
import os
import json
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from fetch_schemes import fetch_scheme_ids, fetch_users

# Load environment variables
load_dotenv()

# Constants from .env
API_TOKEN = os.getenv("API_TOKEN")
DOMAIN = os.getenv("DOMAIN")
EMAIL = os.getenv("EMAIL")
BASE_URL = f"https://{DOMAIN}.atlassian.net/rest/api/3"

# Authentication
auth = HTTPBasicAuth(EMAIL, API_TOKEN)
headers = {"Accept": "application/json", "Content-Type": "application/json"}

# Create a new project in Jira
def create_project(key, name, description, lead_account_id):
    payload = {
        "assigneeType": "PROJECT_LEAD",
        "key": key,
        "name": name,
        "description": description,
        "leadAccountId": lead_account_id,
    }

    # Fetch and add default schemes
    permission_scheme_id = fetch_scheme_ids("permissionscheme", "permissionSchemes")
    if permission_scheme_id:
        payload["permissionScheme"] = permission_scheme_id

    # Fetch notification scheme (optional)
    notification_scheme_id = fetch_scheme_ids("notificationscheme", "notificationSchemes")
    if notification_scheme_id:
        payload["notificationScheme"] = notification_scheme_id

    # Fetch issue security scheme (optional)
    issue_security_scheme_id = fetch_scheme_ids("issuesecurityschemes", "issueSecuritySchemes")
    if issue_security_scheme_id:
        payload["issueSecurityScheme"] = issue_security_scheme_id

    # Make the API request
    url = f"{BASE_URL}/project"
    response = requests.post(url, headers=headers, auth=auth, json=payload)
    if response.status_code == 201:
        print("Project created successfully!")
        print(json.dumps(response.json(), indent=4))
    else:
        print("Failed to create project.")
        print(f"Status Code: {response.status_code}")
        print(response.text)

# Main execution
if __name__ == "__main__":
    # Fetch a valid lead account ID
    users = fetch_users()
    if users:
        for user in users:
            print(f"Display Name: {user['displayName']}, Account ID: {user['accountId']}")
        lead_account_id = input("Enter a valid Account ID for the project lead: ")
    else:
        print("No users found.")
        lead_account_id = None

    if lead_account_id:
        project_key = input("Enter the project key (e.g., 'EX'): ")
        project_name = input("Enter the project name: ")
        project_description = input("Enter the project description: ")

        create_project(project_key, project_name, project_description, lead_account_id)
