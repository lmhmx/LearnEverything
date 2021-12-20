import os
import time
command = "git push"
result = 1
start_time = time.time()
while(result!=0):
    result = os.system(command)
    print("time {:5.2f} result {:10d} ".format(time.time()-start_time,result))
    time.sleep(3)
    