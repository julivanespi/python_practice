from datetime import date
import time

today = date.today()

i = 0
while i < 100:
    print(today)
    time.sleep(10)
    i += 1

print("Done")
