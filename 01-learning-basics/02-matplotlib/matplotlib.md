# matplotlib

> 数据科学可视化工具
>
> matplotlib 库继承自`numpy`



参与：[Matplotlib — Visualization with Python](https://matplotlib.org/)

> 软件开发体系务必参照官方的文档，否则容易出现兼容问题

学习思路，主要通过快速指引：[Quick start guide — Matplotlib 3.10.1 documentation](https://matplotlib.org/stable/users/explain/quick_start.html)



按照如下图进行学习

<img src="./assets/image-20250305194810907.png" alt="image-20250305194810907" style="zoom:50%;" />



库安装问题：

‌**pip设置下载源可以通过以下几种方法实现**‌：

1. ‌**使用pip命令直接设置**‌：在命令行中运行以下命令，可以直接设置默认的下载源。例如，将pip的默认下载源设置为清华大学的镜像源：

   ```
   pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
   ```
   
   类似地，可以将下载源设置为阿里云、中科大、豆瓣等其他国内源。‌12
   
2. ‌**编辑pip配置文件**‌：pip的配置文件默认存储在用户的主目录下的特定位置。在Windows系统中，它通常位于`C:\Users\用户名\.pip\pip.ini`；在Linux和macOS系统中，它通常位于`\~/.pip/pip.conf`。打开配置文件，在[global]部分下添加或修改index-url选项，将其设置为你想要的镜像源地址。例如：

   ```
   index-url = https://pypi.tuna.tsinghua.edu.cn/simple
   ```
   
   保存配置文件并退出编辑器。
   
3. ‌**设置环境变量**‌：在某些情况下，也可以通过设置环境变量来修改pip的默认下载源。但这种方法不如直接编辑配置文件或使用pip命令来得直接和方便。‌1

‌**常用的国内源包括**‌：

- ‌**[清华大学镜像源](https://www.baidu.com/s?word=清华大学镜像源&sa=re_dqa_generate)**‌：https://pypi.tuna.tsinghua.edu.cn/simple
- ‌**[阿里云镜像源](https://www.baidu.com/s?word=阿里云镜像源&sa=re_dqa_generate)**‌：https://mirrors.aliyun.com/pypi/simple
- ‌**[中科大镜像源](https://www.baidu.com/s?word=中科大镜像源&sa=re_dqa_generate)**‌：https://pypi.mirrors.ustc.edu.cn/simple
- ‌**[豆瓣镜像源](https://www.baidu.com/s?word=豆瓣镜像源&sa=re_dqa_generate)**‌：http://pypi.douban.com/simple。‌34

‌**验证配置是否生效**‌：可以通过以下命令查看当前配置信息：
