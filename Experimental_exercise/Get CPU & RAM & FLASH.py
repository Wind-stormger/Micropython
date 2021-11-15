import esp,machine
# import gc
print(machine.freq())#输出当前 CPU 频率
print(gc.mem_alloc())#输出已用 RAM 字节数
print(gc.mem_free())#输出可用 RAM 字节数
print(esp.flash_size())#读取 FLASH 的总大小
