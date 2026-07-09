# BeyondTrust Workflow Notes

## Common Workflow Types

| Workflow | Description |
|---|---|
| JIT Admin Request | User requests temporary admin access |
| Application Elevation | User requests elevation for a specific app |
| Permanent Exception | User requests ongoing exception |
| Blocked Application | EPM blocks execution or elevation |
| macOS Request | macOS endpoint privilege request |

## Recommended SOC Review Fields

| Field | Reason |
|---|---|
| User | Identifies requester |
| Hostname | Identifies endpoint |
| Platform | Windows/macOS context |
| Application | Shows requested executable |
| Publisher | Helps validate legitimacy |
| File hash | Supports reputation checks |
| Duration | Confirms access window |
| Business reason | Helps approve or deny |
| Policy name | Shows EPM control path |

## Suggested Approval Logic

| Condition | Action |
|---|---|
| Known approved business app | Approve temporary elevation |
| Unknown unsigned binary | Deny or escalate |
| Remote admin tool | Escalate for review |
| Script interpreter request | Escalate |
| Repeated request from same user | Review policy gap |
| macOS system change | Validate with Jamf/IT owner |

## Notes

This repo uses placeholder data. Replace sample fields with sanitized lab data only.
