import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

from api_fetcher import ApiFetcher



# Load environment variables from .env file
load_dotenv()
# Get the bot token from the .env
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

start_menu = """Write the name (not the symbol) of a crypto coin to get info for the last 24h.
    \nFor example; you can try with "bitcoin" or "ethereum".
    \nI can only manage coins listed on www.coingecko.com.
    """


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! " + start_menu)


async def get_coin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    api_fetcher = ApiFetcher()
    msg = update.message.text.strip().lower()
    coin_name = msg.split()[0]
    coin_data = api_fetcher.get_coin(coin_name)
    if coin_data is not None:
        await update.message.reply_text(str(coin_data))
    else:
        await update.message.reply_text("I can't find '" + coin_name + "'\n" + start_menu)


if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), get_coin)
    application.add_handler(start_handler)
    application.add_handler(message_handler)

    application.run_polling()