import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import logging
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import sys
import io



scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name("path\\Valued-rigging-423011-p9-19d5f63df9b7.json",scopes=scopes)

file = gspread.authorize(creds)
Workbook = file.open("Viber_Automation")
# sheet3 = Workbook.sheet3
sheet3 = Workbook.get_worksheet(2)  # Get the third sheet (index starts at 0
print("Data from google-sheet are recorded!!")
data = sheet3.get_all_records()



# API_TOKEN = '7180158082:AAGp4O5QF5an6yxJvb8gBVu7zvA54XfoizI'
API_TOKEN = 'Token from botfather'
extra = ["https://t.me/channel1", "https://t.me/channel1","https://t.me/channel2","https://t.me/channel3"]

# Generating Channel links
bot = telebot.TeleBot(API_TOKEN)
links = ["https://t.me/channel1"]

option_s = [
    ["Channel linkတောင်းမယ်။"],
]

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#Configure logging
logging.basicConfig(level=logging.INFO, filename='bot_conversation.log', filemode='a', encoding='utf-8',format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


for row in option_s:
    keyboard.add(*[KeyboardButton(option) for option in row])

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])  # /start
def send_welcome(message):
    random_link = random.choice(links)
    logging.info(f"User: {message.from_user.first_name} ({message.from_user.id}) sent /start command")
    logging.info(f"Bot: {random_link}")
    bot.reply_to(message, f"""အရေးပေါ်လူမှုကယ်ဆယ်ရေးအတွက် ဝင်ရောက်အကူညီတောင်းခံနိုင်ရန် 
                အောက်ပါ hotline Channel ကို သွားပေးပါ => {random_link}""")

@bot.message_handler(commands=['help'])  # /help
def send_help(message):
    random_link = random.choice(links)
    logging.info(f"User: {message.from_user.first_name} ({message.from_user.id}) sent /help command")
    logging.info(f"Bot: {random_link}")
    bot.reply_to(message, f"""/start ကိုနှိပ်၍ အကူညီများတောင်းခံနိုင်ပါတယ်\nအရေးပေါ်ကယ်ဆယ်ရေးအတွက် ၁ ကိုနှိပ်ပါ။\n ငွေကြေးအထောက်ပံ့လိုအပ်ပါက ၂ ကိုနှိပ်ပါ။""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
# Intelligent
def Server_Online(message):
    random_link = random.choice(links)
    if '၁' in message.text:  # Client ဘက်ကပို့တဲ့စာထဲ ဒီစာပါလာရင်
        logging.info(f"User: {message.from_user.first_name} ({message.from_user.id}) sent '{message.text}'")
        logging.info(f"Bot: {random_link}")
        bot.reply_to(message, f"""စိတ်ကိုတည်တည်ငြိမ်ငြိမ်ထားပေးပါ။ လက်ရှိရောက်ရှိတာနေရာနှင့်လိုအပ်သောအကူညီကို ‌ေအာက်ပါအကောင့်မှာပြောပေးပါ => {random_link}""")  # ဒါကိုဖြေပေးပါ
    elif '၂' in message.text:
        logging.info(f"User: {message.from_user.first_name} ({message.from_user.id}) sent '{message.text}'")
        logging.info(f"Bot: {random_link}")
        bot.reply_to(message, f"""စိတ်ကိုတည်တည်ငြိမ်ငြိမ်ထားပေးပါ။ လက်ရှိရောက်ရှိတာနေရာနှင့်လိုအပ်သောအကူညီကို ‌ေအာက်ပါအကောင့်မှာပြောပေးပါ => {random_link}""")
    else:
        bot.reply_to(message, f"""စိတ်ကိုတည်တည်ငြိမ်ငြိမ်ထားပေးပါ။ လက်ရှိရောက်ရှိတာနေရာနှင့်လိုအပ်သောအကူညီကို ‌ေအာက်ပါအကောင့်မှာပြောပေးပါ => {random_link}""")
        #user phone number
        try:
         user_phone = message.contact.phone_number  # This requires the user to send their contact info
        except AttributeError:
         user_phone = "Not provided"
        #user acc link
        user_username = message.from_user.username
        user_link = f"https://t.me/{user_username}" if user_username else "Username not set"
        logging.info(f"User: {message.from_user.first_name} {message.from_user.last_name} user_acclink->{user_link} ({message.from_user.id}) was sent: {message.text} and his ph-no:{user_phone}")
        logging.info(f"Bot: {random_link}")

bot.infinity_polling()