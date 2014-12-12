#!/usr/bin/python

from gevent import monkey; monkey.patch_all()

from flask import Flask
app = Flask(__name__)


from gevent.wsgi import WSGIServer
#from yourapplication import app

@app.route('/')
def hello_world():
  return 'Hello World!'

if __name__ == '__main__':
  http_server = WSGIServer(('', 5000), app)
  http_server.serve_forever()
#    app.run(debug=True)
