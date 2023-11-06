import statistics
import math
import time
print("the value of pi is",math.pi)
second=time.time()
print("second since epoch (the pont where time bigins)=",second)
li=[1,2,3,3,2,2,2]
print("the average of list values is:",end="")
print(statistics.mean(li))
local_time=time.ctime(second)
print("local time:",local_time)