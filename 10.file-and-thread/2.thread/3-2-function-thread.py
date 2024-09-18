import threading 
 
def my_function(): 
    for i in range(5): 
        print(f"Function: {i}") 
 
# Create a thread using a function 
my_thread = threading.Thread(target=my_function) 
 
# Start the thread 
my_thread.start() 
 
# Wait for the thread to finish (optional) 
my_thread.join() 
 
print("Main thread continues.")