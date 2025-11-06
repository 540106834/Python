# 定义两个布尔变量 `x=True`，`y=False`，输出：

#    * `x and y`
#    * `x or y`
#    * `not x`


x = True
y = False  

print("x and y =", x and y)
print("x or y =", x or y)   
print("not x =", not x)

# 判断变量 `num=10` 是否为正数，并打印 `"正数"` 或 `"非正数"`。

num = -10
if num > 0:
    print("正数")
else:
    print("非正数")

d = {"name": "Alice", "age": 25}

# 通过键访问值
print(d["name"])  # Alice

# 使用 get() 方法，键不存在时返回 None 或默认值
print(d.get("city"))         # None
print(d.get("city", "Tokyo")) # Tokyo