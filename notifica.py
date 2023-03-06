import time
import data
import requests
import datetime
import telebot
from data import consultarData, deleteData

bot = telebot.TeleBot('6166265163:AAF1bsNZbTgR6lfR4Ev2hGpApxBdXDFTn44',parse_mode="markdown")

def notify():
  while True:
    time.sleep(6)
    data = datetime.date.today().strftime("%d/%m")
    s = consultarData(data)
    if "Nada" in s:
      r = f"[{data}] - Nada encontrado."
      print(r)
    else:
      bot.send_message(-1001577196038, s)
      deleteData(data)