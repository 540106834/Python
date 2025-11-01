# **Python 类定义（class）** 
它是 Python 面向对象编程（OOP）的核心。

---

##  一、类（Class）的基本概念

在 Python 中：

> **类（class）** 是对象的模板，
> **对象（object）** 是类的实例。

类定义了一类对象的 **属性（数据）** 和 **方法（行为）**。

---

##  二、最基本的类定义语法

```python
class 类名:
    # 构造函数（初始化方法）
    def __init__(self, 参数列表):
        self.属性名 = 参数值  # 实例属性

    # 实例方法
    def 方法名(self, 参数):
        执行语句
```

###  示例：

```python
class Person:
    # 构造方法（初始化）
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def say_hello(self):
        print(f"大家好，我是 {self.name}，今年 {self.age} 岁。")

# 创建对象（实例化）
p1 = Person("小明", 18)
p1.say_hello()
```

输出：

```
大家好，我是 小明，今年 18 岁。
```

---

##  三、类中常用的成员类型

| 成员类型     | 说明                           | 示例                           |
| -------- | ---------------------------- | ---------------------------- |
| **实例属性** | 每个对象独有的属性                    | `self.name = "小明"`           |
| **类属性**  | 所有对象共享的属性                    | `species = "Human"`          |
| **实例方法** | 操作实例数据                       | `def run(self): ...`         |
| **类方法**  | 操作类级数据，用 `@classmethod` 修饰   | `def show_species(cls): ...` |
| **静态方法** | 不依赖实例或类，用 `@staticmethod` 修饰 | `def greet(): ...`           |

---

##  四、完整示例（实例属性 + 类属性 + 方法）

```python
class Person:
    # 类属性（所有实例共享）
    species = "Human"

    # 初始化方法（构造函数）
    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age

    # 实例方法
    def introduce(self):
        print(f"我是 {self.name}，今年 {self.age} 岁。")

    # 类方法
    @classmethod
    def show_species(cls):
        print(f"我们都是 {cls.species}")

    # 静态方法
    @staticmethod
    def greet():
        print("你好！这是一个静态方法。")

# 使用
p = Person("小明", 20)
p.introduce()

Person.show_species()
Person.greet()
```

输出：

```
我是 小明，今年 20 岁。
我们都是 Human
你好！这是一个静态方法。
```

---

##  五、类的继承（Inheritance）

> Python 支持单继承和多继承。

###  单继承：

```python
class Animal:
    def speak(self):
        print("动物在叫")

class Dog(Animal):
    def speak(self):
        print("汪汪汪！")

dog = Dog()
dog.speak()
```

输出：

```
汪汪汪！
```

---

###  调用父类方法：

```python
class Animal:
    def speak(self):
        print("动物在叫")

class Dog(Animal):
    def speak(self):
        super().speak()   # 调用父类方法
        print("狗在叫")

Dog().speak()
```

输出：

```
动物在叫
狗在叫
```

---

##  六、封装（Encapsulation）

通过 **私有属性** 和 **getter/setter** 保护内部数据：

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance  # 私有属性（外部无法直接访问）

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

a = Account(100)
a.deposit(50)
print(a.get_balance())  # ✅ 150
# print(a.__balance)    # ❌ 报错（无法直接访问）
```

---

##  七、类的特殊方法（Magic Methods）

Python 内置许多以 `__双下划线__` 开头的特殊方法：

| 方法         | 作用       | 示例               |
| ---------- | -------- | ---------------- |
| `__init__` | 构造函数     | 初始化对象            |
| `__str__`  | 对象转字符串   | `print(obj)` 时调用 |
| `__repr__` | 调试用字符串表示 | `repr(obj)`      |
| `__len__`  | 对象长度     | `len(obj)`       |
| `__add__`  | 加法重载     | `obj1 + obj2`    |
| `__eq__`   | 判断相等     | `obj1 == obj2`   |

 示例：

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"《{self.title}》有 {self.pages} 页"

b = Book("Python入门", 300)
print(b)
```

输出：

```
《Python入门》有 300 页
```

---

##  八、类与模块结合使用

你可以把类定义放在独立文件中，并导入使用：

```python
# 文件：models.py
class User:
    def __init__(self, name):
        self.name = name
```

```python
# main.py
from models import User
u = User("小红")
print(u.name)
```

---

##  九、总结

| 分类          | 内容                                 | 关键词     |
| ----------- | ---------------------------------- | ------- |
| **定义类**     | `class 类名:`                        | class   |
| **构造方法**    | `def __init__(self):`              | 初始化对象   |
| **实例属性**    | `self.attr`                        | 每个对象独有  |
| **类属性**     | `类名.attr`                          | 所有对象共享  |
| **实例方法**    | `def func(self):`                  | 操作实例    |
| **类方法**     | `@classmethod` + `cls`             | 操作类     |
| **静态方法**    | `@staticmethod`                    | 独立逻辑    |
| **继承**      | `class 子类(父类):`                    | 复用与扩展   |
| **super()** | 调用父类方法                             | super() |
| **私有属性**    | `__attr`                           | 封装内部数据  |
| **魔术方法**    | `__init__`, `__str__`, `__len__` 等 | 特殊行为    |

