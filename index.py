import config
import telebot
import os
import sys
from selenium import webdriver

def take_screenshot(urls):
  DRIVER = 'chromedriver'
  driver = webdriver.Chrome(DRIVER)
  driver.get(url)
  element = driver.find_element_by_tag_name('body')
  element.screenshot("screenshot_full.png")
  driver.quit()

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
  bot.send_message(message.chat.id,'This bot can give you html code of the requested site :-)')

@bot.message_handler(content_types=['text'])
def lalala(message):
  if (message.text == 'Hello'):
    bot.send_message(message.chat.id, 'Hello Man')
  else:
    u = 'Your message was: '+str(message.text)+' :-)'
    bot.send_message(message.chat.id, u)
bot.polling(none_stop=True)
