import requests
import time
import telegram.ext
import telegram
from telegram.ext import Updater, CommandHandler

# Telegram Bot Token
with open("token.txt", "r", encoding="utf-8") as f:
    TOKEN = f.read().strip()

# Cryptopanic API URL'si
api_url = "https://cryptopanic.com/api/v1/posts/?auth_token=345b58e07de1eabf54bcc8317cc27f6903928a7b&kind=news"

# Son alınan haber bilgisini tutmak için bir değişken
last_post_id = None

def start(update, context):
    update.message.reply_text("g0khanbey", parse_mode=telegram.ParseMode.HTML)

def site(update, context):
    update.message.reply_text("<b>g0khanbey</b>", parse_mode=telegram.ParseMode.HTML)

def video(update, context):
    update.message.reply_text("<b>g0khanbey</b>", parse_mode=telegram.ParseMode.HTML, disable_web_page_preview=True)

def check_and_send_message(context: telegram.ext.CallbackContext):
    global last_post_id
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        latest_post = data["results"][0]  # En son haber bilgisi

        if last_post_id != latest_post["id"]:
            last_post_id = latest_post["id"]

            title = latest_post["title"]
            published_at = latest_post["published_at"]
            url = latest_post["url"]
            content = latest_post.get("content", "İçerik bulunmuyor.")

            with open("son_haber.txt", "w", encoding="utf-8") as file:
                file.write(f"Başlık: {title}\n")
                file.write(f"Yayın Tarihi: {published_at}\n")
                file.write(f"URL: {url}\n")
                file.write(f"İçerik: {content}\n")
            
            with open("kontrol.txt", "r", encoding="utf-8") as kontrol_file:
                stored_text = kontrol_file.read().strip()
                with open("son_haber.txt", "r", encoding="utf-8") as haber_file:
                    latest_text = haber_file.read().strip()
                    if stored_text != latest_text:
                        chat_id = -1001977190523  # Hedef chat ID (- ile başlamalı)
                        context.bot.send_message(chat_id=chat_id, text=f"Yeni içerik:\n{latest_text}")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("site", site))
    dp.add_handler(CommandHandler("youtube", video))

    # Her 10 saniyede bir haber kontrolünü yap
    job_queue = updater.job_queue
    job_queue.run_repeating(check_and_send_message, interval=10, first=0)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
