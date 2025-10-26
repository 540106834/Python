好的，我们来做一个 **系统化的 Python 基础语法详解**，既讲概念，也结合实战运维/SRE应用，让你打好写监控脚本和告警系统的基础。

---

# 🐍 1. Python 基本数据类型

| 类型        | 示例            | 描述           | SRE 应用       |
| --------- | ------------- | ------------ | ------------ |
| 整数 int    | `a = 10`      | 整数类型         | CPU 使用率、计数器  |
| 浮点数 float | `b = 3.14`    | 带小数的数        | 内存占用率、响应时间   |
| 字符串 str   | `s = "node1"` | 文本           | 节点名、服务名、告警信息 |
| 布尔 bool   | `flag = True` | True / False | 服务状态、阈值判断    |
| 空值 None   | `x = None`    | 空占位          | API 返回无值时    |

**示例**

```python
cpu_usage = 88        # int
mem_usage = 65.5      # float
node_name = "node1"   # str
healthy = True        # bool
error_value = None    # None
```

---

# 🐍 2. 字符串操作

```python
s = "CPU Usage"
print(s.upper())           # 'CPU USAGE'
print(s.lower())           # 'cpu usage'
print(s[0:3])              # 'CPU'
print(f"{s}: {cpu_usage}%")  # f-string 格式化，'CPU Usage: 88%'
```

**SRE 实战**：生成飞书告警消息、日志内容。

---

# 🐍 3. 数学与逻辑运算

```python
x, y = 10, 3

# 算术
print(x + y, x - y, x * y, x / y, x // y, x % y, x ** y)

# 比较
print(x > y, x == y, x != y)

# 逻辑
print(x > 5 and y < 5)
print(x > 5 or y < 2)
print(not(x > y))
```

**SRE 实战**：指标比较、阈值判断。

---

# 🐍 4. 条件语句

```python
threshold = 80
if cpu_usage > threshold:
    print("⚠️ CPU 超标")
elif cpu_usage > 70:
    print("⚠️ CPU 较高")
else:
    print("✅ CPU 正常")
```

**SRE 实战**：阈值判断触发告警或记录正常日志。

---

# 🐍 5. 循环语句

### for 循环

```python
nodes = ["node1", "node2", "node3"]
for node in nodes:
    print(f"巡检节点: {node}")
```

### while 循环

```python
count = 0
while count < 5:
    print("检查次数:", count)
    count += 1
```

**SRE 实战**：批量巡检多个节点或服务状态。

---

# 🐍 6. 函数与模块

```python
def check_cpu(node, value, threshold=80):
    if value > threshold:
        return f"⚠️ {node} CPU {value}% 超阈值 {threshold}%"
    return f"✅ {node} CPU 正常"

print(check_cpu("node1", cpu_usage))
```

* 参数可有默认值、可变参数 `*args` / `**kwargs`
* 函数封装逻辑，提高复用性

**SRE 实战**：封装指标解析、告警触发逻辑。

---

# 🐍 7. 数据结构

### 列表 List

```python
cpu_values = [60, 72, 88]
cpu_values.append(90)
print(cpu_values[0])   # 60
```

### 元组 Tuple

```python
node_info = ("node1", "192.168.1.101")
```

### 字典 Dict

```python
metrics = {"node1": 88, "node2": 65}
print(metrics["node1"])  # 88
```

### 集合 Set

```python
nodes_set = {"node1", "node2", "node3"}
nodes_set.add("node4")
```

**SRE 实战**：存储节点列表、指标字典、告警历史缓存。

---

# 🐍 8. 文件操作与日志

```python
# 写入日志
with open("monitor.log", "a", encoding="utf-8") as f:
    f.write(f"Node1 CPU={cpu_usage}%\n")

# 读取日志
with open("monitor.log", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

**SRE 实战**：记录巡检结果和告警历史，便于审计。

---

# 🐍 9. 异常处理

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除零异常")
finally:
    print("巡检结束")
```

**SRE 实战**：处理 SSH / HTTP API / Shell 执行异常，保证脚本稳定。

---

# 🐍 10. 模块与第三方库

```python
import requests      # HTTP API
import paramiko      # SSH 自动化
import subprocess    # 本地 Shell 调用
import json          # JSON 数据解析
import yaml          # YAML 配置解析
import logging       # 日志管理
```

**SRE 实战**：构建自动化巡检和告警系统的基础。

---

# 🐍 11. 面向 SRE 的强化语法

| 功能           | 示例                                            |
| ------------ | --------------------------------------------- |
| HTTP API 调用  | `requests.get("http://prometheus/api")`       |
| SSH 批量执行     | `paramiko.SSHClient()`                        |
| 本地命令执行       | `subprocess.run("df -h", shell=True)`         |
| JSON/YAML 解析 | `data = json.loads(resp.text)`                |
| 日志管理         | `logging.basicConfig(filename="monitor.log")` |

**SRE 实战**：自动采集指标、判断阈值、触发告警。

---

### 🔹 核心理念

1. **模块化**：函数 + 模块，易扩展
2. **异常安全**：保证脚本长期稳定
3. **日志化**：记录操作和告警历史
4. **统一数据结构**：列表 / 字典 / JSON
5. **实战导向**：基础语法直接服务于指标采集、阈值判断、告警发送

---

我可以帮你整理一个 **Python 基础 + SRE 实战语法速查表**，直接用于写监控和告警脚本，包括：

* Prometheus / SSH / Shell 指标采集
* 阈值判断 + 告警
* 日志 + 报表处理

这样你几乎不用查文档就能写完整 SRE 脚本。

你希望我整理这个速查表吗？
