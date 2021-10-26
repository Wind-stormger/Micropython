import esp
# import gc

print(gc.mem_alloc())#输出堆RAM字节数
print(gc.mem_free())#返回可用堆 RAM 的字节数
print(esp.flash_size())#读取FLASH的总大小