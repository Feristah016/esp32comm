from flask import Flask, render_template, url_for, redirect, request
from threading import Thread
import requests
from datetime import datetime
from pytz import timezone
import json



app = Flask('')

@app.route('/', methods=['POST', 'GET'])
def home():
  print("home")
  return "yarak"


@app.route("/ozgurdengelen", methods=["POST", "GET"])
def ozgurdengelen():
  if request.method == "POST":

    bilgi = request.form["nm"]
    zaman = datetime.now().astimezone(timezone('Asia/Istanbul')).strftime("%d.%m.%y/%H:%M:%S")
    reqip = ""
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
      reqip = request.environ['REMOTE_ADDR']
    else:
      reqip = request.environ['HTTP_X_FORWARDED_FOR']

    listeicin = bilgi + "///" + zaman + "///" + reqip

    with open("ozgurdengelen.txt", "w") as f:
      f.write(bilgi)
    if bilgi != "nul":
      with open("ozgurdengelenall.txt", "a") as f:
        f.writelines(f"{listeicin}\n")

    return "kürek"

  else:
    with open("ozgurdengelen.txt", "r") as f:
      bilg = f.read()
      print(bilg)
    return bilg

@app.route("/merttengelen", methods=["POST", "GET"])
def merttengelen():
  if request.method == "POST":

    bilgi = request.form["nm"]
    zaman = datetime.now().astimezone(timezone('Asia/Istanbul')).strftime("%d.%m.%y/%H:%M:%S")
    reqip = ""
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
      reqip = request.environ['REMOTE_ADDR']
    else:
      reqip = request.environ['HTTP_X_FORWARDED_FOR']

    listeicin = bilgi + "///" + zaman + "///" + reqip

    with open("merttengelen.txt", "w") as f:
      f.write(bilgi)
    if bilgi != "nul":
      with open("merttengelenall.txt", "a") as f:
        f.writelines(f"{listeicin}\n")

    return "opp"

  else:
    with open("merttengelen.txt", "r") as f:
      bilg = f.read()
      print(bilg)
    return bilg


def run():
  print("run")
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  print("keep alive")
  t = Thread(target=run)
  t.start()

if __name__ == "__main__":
  print("if name")
  keep_alive()
