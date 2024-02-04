import logging
from asyncio import Queue
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, Application

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# Определяем обработчики команд
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, я простой Telegram-бот!")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Определяем функцию main для запуска бота
def main():
    application = Application.builder().token('YOYR_TOKEN').build()

    # Commands
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler('text', echo))

    # Run bot
    application.run_polling(1.0)

# Вызываем функцию main для запуска бота
if __name__ == '__main__':
    main()