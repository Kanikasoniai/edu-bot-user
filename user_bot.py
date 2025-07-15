from telegram.ext import Updater, CommandHandler
from config import USER_BOT_TOKEN, ADMIN_CHAT_ID
import random

print(f"Starting bot... Token: {USER_BOT_TOKEN}, Admin ID: {ADMIN_CHAT_ID}")

def generate_credentials():
    user_id = f"USR{random.randint(1000, 9999)}"
    password = f"PWD{random.randint(1000, 9999)}"
    return user_id, password

def start(update, context):
    user_id, password = generate_credentials()
    message = (
        "📚 Welcome to the Educational Bot!\n"
        f"🆔 ID: {user_id}\n🔐 Password: {password}\n\n"
        "Please choose your category:\n➡️ 11th\n➡️ 12th\n➡️ JEE\n➡️ NEET"
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    updater = Updater(USER_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
