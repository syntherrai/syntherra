import requests
import json

def send_webhook_notification(url, message):
    payload = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        print(f"Webhook failed: {e}")
        return False
