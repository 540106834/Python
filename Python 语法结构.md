# **Python语法结构（Syntax Structure）**
也就是 Python 程序的“骨架”。
下面我会用**系统结构图 + 示例代码**的方式，帮你快速掌握 Python 的整体语法框架。

---

#  一、Python 程序的总体结构

Python 程序一般由以下部分组成：

```
┌────────────────────────┐
│ 1️ 模块导入（import）   │
│ 2️ 全局变量 / 常量定义   │
│ 3️ 函数定义（def）      │
│ 4️ 类定义（class）       │
│ 5️ 主程序执行入口（main）│
└────────────────────────┘
```

 示例：

```python
# 1️ 模块导入
import os
import sys

# 2️ 全局变量
VERSION = "1.0"

# 3️ 函数定义
def greet(name):
    print(f"你好, {name}!")

# 4️ 类定义
class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print(f"大家好，我是 {self.name}")

# 5️ 主程序入口
if __name__ == "__main__":
    greet("小明")
    p = Person("小红")
    p.say_hi()
```

---

#  二、Python 基本语法结构（核心语法单位）

| 类型       | 关键词                      | 示例                                  |
| -------- | ------------------------ | ----------------------------------- |
| **注释**   | `#`、`""" """`            | `# 单行注释`；`"""多行注释"""`               |
| **变量赋值** | `=`                      | `x = 10`                            |
| **条件语句** | `if / elif / else`       | `if x > 0: print("正数")`             |
| **循环语句** | `for / while`            | `for i in range(5): print(i)`       |
| **函数定义** | `def`                    | `def add(a, b): return a + b`       |
| **类定义**  | `class`                  | `class Dog: pass`                   |
| **异常处理** | `try / except / finally` | 捕获错误                                |
| **导入模块** | `import / from`          | `import math`、`from os import path` |
| **返回值**  | `return`                 | 函数返回结果                              |
| **退出程序** | `exit()` 或 `sys.exit()`  | 结束运行                                |
| **空语句**  | `pass`                   | 占位用                                 |

---

#  三、控制结构（Control Structures）

### 1️ 条件判断

```python
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

---

### 2️ 循环结构

```python
for i in range(5):
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1
```

---

### 3️ 循环控制语句

```python
for i in range(10):
    if i == 3:
        continue  # 跳过本次
    if i == 8:
        break     # 提前结束
    print(i)
```

---

#  四、数据结构（Data Structures）

| 类型           | 示例                   | 描述      |
| ------------ | -------------------- | ------- |
| **字符串**      | `'hello'`, `"world"` | 文本类型    |
| **列表 list**  | `[1, 2, 3]`          | 有序可变集合  |
| **元组 tuple** | `(1, 2, 3)`          | 有序不可变集合 |
| **集合 set**   | `{1, 2, 3}`          | 无序不重复集合 |
| **字典 dict**  | `{"a": 1, "b": 2}`   | 键值对映射   |

---

#  五、函数结构（Function）

```python
def greet(name, age=18):
    """打印问候语"""
    print(f"你好 {name}, 你今年 {age} 岁。")
    return age + 1

next_age = greet("小明", 20)
```

---

#  六、类与对象（OOP 基本语法）

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} 在叫")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} 汪汪叫")

dog = Dog("旺财")
dog.speak()
```

---

#  七、异常与错误处理

```python
try:
    x = int(input("输入数字："))
    print(10 / x)
except ValueError:
    print("输入的不是数字！")
except ZeroDivisionError:
    print("不能除以 0！")
finally:
    print("程序结束")
```

---

#  八、模块化与导入

```python
# 文件：math_utils.py
def add(a, b):
    return a + b
```

```python
# 主程序
from math_utils import add
print(add(2, 3))
```

---

#  九、文件与输入输出

```python
# 写入文件
with open("data.txt", "w") as f:
    f.write("Hello Python")

# 读取文件
with open("data.txt", "r") as f:
    print(f.read())
```

---

#  十、主程序执行入口（标准结构）

```python
def main():
    print("程序主入口")

if __name__ == "__main__":
    main()
```

 当文件被直接运行时，`__name__ == "__main__"` 为 True；
被其他模块导入时则不会执行 `main()`。

---

#  总结（Python 语法结构总览）

| 分类         | 关键内容                                |
| ---------- | ----------------------------------- |
| **程序组织结构** | import → def/class → main           |
| **控制结构**   | if / for / while / break / continue |
| **函数结构**   | def + return                        |
| **类结构**    | class + self + 继承                   |
| **模块结构**   | import / from                       |
| **异常结构**   | try / except / finally              |
| **数据结构**   | list / dict / tuple / set           |
| **文件结构**   | with open() 读写文件                    |
| **执行结构**   | `if __name__ == "__main__":`        |


