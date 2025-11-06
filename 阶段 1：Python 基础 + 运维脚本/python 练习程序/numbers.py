import psutil

cpu = psutil.cpu_percent(interval=1)

if cpu < 50:
    print("CPU 使用正常")
elif cpu < 80:
    print("CPU 使用偏高")
else:
    print("CPU 使用过高，注意告警")

print(f"当前CPU使用率: {cpu}%")
