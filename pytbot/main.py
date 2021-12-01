import telebot
import re
from translate import Translator

mat = []
def CheckMat(message):
    for i in mat:
        if re.search(i, message.text.lower()):
            bot.send_message(message.chat.id, 'МатОфф Please')
            return "МатОфф Please"
    return "All is OK"

def Mention(message):
    if re.search(r'@all+', message.text):
        bot.reply_to(message, "@DavHovh\n@Serobyanhovhannes\n@razmiqayelyan\n@Supreme8Leader\n@ndovlatyan\n@Jinxed7")
        return True
    return "@all not found"

def PerevodTo(message):
    if re.search(r'@perevod+', message.text):
        if message.reply_to_message:
            translator= Translator(from_leng="en" ,to_lang="ru")
            translation = translator.translate(str(message.reply_to_message.text))
            bot.send_message(message.chat.id, translation)
    elif re.search(r'@translate+', message.text):
        if message.reply_to_message:
            translator= Translator(to_lang="en", from_leng="ru")
            translation = translator.translate(str(message.reply_to_message.text))
            bot.send_message(message.chat.id, translation)






bot = telebot.TeleBot("1553329494:AAGDbejXYwpz62B5sMfq8o6rIn1ABrrp3Z0")
@bot.message_handler(func=lambda message: True)
def echo_all(message):

    if message.reply_to_message:
        print(message.reply_to_message.text)
    PerevodTo(message)
    CheckMat(message)
    Mention(message)

bot.polling(none_stop=True)
