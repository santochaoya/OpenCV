# OpenCV
This is a tutorial of learning OpenCV with Python.

## 1. Indroduction

### 1. read an image  
`cv2.imread(filename, flag)`   
apply a filter of black image(default as full color image with alpha channel)   


**NOTES**: 
* IMREAD_GREYSCAL - 0
* IMREAD_COLOR - 1
* IMREAD_UNCHANGED - -1

cv2 used color with BGR, matplotlib used RGB, if an image read by cv2 and show by matplotlib with color, colors will be wrong.

### 2. save an image
`cv2.imwrite(filename, img, params=None)`

## 2. loading video source
### 1. read video file

`cap = cv2.VideoCapture(0)`   
0: the first camera in the system(you are watching now).
1: the second camera(ready to go) 

`cap.read()`
read video frame by frame

`cv2.cvtColor`change color to get a simpler frame

### 2. output video file
`cv2.VideoWriter_fourcc(*'DIVX')`   
specify video codec

* In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size video. X264 gives very small size video)
* In Windows: DIVX (More to be tested and added)
* In OSX: MJPG (.mp4), DIVX (.avi), X264 (.mkv).

`cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))`   
`20.0`: number of frame per second(fps)   
`(640, 480)`: size

## 3. Drawing
### 1. draw a line
`line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)`   
* pt1: where to start   
* pt2: where to end   
* color: cv2 use BGR

(Tips: in computer, you put more value of color, color will be more light)

### 2. draw a rectangle
`rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)`
* pt1: where to start, top left   
* pt2: where to end, bottom right   
* color: cv2 use BGR

### 3. draw a circle
`circle(img, center, radius, color, thickness=None, lineType=None, shift=None)`

### 4. draw a ploygon
an array of points, then close the ploygon
`polylines(img, pts, isClosed, color, thickness=None, lineType=None, shift=None)`   
### 5. write
1. specify the font
2. write
`putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None)`   
* `cv2.LINE_AA` attempted anti-aliasing