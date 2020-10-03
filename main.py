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
