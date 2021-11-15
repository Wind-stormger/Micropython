import esp,machine
# import gc
print("CPU frequency = {CPU}Mhz".format(CPU = machine.freq()/1000000))#输出当前 CPU 频率
print("RAM used = {RAM_used}KB".format(RAM_used = gc.mem_alloc()/1024))#输出已用 RAM 
print("RAM free = {RAM_free}KB".format(RAM_free = gc.mem_free()/1024))#输出可用 RAM 
#print("RAM total = {RAM_total}KB".format(RAM_total = ( gc.mem_free() + gc.mem_alloc() ) / 1024))
print("FLASH total = {FLASH_total}KB".format(FLASH_total = esp.flash_size()/1024))#输出 FLASH 的总容量