#context manager 
import os

class ChangeDirectoryContextManager:
    def __init__(self, new_directory):
        self.new_directory = new_directory
        self.previous_directory = None

    def __enter__(self):
        # Save the current directory
        self.previous_directory = os.getcwd()

        # Change to the new directory
        os.chdir(self.new_directory)
        print(f"Changed directory to: {self.new_directory}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Change back to the previous directory
        os.chdir(self.previous_directory)
        print(f"Changed directory back to: {self.previous_directory}")

# Example usage
with ChangeDirectoryContextManager("my_directory"):
    # Perform operations within the new directory
    print("Current directory:", os.getcwd())
    # ... additional operations ...

# Outside the context, we are back to the original directory
print("Current directory:", os.getcwd())

# Multithreading

import threading
import time

def task(name):
    print(f"Task '{name}' started.")
    time.sleep(2)  # Simulate some work
    print(f"Task '{name}' completed.")

# Create multiple threads
threads = []
for i in range(3):
    t = threading.Thread(target=task, args=(f"Thread {i+1}",))
    threads.append(t)

# Start the threads
for t in threads:
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All tasks completed.")




#multiprocessing
import multiprocessing
import time

def task(name):
    print(f"Task '{name}' started.")
    time.sleep(2)  # Simulate some work
    print(f"Task '{name}' completed.")

# Create a pool of worker processes
pool = multiprocessing.Pool(processes=3)

# Submit tasks to the pool
for i in range(3):
    pool.apply_async(task, args=(f"Process {i+1}",))

# Close the pool to indicate no more tasks will be submitted
pool.close()

# Wait for all tasks to complete
pool.join()

print("All tasks completed.")
