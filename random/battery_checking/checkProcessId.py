import psutil

print(psutil.pids())

list = psutil.pids()
list_x = psutil._ppid_map()

# for x in list_x:
#     print(x)
