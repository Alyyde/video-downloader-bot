import telebot

bot = telebot.TeleBot("YOUR_BOT_TOKEN")  # bu yerga bot tokeningni yoz
bot.remove_webhook()
print("✅ Webhook removed.")
