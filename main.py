import telebot
import requests
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "📥 Menga TikTok, Instagram yoki Pinterest videosining linkini yuboring.")

@bot.message_handler(func=lambda m: True)
def download_video(message):
    url = message.text.strip()
    bot.reply_to(message, "⏳ Yuklanmoqda...")
    try:
        api_url = f"https://save-from.net/api/convert?url={url}"
        res = requests.get(api_url)
        data = res.json()
        if 'url' in data and 'meta' in data:
            title = data['meta'].get('title', 'video')
            video_url = data['url']
            bot.send_message(message.chat.id, f"✅ {title}\n🔗 {video_url}")
        else:
            bot.send_message(message.chat.id, "❌ Video topilmadi. Iltimos, boshqa linkni sinab ko‘ring.")
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Xatolik: {str(e)}")

bot.remove_webhook()
bot.polling()
