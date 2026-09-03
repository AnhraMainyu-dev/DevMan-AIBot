from datetime import time
from decouple import config

from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from handlers import (start, repeat_after
)

TELEGRAM_BOT_TOKEN = config("TELEGRAM_BOT_TOKEN")


def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, repeat_after))
    app.run_polling()


if __name__ == "__main__":
    main()
