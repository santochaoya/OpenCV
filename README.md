# OpenCV
This is a tutorial of learning OpenCV with Python.

## Indroduction

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