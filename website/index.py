# web stuff:
from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)
import hashlib

# elecric stuff:
from hw import handler

server_adress = "server.remy-moll.v6.rocks"
# server_ip = "192.168.178.54"
server_ip = "server.remy-moll.v6.rocks" # probably more stable than the above, which might change due to dhcpcd
handler = handler(server_ip, server_adress)

@app.route('/')
def index():
   templateData = {
      'heading' : "Start the MC-server here",
      "explanation" : explanation,
      "action_name" : 'activate',
      "action_dest" : "activate",
      "status" : status_text()
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
      'heading' : "Launching the server",
      "explanation" : ["A start-command was just sent to the server. It should be up in a short time. Refresh to see the status."],
      "action_name" : 'Reload',
      "action_dest" : "status",
      "status" : status_text()
   }
   return render_template('index.html', **templateData)


explanation = [
   "How it works:",
   "1. Click activate",
   "2. Give it a minute, just like for aternos",
   "3. Connect to " + server_adress
]

def status_text():
   status = handler.is_on()
   value = "🔴 Server not online yet."
   if status:
       value = "🟢 Server responding to ping. You should be able to connect."
   return value



if __name__ == '__main__':
   app.run(debug=False, port=80, host='::')
