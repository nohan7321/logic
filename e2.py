import threading
import time


# Define the function you want to run in a separate thread
def process_item(item):
    time.sleep(item)
    print("Thread: Processing item " + str(item))


# Create a list of items
item_list = [5, 5, 1, 4, 1]

# Create Thread objects for each item in the list
threads = []

for item in item_list:
    thread = threading.Thread(target=process_item, args=(item,))
    threads.append(thread)

# Start all the threads
for thread in threads:
    thread.start()

# Wait for all the threads to finish
for thread in threads:
    thread.join()

print("All threads have finished.")
