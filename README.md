# Drone Webhook Notification Plugin

## Quickstart 🚀

```yaml
kind: pipeline
name: default

steps:
  
  - name: notify webhook
  image: lstama/apk-update-notification:latest
  settings:
    webhook_url:
      from_secret: webhook_url
    webhook_text: "sample text"
```

### Details 📒

The plugins send a post request to webhook url with payload {"text" : "sample text"}