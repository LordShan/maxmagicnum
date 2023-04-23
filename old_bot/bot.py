import os
from dotenv import load_dotenv
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler,filters,ConversationHandler

# Настройки логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

load_dotenv()
# Токен вашего бота
TOKEN = os.getenv('TOKEN') 

# Определение состояний диалога
START, ENTER_NUMBER = range(2)
# Обработчик команды /start

# def auto_start(update, context):
#     context.bot.send_message(chat_id=update.message.chat_id, text="Здравствуйте! Я телеграм-бот. Чем я могу вам помочь?")
    


def start(update, context):
    # Создаем кнопки для первого набора
    button1 = InlineKeyboardButton(text="I guess the number...", callback_data="set2")
    button2 = InlineKeyboardButton(text="You guess the number...", callback_data="set2")
    button3 = InlineKeyboardButton(text="Settings...", callback_data="enter_number")
    # Создаем панель для первого набора кнопок
    keyboard1 = [[button1], [button2], [button3]]
    reply_markup1 = InlineKeyboardMarkup(keyboard1)
    # Отправляем сообщение с первым набором кнопок
    update.message.reply_text(text="Choose an option:", reply_markup=reply_markup1)
# Обработчик нажатия на кнопку

# Функция, которая будет вызываться после ввода числа пользователем
def handle_number(update, context):
    text = update.message.text
    try:
        number = int(text)
        update.message.reply_text(f"Вы ввели число {number}")
    except ValueError:
        update.message.reply_text("Ошибка! Введите целое число.")


def button(update, context):
    query = update.callback_query
    # Обрабатываем нажатие на кнопку
    if query.data == "set2":
        # Создаем кнопки для второго набора
        button4 = InlineKeyboardButton(text="Button 4", callback_data="set1")
        button5 = InlineKeyboardButton(text="Button 5", callback_data="set1")
        button6 = InlineKeyboardButton(text="Button 6", callback_data="set1")
        # Создаем панель для второго набора кнопок
        keyboard2 = [[button4], [button5], [button6]]
        reply_markup2 = InlineKeyboardMarkup(keyboard2)
        # Отправляем сообщение с вторым набором кнопок
        query.edit_message_text(text="Choose another option:", reply_markup=reply_markup2)
    elif query.data == "set1":
        # Создаем кнопки для первого набора
        button1 = InlineKeyboardButton(text="I guess the number...", callback_data="set2")
        button2 = InlineKeyboardButton(text="You guess the number...", callback_data="set2")
        button3 = InlineKeyboardButton(text="Settings...", callback_data="enter_number")
        # Создаем панель для первого набора кнопок
        keyboard1 = [[button1], [button2], [button3]]
        reply_markup1 = InlineKeyboardMarkup(keyboard1)
        # Отправляем сообщение с первым набором кнопок
        query.edit_message_text(text="Choose an option:", reply_markup=reply_markup1)
    
        
        pass
            
# Функция, которая будет вызываться после нажатия на кнопку "Ввести число"
def enter_number(update, context):
    update.callback_query.answer()
    update.callback_query.edit_message_text('Введите число:')

    return ENTER_NUMBER


# Главная функция


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    # Добавление обработчика для автостарта
    # dp.add_handler(MessageHandler(filters.Filters.status_update.new_chat_members, auto_start))  
    # Обработчики команд
    dp.add_handler(CommandHandler("menu", start))

    # Обработчики кнопок
    dp.add_handler(CallbackQueryHandler(button))
    
    # Добавляем обработчик для кнопки "Ввести число"
    dp.add_handler(CallbackQueryHandler(enter_number, pattern='enter_number'), group=1)
    # Добавляем обработчик для ввода числа
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Filters.text, start)],
        states={
            START: [CallbackQueryHandler(enter_number, pattern='enter_number')],
            ENTER_NUMBER: [MessageHandler(filters.Filters.text, handle_number)]
        },
        fallbacks=[],
        allow_reentry=True
    )
    dp.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
