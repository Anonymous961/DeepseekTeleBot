import logging
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, Updater, filters
from deepseek import *
from dotenv import load_dotenv
import time
import os
import asyncio

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

unique_users = set()
total_questions = 0


async def track_metrics(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global unique_users, total_questions

    # Track unique users
    user_id = update.effective_user.id
    unique_users.add(user_id)

    # Track total questions
    total_questions += 1

    # Log metrics
    logging.info(f"Unique Users: {len(unique_users)}, Total Questions: {total_questions}")


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    await update.message.reply_text(f'Thanks for using this bot. Please feel free to chat with me!')


async def typing_indicator(chat_id, context: ContextTypes.DEFAULT_TYPE):
    """Continuously send typing action until the task is done."""
    while True:
        await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
        await asyncio.sleep(2)  # Send typing action every 2 seconds


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await track_metrics(update, context)
    typing_task = asyncio.create_task(typing_indicator(update.effective_chat.id, context))

    user_message = update.message.text
    answer = await asyncio.to_thread(get_answer, user_message)  # Run blocking function in a separate thread
    typing_task.cancel()

    # Send the response
    await update.message.reply_text(answer)


app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
