import threading 

def worker_thread(thread_id): 
    print(f"Thread {thread_id} started.") 
    # Your task code here 
    print(f"Thread {thread_id} finished.") 
 
# Create thread objects 
thread1 = threading.Thread(target=worker_thread, args=(1,)) 
thread2 = threading.Thread(target=worker_thread, args=(2,)) 
 
# Start threads 
thread1.start() 
thread2.start() 
 
# Wait for threads to finish 
thread1.join() 
thread2.join() 
 
print("Main thread continues.") 