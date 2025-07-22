import telebot
import requests
import os

TOKEN = os.environ.get("7525317952:AAFZqCsmhcWpF9qX4iWX2XVmTY7gmq6M8a8")
bot = telebot.TeleBot(TOKEN)

# Webhookni o‘chirish
bot.remove_webhook()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Send me a video link from TikTok, Instagram, or Pinterest.")

@bot.message_handler(func=lambda m: True)
def download_video(message):
    url = message.text.strip()
    bot.reply_to(message, "⏳ Downloading...")

    try:
        api_url = f"https://save-from.net/api/convert?url={url}"
        res = requests.get(api_url)
        data = res.json()

        if 'url' in data and 'meta' in data:
            title = data['meta'].get('title', 'video')
            video_url = data['url']
            bot.send_message(message.chat.id, f"✅ {title}\n🔗 {video_url}")
        else:
            bot.send_message(message.chat.id, "❌ Failed to retrieve video. Try another link.")

    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Error: {str(e)}")

bot.polling()
