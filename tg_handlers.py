from telegram import Update
from telegram.ext import CallbackContext

from dialogflow import detect_intent_text


async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Бот запущен")


async def reply(update: Update, context: CallbackContext):
    text = update.message.text.strip()
    answer = detect_intent_text(
        context.bot_data["google_key"],
        context.bot_data["dialogflow_id"],
        str(update.message.from_user.id),
        text,
        language_code="ru",
    )
    await update.message.reply_text(answer.fulfillment_text)
