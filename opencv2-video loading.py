import cv2
import numpy as np
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# if camera is not open
if not cap.isOpened():
    print('There is no camera.')
    exit()

while True:
    ret, frame = cap.read()

    #if read video is correct
    if not ret:
        print('Can\'t receive frame. Existing...')
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()