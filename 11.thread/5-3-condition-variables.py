import threading 
condition = threading.Condition() 
def thread1(): 
    with condition: 
        condition.wait() 
        print("Thread 1 woke up!") 
 
def thread2(): 
    with condition: 
        condition.notify() 

t1 = threading.Thread(target=thread1) 
t2 = threading.Thread(target=thread2) 

# Start threads 
t1.start() 
t2.start() 
 
# Wait for threads to finish 
t1.join() 
t2.join() 

print("Main thread continues.") 