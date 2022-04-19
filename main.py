"""
Simple Bot to reply to Telegram messages taken from the python-telegram-bot examples.
Source: https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py
"""

import logging
import os

from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

is_prod = os.environ.get('IS_PROD', None)
if not is_prod:
    load_dotenv('.env')
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
PORT =  int(os.environ.get('PORT', '8443'))


def play(update: Updater, context: CallbackContext) -> None:
    update.message.reply_text("Don't forget to play Tradle today! https://oec.world/en/tradle/")
    

def error(update: Updater, context: CallbackContext) -> None:
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("play", play))
    dp.add_error_handler(error)

    updater.start_webhook(
        listen='0.0.0.0',
        port=PORT,
        url_path=TOKEN,
        webhook_url='https://tradlebot.herokuapp.com/' + TOKEN,
    )

    updater.idle()

if __name__ == '__main__':
    main()
