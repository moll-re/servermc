from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)
import hashlib

server_adress = "remy-moll.selfhost.eu"


@app.route('/')
def index():
   templateData = {
      'title' : 'Server mc!',
      'heading' : "Start the MC-server here",
      "explanation" : "Here is how it works: 1. Click <ACTIVATE> -> 2. Wait a bit -> 3. On minecraft connect to " + server_adress,
      "action_name" : 'activate',
      "action_dest" : "activate",
      "status" : "🔴 Not started yet"
      }
   return render_template('index.html', **templateData)


@app.route("/activate/", methods=['POST'])
def activate_server():
   pw = request.form.get("pw")
   if hashlib.sha256(pw.encode("utf-8")).hexdigest() == "5ac152b6f8bdb8bb12959548d542cb237c4a730064bf88bbb8dd6e204912baad": # hash of my super secret password
      send_start_command()
      status = "🟡 Just started the PC."
   else:
      status = "Wrong password. Nothing happened"
   templateData = {
      'title' : 'Server mc!',
      'heading' : "Launching the server",
      "explanation" : "If the password is correct, the server should be booting right now.",
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
      "explanation" : "A start-command was just sent to the server. It should be up in a short time. Refresh to see the status.",
      "action_name" : 'Reload',
      "action_dest" : "status",
      "status" : get_status()
   }
   return render_template('index.html', **templateData)



def get_status():
   # perform network ping test here
   # do something else
   status = True
   value = "🔴 Server not online yet. Give it a little time..."
   if status:
      value = "🟢 Server should be ready now. Try to connect"
   
   return value


def send_start_command():
   #
   print("HEY HO")














if __name__ == '__main__':
   app.run(debug=True, port=80, host='0.0.0.0')


   