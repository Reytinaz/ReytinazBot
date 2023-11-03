#from flask import Flask
#from threading import Thread

#app = Flask('')

#@app.route('/')
#def home():
#  return "Hello!"

#def run():
#  app.run(host='0.0.0.0',port=8080)

#def keep_alive():
#  t = Thread(target=run)
#  t.start()
from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World</p>"


if __name__ == '__main__':
    http_server = WSGIServer(("127.0.0.1", 8080), app)
    http_server.serve_forever()