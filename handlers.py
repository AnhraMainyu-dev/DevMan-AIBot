from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.error import Forbidden
from telegram.ext import ContextTypes, ConversationHandler, CallbackContext
from dialogflow import detect_intent_text
from decouple import config

DIALOGFLOW_PROJECT_ID=config("DIALOGFLOW_PROJECT_ID")

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Здравствуйте')

async def repeat_after(update: Update, context: CallbackContext):
    text = update.message.text.strip()
    await update.message.reply_text(text)

async def reply(update: Update, context: CallbackContext):
    text = update.message.text.strip()
    answer = detect_intent_text(DIALOGFLOW_PROJECT_ID, str(update.message.from_user.id), text, language_code='ru')
    await update.message.reply_text(answer.fulfillment_text)