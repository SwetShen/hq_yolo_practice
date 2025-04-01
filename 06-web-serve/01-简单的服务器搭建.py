from flask import Flask

# 构建flask微服务应用
app = Flask(__name__)  # __name__ 主线程名称


# 以下路由的访问地址： http://127.0.0.1:9000/
@app.route("/")  # 默认网页路由
def hello():
    return "<h1 style='color:red;'>这是我的第一个网页</h1>"  # h1 标签是网页中的标题区域


if __name__ == '__main__':
    # 启动服务器
    # http://127.0.0.1:9000 只能在自己的电脑中访问
    # app.run(host="127.0.0.1", port=9000, debug=True)
    # http://localhost:9000 只能在自己的电脑中访问
    # app.run(host="localhost", port=9000, debug=True)
    # http://10.120.4.58:9000 可以让内容在局域网中访问
    # app.run(host="10.120.4.58", port=9000, debug=True)
    # http://127.0.0.1:9000 或者 http://10.120.4.58:9000
    app.run(host="0.0.0.0", port=9000, debug=True)
    # http://公共的IP地址:9000 可以让内容在整个网络都可以访问
    # app.run(host="公共的IP地址", port=9000, debug=True)
