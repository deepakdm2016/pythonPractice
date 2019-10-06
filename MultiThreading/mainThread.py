import threading

name=threading.current_thread().getName()
print("Main thread",name)

if threading.current_thread()==threading.main_thread():
    print("Executing main thread logic")
else:
    print("Executing other thread program")