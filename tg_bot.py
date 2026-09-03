from decouple import config
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from tg_handlers import reply, start


def main():
    tg_bot_token = config("TELEGRAM_BOT_TOKEN")
    app = Application.builder().token(tg_bot_token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    app.run_polling()


if __name__ == "__main__":
    main()
