import threading 
import time
class MyThread(threading.Thread): 
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    # method auto-run of a thread
    def run(self): 
        print(f'Begin thread {self.name}')
        time.sleep(self.delay)
        print(f'End Thread {self.name}')        
 
# Create an instance of the custom thread class 
t1 = MyThread('Thread-1', 6)
t2 = MyThread('Thread-2', 4) 
 
# Start the thread 
t1.start() 
t2.start() 
# Wait for the thread to finish (optional) 
t1.join()
t2.join() 
 
print("Main thread continues.") 