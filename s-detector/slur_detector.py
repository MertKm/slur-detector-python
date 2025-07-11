#!/usr/bin/python3(venv)
# Sensitive content: slurs written in the script. 
# python script programmed to detect slurs via (!)keylogger and start functions.

try:
    import threading
    import os
    import subprocess
    import sys
    from datetime import datetime
    from pynput import keyboard 
except ModuleNotFoundError:
    from subprocess import call
    modules = ["pynput"]
    call("pip install" + ''.join(modules), shell=True)


# colors
black = "\x1b[30m"
red = "\x1b[31m"
green = "\x1b[32m"
yellow = "\x1b[33m"
blue = "\x1b[34m"
gray = "\x1b[38m"
# styles
reset = "\x1b[0m"
bold = "\x1b[1m"

COLOR = {
    'enter': red + bold,
    'space': yellow,
    'ctrl_l': blue,
    'ctrl_r': blue,
    'shift': green,
    'shift_r': green,
    'alt_l': gray,
    'alt_r': gray,
    'esc': red,
    'backspace': red + bold,
}


typed_buffer = ""

# functions for triggers here:
def punish0():
    photo_path = os.path.join("photos", "cokayib.jpg")    
    if os.name == "posix":
        subprocess.Popen(['xdg-open', photo_path])
    elif os.name == "nt":
        os.startfile(photo_path)
    
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    warning = "don't say racial slurs again >:("
    full_warning = f"[{timestamp}] {warning}"
    print(warning)
    with open("slur_logs.txt", "a") as file:
        file.write("".join(full_warning) + "\n")

def punish1():
    photo_path = os.path.join("photos", "shhh.png")
    if os.name == "posix":
        subprocess.Popen(['xdg-open', photo_path])
    elif os.name == "nt":
        os.startfile(photo_path)
    
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    warning = "don't say bad words again :("
    full_warning = f"[{timestamp}] {warning}"
    print(warning)
    with open("slur_logs.txt", "a") as file:
        file.write("".join(full_warning) + "\n")

def punish2():
    photo_path = os.path.join("photos", "sus.jpg")
    if os.name == "posix":
        subprocess.Popen(['xdg-open', photo_path])
    elif os.name == "nt":
        os.startfile(photo_path)
    
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    warning = "amongus?"
    full_warning = f"[{timestamp}] {warning}"
    print(warning)
    with open("slur_logs.txt", "a") as file:
        file.write("".join(full_warning) + "\n")
    


## WARNING: there will be the slur words or the things we don't want the user to say. 
## this section may be sensitive for some people. Be cautious. 

# you can change this part however you want.

trigger_actions = {            

    ## FILL FHIS PLACE WITH WHATEVER YOU WANT.
    # for example: 
    # "slur1": punish0

}


def kill_trigger(word):
    action = trigger_actions.get(word)
    if action:    
        action()

def color_print(text, color):
    print(f"{color}{text}{reset}", end="", flush=True)


def on_press(key):
    global typed_buffer

    try:
        char = key.char
        typed_buffer += char
        color_print(char, green)
    except AttributeError:
        key_name = key.name
        color_code = COLOR.get(key_name.lower(), blue)
        text = f"[{key_name}]"

        
        if key_name == "space":
            typed_buffer += " "
        elif key_name == "enter":
            typed_buffer += "\n"
        elif key_name == "backspace":
            typed_buffer = typed_buffer[:-1]

        color_print(text, color_code)

    
    for word, func in trigger_actions.items():
        if word in typed_buffer:
            func()
            typed_buffer = ""  

try:   
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()    
except KeyboardInterrupt:
    print("\n\nPressed CTRL-C, stopping keylogger.\n\n")


