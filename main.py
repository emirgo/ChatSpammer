from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

count = 3

message = input("Please input a message: ")
while isinstance(message, str) != True:
    print("ERROR: Make sure you are inputting a valid text.")
    message = input("Please input a message: ")

while count > 0:
    print("Bombarding ", message, " in ", count, " seconds...", end="\r")
    time.sleep(1)
    count -= 1

for char in message:
    print(char)

'''
while count < 50:
    keyboard.press("<")
    keyboard.release("<")
    keyboard.press("3")
    keyboard.release("3")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    count += 1
'''