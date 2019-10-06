from threading import Thread

class myThread(Thread):
    def run(self):
        for i in range(2,10):
            print(i)
            

t=myThread()
t.start()
        