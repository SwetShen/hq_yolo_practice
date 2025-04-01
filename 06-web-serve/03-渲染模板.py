from flask import Flask
from flask import render_template

app = Flask(__name__)


# http://127.0.0.1:9000/
@app.route("/")
def hello():
    return render_template("index.html")



if __name__ == '__main__':
    # 启动服务器
    app.run(host="0.0.0.0", port=9000, debug=True)
