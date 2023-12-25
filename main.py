from typing import Final
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ContextTypes

TOKEN = '6858961228:AAEATkFS54VAhAUBv9PqcOyC391BLEpKQa0'
BOT_USERNAME: Final = '@AI_TSP_BOT'

# Command handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('You can start talk to me.')
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am an AI bot who will talk to you, so you can pass this exam. Send me voice message, and I will respond.')
    
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Custom text.')
    
# Response handlers

def voice_handler(text: str) -> str:
    processed:str = text.lower()
    
    if 'hello' in text:
        return 'Go fuck yourself.'
    if 'goodbuy' in text:
        return 'Go fuck yourself twice.'
    
    return 'Why there is no switch statements in python?'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
