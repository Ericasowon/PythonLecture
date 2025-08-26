# Goal
# Get the current time (time.strftime)
# Update and display it on the screen every second


import time
import os

print("⏰ Digital Clock Program")

try:
    while True:
        now = time.strftime("%Y-%m-%d %H:%M:%S")  # current time
        os.system("cls" if os.name == "nt" else "clear")  # clear screen
        print("Current time:", now)
        time.sleep(1)  # wait 1 second
except KeyboardInterrupt:
    print("\n🛑 Clock stopped.")
