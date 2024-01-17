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
    application = Application.builder().token('').build()

    # Commands
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler('text', echo))

    # Run bot
    application.run_polling(1.0)
    # Создаем объект Updater и передаем ему токен вашего бота
    # bot = Bot(token='')
    # update_queue = Queue()
    #
    # updater = Updater(bot, update_queue)
    #
    # # Получаем объект диспетчера для регистрации обработчиков
    # # dispatcher = updater.dispatcher
    #
    # # Регистрируем обработчики команд
    # start_handler = CommandHandler('start', start)
    # dispatcher.add_handler(start_handler)
    #
    # # Регистрируем обработчики сообщений
    # echo_handler = MessageHandler(filters.text, echo)
    # dispatcher.add_handler(echo_handler)
    #
    # # Запускаем бота
    # updater.start_polling()
    #
    # # Останавливаем бота вручную, если нажата Ctrl+C
    # updater.idle()

# Вызываем функцию main для запуска бота
if __name__ == '__main__':
    main()
