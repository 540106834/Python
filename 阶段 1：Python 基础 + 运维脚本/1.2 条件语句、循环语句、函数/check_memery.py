# def check_memory(memory):
#     """根据内存使用率判断状态"""
#     if memory > 40:
#         return "⚠️ 内存高"
#     else:
#         return "✅ 内存正常"

# # 获取系统内存
# import psutil
# memory_usage = psutil.virtual_memory().percent

# # 调用函数判断
# status = check_memory(memory_usage)
# print(f"内存状态: {memory_usage}% {status}")

import random

cpu_usage = random.randint(50, 100)      # 50-100 的随机整数
mem_usage = random.uniform(30, 90)       # 30-90 的随机浮点数

print(f"CPU 使用率: {cpu_usage}%")
print(f"内存使用率: {mem_usage:.2f}%")
def check_cpu(cpu):
    """根据 CPU 使用率判断状态"""
    if cpu > 75:
        return "⚠️ CPU 高"
    else:
        return "✅ CPU 正常"
def check_memory(memory):
    """根据内存使用率判断状态"""
    if memory > 60:
        return "⚠️ 内存高"
    else:
        return "✅ 内存正常"
cpu_status = check_cpu(cpu_usage)
mem_status = check_memory(mem_usage)
print(f"CPU 状态: {cpu_status}")
print(f"内存状态: {mem_status}")