import sqlite3
import datetime

def diaMes():
  res = datetime.date.today().strftime("%d/%m")
  return res

def cadastrarData(data, desc):
  con = sqlite3.connect("data.db")
  cur = con.cursor()
  query = f"INSERT INTO datas VALUES ('{data}','{desc}');"
  ps = cur.execute(query)
  con.commit()

def deleteData(data):
  con = sqlite3.connect("data.db")
  cur = con.cursor()
  query = f"DELETE FROM datas WHERE data = '{data}';"
  ps = cur.execute(query)
  con.commit()
  
def consultarData(busca):
  con = sqlite3.connect("data.db")
  cur = con.cursor()
  query = f"SELECT * FROM datas WHERE data='{busca}';"
  ps = cur.execute(query)
  k = ps.fetchall()
  if len(k) == 0:
    return "Nada encontrado na database."
  else:
    for i in k:
      data = f"""
📆 DATA: {i[0]}
📝 DESCRIÇÃO: {i[1]}
"""
    return data