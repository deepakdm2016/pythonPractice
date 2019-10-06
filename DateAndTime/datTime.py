import time,datetime
eposchsec=time.time()
print(eposchsec)

t=time.ctime(eposchsec)
print(t)

dt=datetime.datetime.today()
print('Current date: {}/{}/{}'.format(dt.day,dt.month, dt.year))
print('Current date: {}:{}:{}'.format(dt.hour,dt.minute, dt.second))