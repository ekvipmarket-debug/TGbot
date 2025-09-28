from telegram import Bot

TOKEN = AAH__ie40UxlVUOMw-dXP1D5tewFGBAp2tY
CHANNEL_ID = "@tatyshcho"

bot = Bot(token=TOKEN)

def post_news():
    news_text = "Привет! Это автоматическая новость от бота."
    bot.send_message(chat_id=CHANNEL_ID, text=news_text)

if __name__ == "__main__":
    post_news()


