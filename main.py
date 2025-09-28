import os
from telegram import Bot
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = Bot(token=TOKEN)

def start(update, context):
    update.message.reply_text("Бот запущено!")

def main():
    from telegram.ext import Updater
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
