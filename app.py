import cv2
import math
import argparse


def highlistface(net, frame, conf_threshold=0.7):
  frameOpencvDnn = frame.copy()
  frameHeight = frameOpencvDnn.shape[0]
  frameWidth = frameOpencvDnn.shape[1]
  blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)
  net.setInput(blob)
  detection = net.forward()
  faceBoxes = []
  for i in range(detections.shape[2]):
    confidence = detections[0,0,i,2]
    if confidence > conf_threshold:
      x1 = int(detections[0,0,i,3]*frameWidth)
      y1 = int(detections[0,0,i,4]*frameHeight)
      
  
