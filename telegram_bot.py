from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from datetime import datetime

# Replace 'YOUR_TOKEN_HERE' with your bot's token
TOKEN = '7942164878:AAEvsE6uQsClEZhI12ikeUZ4sOxcyiecEPg'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot. How can I help you?')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Available commands:\n/start - Start the bot\n/help - Show this help message\n/time - Show current server time')

def time_command(update: Update, context: CallbackContext) -> None:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    update.message.reply_text(f'Current server time: {current_time}')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the /start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Register the /help command handler
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Register the /time command handler
    dispatcher.add_handler(CommandHandler("time", time_command))

    # Register a message handler to echo messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()