## SublimeText Slack chat plugin

SublimeText Plugin to send selected text to Slack Chat.

### Quick Start
- Clone/download plugin to your SublimeText User folder under SubSlack

### Configuration

 1. Go to https://api.slack.com and create new TOKEN
 2. Open `Package Settings > SubSlack > Settings – Default`:

```
{
    "token": "YOUR_TOKEN_GOES_HERE",
    "bot_name": "SublimeSlack",
    "default_chat": "dev"
}
``` 

### Hotkeys configuration
`Preferences: Package Settings > SubSlack > Key Bindings – Default`:

```
  {
    "keys": ["shift+command+x"],
    "command": ""
  }
```

### Functions

	- Send selected text to chat room.