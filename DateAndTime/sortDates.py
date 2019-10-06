from datetime import date
import time

startTime=time.perf_counter()
ldatesList=[]
d1=date(2019,11,6)
d2=date(2019,11,5)
d3=date(2017,10,5)

ldatesList.append(d1)
ldatesList.append(d2)
ldatesList.append(d3)

ldatesList.sort(key=None, reverse=False)

for i in ldatesList:
    time.sleep(2)
    print(i)

endTime=time.perf_counter()

print("ExecutionTime in seconds=",endTime-startTime)


