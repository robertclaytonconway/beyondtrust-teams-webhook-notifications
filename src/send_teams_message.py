import os
import logging
import requests
from dotenv import load_dotenv

load_dotenv()

TEAMS_WEBHOOK_URL = os.getenv("TEAMS_WEBHOOK_URL")
NOTIFICATION_TITLE = os.getenv("NOTIFICATION_TITLE", "BeyondTrust EPM Notification")
DEFAULT_ENVIRONMENT = os.getenv("DEFAULT_ENVIRONMENT", "Lab")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s %(levelname)s %(message)s"
)


def build_message():
    """
    Build a simple Microsoft Teams webhook message.

    Replace the sample values with sanitized BeyondTrust workflow data.
    """

    return {
        "text": (
            f"**{NOTIFICATION_TITLE}**\n\n"
            f"**Environment:** {DEFAULT_ENVIRONMENT}\n\n"
            "**Request Type:** JIT Admin Access\n\n"
            "**User:** jsmith@example.com\n\n"
            "**Host:** WIN10-TEST-01\n\n"
            "**Duration:** 24 hours\n\n"
            "**Reason:** Install approved business application\n\n"
            "**Status:** Pending Review"
        )
    }


def send_message(payload):
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
    payload = build_message()
    response = send_message(payload)
    logging.info("Teams message sent successfully. Status code: %s", response.status_code)


if __name__ == "__main__":
    main()
