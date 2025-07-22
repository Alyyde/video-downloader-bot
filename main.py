import telebot
import requests
import os

# Tokenni muhit o'zgaruvchisidan olamiz
TOKEN = os.environ.get("7525317952:AAFZqCsmhcWpF9qX4iWX2XVmTY7gmq6M8a8")
bot = telebot.TeleBot(7525317952:AAFZqCsmhcWpF9qX4iWX2XVmTY7gmq6M8a8)

# Webhookni tozalaymiz (shart emas, lekin foydali)
bot.remove_webhook()

# Start komandasi
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Salom! Menga TikTok, Instagram yoki Pinterest videosining linkini yubor.")

# Video yuklovchi handler
@bot.message_handler(func=lambda m: True)
def download_video(message):
    url = message.text.strip()
    bot.reply_to(message, "⏳ Yuklanmoqda...")

    try:
        api_url = f"https://save-from.net/api/convert?url={url}"
        res = requests.get(api_url)
        data = res.json()

        if 'url' in data and 'meta' in data:
            title = data['meta'].get('title', 'Video')
            video_url = data['url']
            bot.send_message(message.chat.id, f"✅ {title}\n🔗 {video_url}")
        else:
            bot.send_message(message.chat.id, "❌ Video topilmadi. Iltimos, boshqa link yuboring.")
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Xatolik: {str(e)}")

bot.polling()
