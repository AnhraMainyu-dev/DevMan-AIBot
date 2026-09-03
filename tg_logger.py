import logging

import requests
from decouple import config

TG_BOT_TOKEN = config("TG_BOT_TOKEN")
TG_USER_ID = config("TG_USER_ID")

logger = logging.getLogger(__name__)


class TgLogsHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.bot_token = TG_BOT_TOKEN
        self.chat_id = TG_USER_ID

    def emit(self, record):
        log_entry = self.format(record)
        url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"
        response = requests.post(url, data={"chat_id": TG_USER_ID, "text": log_entry})
        response.raise_for_status()


def setup_logger(start_text):
    handler = TgLogsHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter("%(levelname)s %(name)s\n%(message)s"))
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(handler)
    logger.info(start_text)
