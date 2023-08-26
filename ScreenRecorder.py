import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time
dur=eval(input("Enter the duration of the screenrecord: "))
name=input("Enter the name of the output file: ")
width= GetSystemMetrics(0)
height=GetSystemMetrics(1)
dim=(width,height)
f=cv2.VideoWriter_fourcc(*"XVID")
result=cv2.VideoWriter(f"{name}.mp4",f,30.0,dim)
start_time=time.time()
end_time=start_time+dur
while True:
    img=pyautogui.screenshot()
    frame=np.array(img)
    frame1=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result.write(frame1)
    current_time=time.time()
    if current_time > end_time:
        break
result.release()
print("Your Recording has stopped")
print("File Saved Successfully")