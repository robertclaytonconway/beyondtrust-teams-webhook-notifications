# Microsoft Teams Webhook Guide

## Simple Message Format

A basic Teams webhook message can use:

```json
{
  "text": "BeyondTrust EPM request received"
}
```

## Adaptive Card Format

Adaptive Cards provide a cleaner layout for SOC notifications.

Useful fields:

| Field | Purpose |
|---|---|
| `TextBlock` | Title or summary |
| `FactSet` | Key/value request details |
| `Action.OpenUrl` | Link to console or ticket |

## Recommended Notification Fields

| Field | Example |
|---|---|
| Request Type | JIT Admin Access |
| User | jsmith@example.com |
| Hostname | WIN10-TEST-01 |
| Platform | Windows |
| Duration | 24 hours |
| Application | ExampleInstaller.exe |
| Reason | Install approved business application |
| Status | Pending Review |

## Security Considerations

Teams webhook URLs act like secrets. Anyone with the URL can post to the channel.

Protect the webhook URL the same way you would protect an API token.
