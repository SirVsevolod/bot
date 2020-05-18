#!/usr/bin/python

from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters

TG_TOKEN = "755908622:AAHYBgcmqZa-OABhnTGyKgUzZQDRpvE3Bdo"

def message_handler(bot: Bot, update: Update):
    user = update.effective_user

    if user: 
        neme= user.first_name
    else:
        name = "Аноним"

    text = update.effective_message.text
    reply_text = f"Привет, {name}!\n\n{text}"

    bot.send_message(
        chat_id = update.effective_message.chat_id,
        text = reply_text,
    )


def main():
    bot = Bot(
        token = TG_TOKEN,
        base_url = "https://telegg.ru/orig/bot"
    )
    updater = Updater(
        bot = bot,
        use_context = True
    )

    handler = MessageHandler(Filters.all, message_handler)
    updater.dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
