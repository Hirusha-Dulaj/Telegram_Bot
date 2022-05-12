import os
import telebot

bot = TeleBot("5389338453:AAGP8XgZmZWh5Z_aRmhOCYOpKVBpWLUEEyE")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello i'am a Bot")

@bot.message_handler(commands=["about"])
def send_message(message):
    bot.send_message(message,"bot developed by Hirusha Dulaj")

bot.polliing()