# Setup Guide

## 1. Create a Microsoft Teams Incoming Webhook

In Microsoft Teams:

```text
Team Channel → Connectors / Workflows → Incoming Webhook
```

Create a webhook for the SOC or security channel.

Copy the webhook URL and store it locally in `.env`.

Do not commit the webhook URL to GitHub.

## 2. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/beyondtrust-teams-webhook-notifications.git
cd beyondtrust-teams-webhook-notifications
```

## 3. Create Python Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 4. Configure Environment

```bash
cp .env.example .env
nano .env
```

Update:

```text
TEAMS_WEBHOOK_URL=
DEFAULT_ENVIRONMENT=
```

## 5. Send a Test Message

```bash
python3 src/send_teams_message.py
```

## 6. Send a Test Adaptive Card

```bash
python3 src/send_adaptive_card.py
```

## 7. Connect to BeyondTrust Workflow

In BeyondTrust EPM, configure the workflow/webhook action to send request data to a webhook handler or automation endpoint.

Common events to route:

- JIT admin request
- Application elevation request
- Permanent exception request
- Blocked application alert
- macOS elevation request

## 8. Production Safety

- Use a dedicated Teams channel.
- Do not expose webhook URLs.
- Rotate webhook URLs if leaked.
- Avoid posting secrets, passwords, internal URLs, or customer data.
- Keep messages concise and actionable.
