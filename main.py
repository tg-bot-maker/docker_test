from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world!!"


@app.route("/opa")
def opa():
    return "Hello buddy!!"


@app.route("/get_ip")
def get_ip():
    return request.remote_addr
    



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)