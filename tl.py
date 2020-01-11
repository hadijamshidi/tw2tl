import settings
import telegram

Bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)


def send2channel(msg):
    Bot.sendMessage(chat_id=settings.TELEGRAM_CHANNEL, text=msg)
