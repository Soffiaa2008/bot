from config import token
import telebot
import random


bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет. Я новый телеграм бот!
Я пока что нахожусь в стадии разработки, но все равно умею выполнять не много команд\
""")



@bot.message_handler(commands=['help'])
def welcome_help(message):
    bot.send_message(message.chat.id, 'чем я могу тебе помочь?')

@bot.message_handler(commands=['hello','hi','привет','приветик','хай','прив'])
def welcome_soo(message):
    bot.send_message(message.chat.id, 'привеет')

@bot.message_handler(commands=['coin'])
def coin(message):
    c=random.choice(["орел","решка"])
    bot.send_message(message.chat.id, c)

@bot.message_handler(commands=['info'])
def coin(message):
    bot.send_message(message.chat.id, "")

@bot.message_handler(content_types=["document"])
def content_document(message):
    bot.send_message(message.chat.id, 'оп оп, документик')



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)




bot.infinity_polling()

print(token)