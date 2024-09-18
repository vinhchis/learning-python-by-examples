# Program, process, thread and multi-threads
## Program
    - contains code or a set of processor instructor
    - stored in disk
    - firefox.exe, run.bat, hello.py,...

# Process
> `process` - when the code in program is loaded into memory(RAM) and executed by processor

    - resources (CPU,RAM) manager by I/O
    - part of a process(4):
        - Process registers
        - Program counters
        - Stack pointers
        - Memory pages
        - ...
    - Property of process:
        - Code
        - Data
        - Heap
        - Stack
    - One process cannot corrupt the memory space of another process => independent
    - example: a tab chrome is a process

## threads
> thread - the unit of execution within a process

    - a process has at least one thread (main thread)
    - part of a thread(3):
        - Stack
        - Registers
        - Program counters
## multi-threads

    - threads in a process use :
        - sharing memory space (Heap)
        - can use global variables and heap of process
    - a misbehaving(không đúng) could bring down entire process

# OS run a thread or process in CPU
    
> context switch - handled run threads (saving and reloading), importance body is PCB 

> `PCB` - Process Control BLock
    - process state
    - process number
    - process counter
    - register
    - memory limits
    - list of open files
    - ...


1.Thách thức:
- Đồng bộ hóa: Cần quản lý truy cập vào tài nguyên chia sẻ để tránh xung đột.
- Deadlocks: Có thể xảy ra khi các threads chờ đợi lẫn nhau.
- Khó gỡ lỗi: Lỗi trong môi trường đa luồng thường khó tái tạo và sửa chữa.


1 write, 1 read -> raise condition

 
7 ngài hiền triết và 7 chiếc đũa


# parallelism vs Concurrency

thread lock