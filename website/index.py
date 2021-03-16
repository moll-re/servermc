# web stuff:
from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)
import hashlib

# elecric stuff:
import time
from hw import handler
import os

server_adress = "server.remy-moll.v6.rocks"


@app.route('/')
def index():
   templateData = {
      'title' : 'Server mc!',
      'heading' : "Start the MC-server here",
      "explanation" : explanation,
      "action_name" : 'activate',
      "action_dest" : "activate",
      "status" : "🔴 Not started yet"
      }
   return render_template('index.html', **templateData)


@app.route("/activate/", methods=['POST'])
def activate_server():
   pw = request.form.get("pw")
   if hashlib.sha256(pw.encode("utf-8")).hexdigest() == "5ac152b6f8bdb8bb12959548d542cb237c4a730064bf88bbb8dd6e204912baad": # hash of my super secret password
      handler.turn_on()
      status = "🟡 Just started the PC."
      action_name = 'Reload '
      action_dest = "status"
      explanation = ["Everything going to plan..."]
   else:
      status = "Wrong password. Nothing happened."
      action_name = 'Try again'
      action_dest = "activate"
      explanation = ["Uh oh..."]

   templateData = {
      'title' : 'Server mc!',
      'heading' : "Launching the server",
      "explanation" : explanation,
      "action_name" : 'Reload',
      "action_dest" : "status",
      "status" : status
   }
   return render_template('index.html', **templateData)


@app.route("/status/", methods=['POST'])
def refresh_page():
   templateData = {
      'title' : 'Server mc!',
      'heading' : "Launching the server",
      "explanation" : ["A start-command was just sent to the server. It should be up in a short time. Refresh to see the status."],
      "action_name" : 'Reload',
      "action_dest" : "status",
      "status" : get_status()
   }
   return render_template('index.html', **templateData)



def get_status():
   # perform network ping test here
   # do something else
   hostname = "192.168.178.29"
   response = os.system("ping -c 1 " + hostname)

   status = (response == 0)

   value = "🔴 Server not online yet. Give it a little time..."
   if status:
      value = "🟢 Server should be ready any second now. Try to connect"
   
   return value


explanation = [
   "How it works:",
   "1. Click_activate",
   "2. Give it a minute, just like for aternos",
   "3. Connect to " + server_adress
]


if __name__ == '__main__':
   app.run(debug=False, port=80, host='::')
