import sqlite3
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


# Подключение к базе данных
def db_connection():
    conn = sqlite3.connect('database.db')
    return conn

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Введите почту или телефонный номер")

# Команда /find_email
def email(update: Update, context: CallbackContext):
    email = ' '.join(context.args)
    if not email:
        update.message.reply_text("Введите email.")
        return

    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emails WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()

    if result:
        update.message.reply_text(f"Данный email {email} найден.")
    else:
        update.message.reply_text(f"Данный email {email} не найден.")

# Команда /find_phone
def phone(update: Update, context: CallbackContext):
    phone = ' '.join(context.args)
    if not phone:
        update.message.reply_text("Введите номер:")
        return

    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM phones WHERE phone = ?", (phone,))
    result = cursor.fetchone()
    conn.close()

    if result:
        update.message.reply_text(f"Номер телефона {phone} найден.")
    else:
        update.message.reply_text(f"Номер телефона {phone} не найден.")

def main():
 
    updater = Updater('7985696955:AAHJc62xNSBITmJoNBXmlHk0VeZdy7rmBJ4', use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("email", email))
    dp.add_handler(CommandHandler("phone", phone))
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

DB_NAME = 'db'
DB_USER = 'abdulatipov'
DB_PASSWORD = 'gusen12345'
DB_HOST = '127.0.0.1'
DB_PORT = '5432'