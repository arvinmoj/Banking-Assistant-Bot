from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from src.tg_bot import TELEGRAM_TOKEN, start_command, handle_message, logger

def main():
    # Initialize the application
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start polling for updates
    logger.info("Bot is starting...")
    application.run_polling()

if __name__ == "__main__":
    main()