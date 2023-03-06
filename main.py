import telebot 
import data
import threading
import datetime
from datetime import date
import notifica
from notifica import notify
from data import cadastrarData, consultarData, diaMes

s = threading.Thread(target=notify, args=()).start()

bot = telebot.TeleBot('6166265163:AAF1bsNZbTgR6lfR4Ev2hGpApxBdXDFTn44',parse_mode="markdown")

@bot.message_handler(commands=["buscar"])
def buscar(message):
  r = message.text.split()[1]
  search = consultarData(r)
  bot.reply_to(message, search)
  
@bot.message_handler(commands=["cadastrar"])
def cadastrar(message):
  r = message.text.split()[1]
  r2 = message.text.split()[2]
  print(r2)
  cad = cadastrarData(r, r2)
  success = f"""
*=> Data cadastrada com sucesso!*

*Dia*: `{r}`
*Descrição*: `{r2}`

_No dia {r} irei enviar o lembrete no chat._
  """
  bot.reply_to(message, success)
  
@bot.message_handler(commands=["hoje"])
def hoje(message):
  data_atual = diaMes()
  bot.reply_to(message, data_atual)

bot.polling()