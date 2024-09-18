import threading 
def main(): 
    print("This is the main thread.") 
 
if __name__ == "__main__": 
    main_thread = threading.main_thread() 
    print(f"Main thread name: {main_thread.name}") 
    main() 
# Main thread name: MainThread
# This is the main thread