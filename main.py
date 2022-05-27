import os
import telebot

bot = TeleBot("5389338453:AAGP8XgZmZWh5Z_aRmhOCYOpKVBpWLUEEyE")

@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):

bot.reply_to(message, "Hello! I'm Hirusha Dulaj Test Bot. How can I help you?")
bot.polliing()
