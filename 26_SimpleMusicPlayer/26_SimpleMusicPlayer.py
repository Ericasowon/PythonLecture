# Goal
# Load music file (pygame.mixer.music.load)
# Play / Stop / Pause functionality
# Control with a simple menu


import pygame

# Initialize pygame
pygame.mixer.init()

print("🎵 Simple Music Player")
print("Enter the music file name (e.g., music.mp3):")
filename = input("> ")

try:
    pygame.mixer.music.load(filename)  # Load music file
    print("✅ Music loaded successfully!")
except:
    print("⚠ Could not load the music file. Make sure the mp3 file exists in the same folder.")
    exit()

while True:
    print("\nMenu: 1. Play  2. Pause  3. Resume  4. Stop  5. Exit")
    choice = input("Select: ")

    if choice == "1":
        pygame.mixer.music.play()
        print("▶ Playing music...")
    elif choice == "2":
        pygame.mixer.music.pause()
        print("⏸ Music paused")
    elif choice == "3":
        pygame.mixer.music.unpause()
        print("▶ Music resumed")
    elif choice == "4":
        pygame.mixer.music.stop()
        print("⏹ Music stopped")
    elif choice == "5":
        pygame.mixer.music.stop()
        print("👋 Exiting program.")
        break
    else:
        print("⚠ Invalid input.")
