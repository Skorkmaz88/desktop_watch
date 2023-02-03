# importing the required packages
import pyautogui
import cv2
import numpy as np
import torch

model = torch.hub.load("ultralytics/yolov5", "yolov5l")
while True:

    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(img)
    print(results)
    # Write it to the output file

    # Optional: Display the recording screen
    # cv2.imshow("Live", frame)
    # Stop recording when we press 'q'
    # if cv2.waitKey(1) == ord("q"):
    #    break

