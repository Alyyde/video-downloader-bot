import telebot

bot = telebot.TeleBot("7525317952:AAFZqCsmhcWpF9qX4iWX2XVmTY7gmq6M8a8")  # bu yerga bot tokeningni yoz
bot.remove_webhook()
print("✅ Webhook removed.")
