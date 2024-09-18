import threading 
import queue 
 
q = queue.Queue() 
 
def producer(): 
    data = "Hello, World!" 
    q.put(data)
 
def consumer(): 
    data = q.get() 
    print(data) 

thread1 = threading.Thread(target=producer) 
thread2 = threading.Thread(target=consumer) 

# Start threads 
thread1.start() 
thread2.start() 
 
# Wait for threads to finish 
thread1.join() 
thread2.join() 

print("Main thread continues.") 