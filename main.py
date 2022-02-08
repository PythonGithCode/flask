from flask import Flask, request as rq
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
 socketio.run(app)

@app.route('/2/')
def mains():
 return "<iframe style=\"width: 100%; height: 100%; border: none;\" name=\"embedded_python_anywhere\" src=\"https://www.pythonanywhere.com/embedded3/\"></iframe>"

@app.route('/1/')
def new():
 return "<iframe style=\"width: 100%; height: 100%; border: none;\" name=\"embedded_python_anywhere\" src=\"https://www.pythonanywhere.com/gists/5ad1c19979e5228aa6f2ce97aa97365b/mine.py/ipython3/\"></iframe>"

@app.route('/')
def sokrect():
 e = """
<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js" integrity="sha512-q/dWJ3kcmjBLU4Qc47E4A9kTB4m3wuTY7vkFJDTZKjTs8jhyGQnaUrxa0Ytd0ssMZhbNua9hE+E7Qv1j+DyZwA==" crossorigin="anonymous"></script>
<script type="text/javascript" charset="utf-8">
 var socket = io();
 socket.connect("https://fooddude.pythonanywhere.com/");
 //alert("no");
 console.log("42069")
 socket.on('connect', function() {
  socket.emit('my event',
  {data: 'I\'m connected!'});
  //alert("go");
  console.log("69420")
 });
</script>
<a>sum texts</a>
"""
 return e

@app.route("/r/")
def rdc():
 return "<a>yes</a>"

#@socketio.on('message')
#def handle_message(message):
# send(message)

@socketio.on('json')
def handle_json(json):
 send(json, json=True)

#@socketio.on('my event')
#def handle_my_custom_event(json):
# emit('my response', json)

@socketio.on('message')
def handle_message(message):
 send(message, namespace='/')

@socketio.on('my event')
def handle_my_custom_event(json):
 emit('my response', json, namespace='/')



