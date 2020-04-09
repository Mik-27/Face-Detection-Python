# Face Detection
Project includs detection of face from from a saved image and also detection of face live through the webcam.
## Getting Started
This files can be run on any Pyhton IDE or simply through the command prompt.
### Prerequisites
Pyhton needs to be installed on your system for running the code. It also requires the OpenCV framework for getting images and storing them.

## Description
The detection of the face from the image or live webcam is done with the help of a database provided in opencv itself.
This file ```haarcascade_frontalface_default.xml``` contains the various attributes of the face and they are compared with the frame in the code.
The frame/frames is converted to grayscale for better comparison with the datavbase.

Algorithm is used for the detection of the face by scaling the face with reference to ```scalingFactor```. The scaling is increase from 1% to 100% of the orignal. The less is the scaling factor more is the accuracy of detection. Reducing the ```scalingFactor``` may result in detection of objects that are not faces but contain some attributes of a face.
In the code,
```
scalingFactor = 1.15
```
The minimum number of neighbours to a face are:
```
minNeighbours = 5
```
A rectangle shows the face that is detected according to the values that are returned by the 
```face_cascade.detectMultiScale(img, scalefactor, minNeighboours)```.

## Built with

* [Python](https://www.python.org) - The language used.
* [OpenCV](https://opencv.org) - The framework used.

## Author

* **Mihir Thakur** - [GitHub](https://github.com/Mik-27)

## Thank You
