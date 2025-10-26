def check_memory(memory):
    """根据内存使用率判断状态"""
    if memory > 40:
        return "⚠️ 内存高"
    else:
        return "✅ 内存正常"

# 获取系统内存
import psutil
memory_usage = psutil.virtual_memory().percent

# 调用函数判断
status = check_memory(memory_usage)
print(f"内存状态: {memory_usage}% {status}")
