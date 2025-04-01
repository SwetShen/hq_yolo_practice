from flask import Flask

app = Flask(__name__)


# http://127.0.0.1:9000/hello
@app.route("/hello")
def hello():
    return "<h1 style='color:red;'>You say hello</h1>"


# http://127.0.0.1:9000/hi
@app.route("/hi")
def hi():
    return "<h1 style='color:red;'>hi,nice to meet you</h1>"


if __name__ == '__main__':
    # 启动服务器
    app.run(host="0.0.0.0", port=9000, debug=True)
