from flask import Flask

app = Flask(__name__)

@app.route("/") # https://example.com/
def index(): # You could name this whatever you want.
  return "<h1>Welcome to the first webpage.</h1>"

app.run(
  host = "0.0.0.0", # or 127.0.0.1
  port = 8080, # make sure this is a non privileged port
  debug = True # this will allow us to easily fix problems and bugs
)