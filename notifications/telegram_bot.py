import requests

class TelegramBot:
    def __init__(self, bot_token, chat_id):
        self.url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        self.chat_id = chat_id

    def send_message(self, text):
        payload = {
            "chat_id": self.chat_id,
            "text": text,
            "parse_mode": "Markdown"
        }
        try:
            response = requests.post(self.url, data=payload)
            return response.status_code == 200
        except Exception as e:
            print(f"Telegram error: {e}")
            return False
