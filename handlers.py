from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.error import Forbidden
from telegram.ext import ContextTypes, ConversationHandler, CallbackContext


async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Здравствуйте')

async def repeat_after(update: Update, context: CallbackContext):
    text = update.message.text.strip()
    await update.message.reply_text(text)