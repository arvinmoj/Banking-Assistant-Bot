import os
import json
from telegram import Update
from telegram.ext import ContextTypes
from src.api_handler import call_api
from src.utils.logging import configure_logging

logger = configure_logging()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TELEGRAM_TOKEN:
    logger.error("Environment variable TELEGRAM_BOT_TOKEN is not set.")
    exit(1)

# Function to send a message via Telegram bot
async def send_telegram_message(chat_id, message, context: ContextTypes.DEFAULT_TYPE):
    try:
        await context.bot.send_message(chat_id=chat_id, text=message)
    except Exception as e:
        logger.error(f"Failed to send message to Telegram: {e}")

# Handler for incoming messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    logger.info(f"Received message from {update.effective_user.id}: {user_message}")

    input_data = user_message
    api_response = call_api(input_data)

    # Extract the part of the response you care about
    if isinstance(api_response, dict):
        try:
            # Extract the relevant "text" response
            if "outputs" in api_response and "text" in api_response["outputs"]:
                formatted_message = api_response["outputs"]["text"]
            else:
                # Log the full response and return a fallback message
                logger.error(f"Unexpected response structure: {json.dumps(api_response, indent=2)}")
                formatted_message = "Error: Unexpected response structure."
        except (TypeError, ValueError) as e:
            logger.error(f"JSON formatting error: {e}")
            formatted_message = "Error: Unable to format the API response."
    else:
        formatted_message = api_response  # This contains the error message

    await send_telegram_message(update.effective_chat.id, formatted_message, context)

# Optional: Handler for the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "Hello! I'm your bot. Send me any message, and I'll process it using the API."
    )
    await update.message.reply_text(welcome_text)
