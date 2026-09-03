from datetime import time
from decouple import config
import os
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from handlers import (start, repeat_after, reply
)

TELEGRAM_BOT_TOKEN = config("TELEGRAM_BOT_TOKEN")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = config('GOOGLE_APPLICATION_CREDENTIALS')
DIALOGFLOW_PROJECT_ID=config('DIALOGFLOW_PROJECT_ID')


def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    # app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, repeat_after))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    app.run_polling()


if __name__ == "__main__":
    main()
