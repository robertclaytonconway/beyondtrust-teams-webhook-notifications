# Security Policy

## Sensitive Data

Do not commit:

- Real Microsoft Teams webhook URLs
- BeyondTrust API keys
- Internal hostnames
- Usernames from production
- Customer data
- Screenshots from production systems
- Internal URLs
- Approval logs
- Private payloads

## Safe Usage

This repository is designed for lab and portfolio use. Use placeholder data or sanitized examples only.

## Webhook Security

Teams webhook URLs are secrets. If a webhook URL is exposed, rotate or delete the webhook immediately.
