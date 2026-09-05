import logging

from decouple import config
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from tg_handlers import reply, start
from tg_logger import setup_logger

logger = logging.getLogger(__name__)


def main():
    setup_logger(config("TG_BOT_TOKEN"), config("TG_USER_ID"), "ТГ-бот запущен")

    tg_bot_token = config("TELEGRAM_BOT_TOKEN")
    app = Application.builder().token(tg_bot_token).build()
    app.bot_data["google_key"] = config("GOOGLE_APPLICATION_CREDENTIALS")
    app.bot_data["dialogflow_id"] = config("DIALOGFLOW_PROJECT_ID")
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    try:
        app.run_polling()
    except Exception:
        logger.exception("Ошибка в ТГ-боте")


if __name__ == "__main__":
    main()
