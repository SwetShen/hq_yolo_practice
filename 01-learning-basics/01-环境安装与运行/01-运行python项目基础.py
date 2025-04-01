# 变量、函数、类、循环、条件 ...

#  变量的定义
a = 1
b: int = 1  # 限制条件指定变量类型


# 函数
def add1(a: int, b: int):
    return a + b


async def add2(a: int, b: int):  # 异步线程调取方式（多线程并发）
    return a + b


# 类的创建方式
class MyObj(object):
    def __init__(self, a: int, b: int):
        super().__init__()
        # 将外部参数进行类的局部变量化
        self.a = a
        self.b = a

    # 类中的函数
    def add(self):
        # self 代表整个类的对象
        return self.a + self.b


obj = MyObj(1, 2)  # 新建对象
print(obj.a, obj.b)  # 针对属性进行调用
obj.add()  # 调用对象中的方法

# 循环 (遍历矩阵的第一个维度)
for i in range(10):  # i 从0迭代到9
    print(i)

for i in [1, 2, 3]:  # i 从1迭代到3
    print(i)

for i, fruit in enumerate(["apple", "banana", "pear"]):  # enumerate 遍历项配置下标
    print(i, fruit)

for i, fruit in zip([3, 2, 1], ["apple", "banana", "pear"]):  # zip可以将多个遍历项进行打包处理
    print(i, fruit)

#  条件语句
a = 2
b = 3
if a < b:
    print(f"{a} < {b}")
else:
    print(f"{a} >= {b}")

# 条件语句在实际开发中，还可以做对象空或者非空判断
obj = None
if obj:
    print("pbj 不为空 为True")
else:
    print("pbj 为空 为False")
# 列表为空
alist = []
if alist:
    print("alist 不为空 为True")
else:
    print("alist 为空 为False")
