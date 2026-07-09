import os
import logging
import requests
from dotenv import load_dotenv

load_dotenv()

TEAMS_WEBHOOK_URL = os.getenv("TEAMS_WEBHOOK_URL")
DEFAULT_ENVIRONMENT = os.getenv("DEFAULT_ENVIRONMENT", "Lab")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s %(levelname)s %(message)s"
)


def build_adaptive_card():
    """
    Build a Microsoft Teams Adaptive Card payload for a BeyondTrust EPM request.

    This is a sanitized lab-safe example.
    """

    return {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.4",
                    "body": [
                        {
                            "type": "TextBlock",
                            "text": "BeyondTrust EPM JIT Admin Request",
                            "weight": "Bolder",
                            "size": "Large"
                        },
                        {
                            "type": "FactSet",
                            "facts": [
                                {"title": "Environment:", "value": DEFAULT_ENVIRONMENT},
                                {"title": "User:", "value": "jsmith@example.com"},
                                {"title": "Host:", "value": "WIN10-TEST-01"},
                                {"title": "Request Type:", "value": "Temporary Admin Access"},
                                {"title": "Duration:", "value": "24 hours"},
                                {"title": "Reason:", "value": "Install approved business application"},
                                {"title": "Status:", "value": "Pending Review"}
                            ]
                        }
                    ],
                    "actions": [
                        {
                            "type": "Action.OpenUrl",
                            "title": "Open BeyondTrust Console",
                            "url": "https://beyondtrust.example.com"
                        }
                    ]
                }
            }
        ]
    }


def send_card(payload):
    if not TEAMS_WEBHOOK_URL:
        raise ValueError("TEAMS_WEBHOOK_URL is missing from .env")

    response = requests.post(
        TEAMS_WEBHOOK_URL,
        json=payload,
        timeout=30
    )

    response.raise_for_status()
    return response


def main():
    payload = build_adaptive_card()
    response = send_card(payload)
    logging.info("Adaptive Card sent successfully. Status code: %s", response.status_code)


if __name__ == "__main__":
    main()
