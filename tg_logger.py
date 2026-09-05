import logging

import requests

logger = logging.getLogger(__name__)


class TgLogsHandler(logging.Handler):
    def __init__(self, bot_token, chat_id):
        super().__init__()
        self.bot_token = bot_token
        self.chat_id = chat_id

    def emit(self, record):
        log_entry = self.format(record)
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        response = requests.post(url, data={"chat_id": self.chat_id, "text": log_entry})
        response.raise_for_status()


def setup_logger(bot_token, chat_id, start_text):
    handler = TgLogsHandler(bot_token, chat_id)
    handler.setLevel(logging.WARNING)
    handler.setFormatter(logging.Formatter("%(levelname)s %(name)s\n%(message)s"))
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(handler)
    logger.warning(start_text)
