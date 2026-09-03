from decouple import config
from telegram import Update
from telegram.ext import CallbackContext

from dialogflow import detect_intent_text

DIALOGFLOW_PROJECT_ID = config("DIALOGFLOW_PROJECT_ID")


async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Бот запущен")


async def reply(update: Update, context: CallbackContext):
    text = update.message.text.strip()
    answer = detect_intent_text(
        DIALOGFLOW_PROJECT_ID,
        str(update.message.from_user.id),
        text,
        language_code="ru",
    )
    await update.message.reply_text(answer.fulfillment_text)
