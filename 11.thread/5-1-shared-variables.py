import threading 
 
shared_var = 0 
lock = threading.Lock() 
 
def increment():
    global shared_var
    for _ in range(100000):
        with lock:
            shared_var += 1  # Safe modification with a lock

 
def decrement():
    global shared_var
    for _ in range(100000):
        with lock:
            shared_var -= 1   # Safe modification with a lock


# Create threads
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=decrement)

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()


print("Final shared_var:", shared_var)