import cv2      
import pyautogui    
import ctypes
import numpy as np 
import time

# Get the screen size
user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

# print(width,height)
dim = (width, height)
f = cv2.VideoWriter_fourcc(*"mp4v")
output = cv2.VideoWriter("test3.mp4",f,30.0,dim)

# Record for 10 seconds
now_start_time = time.time()
dur = 10
end_time = now_start_time + dur

# Capture the screen
while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    output.write(frame)
    
    current_time = time.time()
    if current_time > end_time :
        break

# Release the Video writer
output.release()

# Destroy all the windows
print("---- END ----")