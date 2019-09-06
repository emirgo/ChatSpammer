from pynput.keyboard import Key, Controller
import time
import os

# Cross-platform console clear function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Keyboard controller
keyboard = Controller()

# Grace period before user clicks on the message box
time_count = 3 

# Asking for input, which is message we will send
message = input("Please input a message: ")
while isinstance(message, str) != True:
    print("ERROR: Make sure you are inputting a valid text.")
    message = input("Please input a message: ")

# Clear console
clear()

# Asking for input, how many messages to send
message_count = int(input("Please input amount of messages to send: "))
while isinstance(message_count, int) != True:
    print("ERROR: Make sure you are inputting a valid number.")
    message_count = input("Please input amount of messages to send: ")

# Grace period
while time_count > 0:
    print("Bombarding ", message, " in ", time_count, " seconds...", end="\r")
    time.sleep(1)
    time_count -= 1

# Clear console
clear()

# Main loop
count = 0
while message_count > count:        
    for char in message:
        keyboard.press(char)
        keyboard.release(char)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    count += 1
    print("Sent ", count, " messages", end="\r")
    
print("Sent ", count, " messages.")
print("Done!")