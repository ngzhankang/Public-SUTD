from deepface import DeepFace
from time import sleep
import cv2
import os
import datetime

frames_analyzed = 3
backends = [
  'opencv', 
  'ssd', 
  'dlib', 
  'mtcnn', 
  'retinaface', 
  'mediapipe',
  'yolov8',
  'yunet',
]

while True:
        i = 0
        start_time = datetime.datetime.now()

        while i < frames_analyzed:
                vidcap = cv2.VideoCapture(0)
                if vidcap.isOpened():
                    ret, frame = vidcap.read()
                    if ret:
                        cv2.imwrite("Frames/"+str(i)+".jpg",frame)
                    else:
                        print("Error : Failed to capture frame")
                else:
                    print("Cannot open camera")
                vidcap.release()
                i = i+1
                
        face_detected = 0
        
        for i in range(frames_analyzed-1):
                try:
                        DeepFace.extract_faces(img_path = "Frames/"+str(i)+".jpg", detector_backend = backends[5])
                        face_detected = face_detected+1
                except:
                        continue
                os.remove("Frames/"+str(i)+".jpg")

        end_time = datetime.datetime.now()  
        print(face_detected, (end_time-start_time).total_seconds())
