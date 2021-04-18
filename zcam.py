import cv2

#from OpenCV Library
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#count variables
countClose = 0
countFar = 0

class cam(object):
    '''
    Citation for code for function __del__ and __init__ 
    Title: How I got my OpenCV Project on a web server
    Author: Misbah Mohammed
    Date:4/17/2021
    Program Version: Python 3.8.6
    Availability: 
    https://www.youtube.com/watch?v=-4v4A550K3w
    '''  
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.releast()
        
    def get_frame(self):
        #Lines 27-35 uses functions from OpenCV Library
        ret, frame = self.video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #Detects face
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        
        #Draws the rectangle around a face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
        #based on the area the rectangle, determines if you are too close or too far away from camera
            lengthFaceRect = (x + w) - x
            widthFaceRect = (y + h) - y
            areaFaceRect = lengthFaceRect * widthFaceRect
            if areaFaceRect <= 12000:
                #makes local variable global to have a counter
                global countFar
                countFar = countFar + 1
                print("You have been too far away from your screen " + str(countFar) + " times.")
            if areaFaceRect >= 40000:
                global countClose
                countClose = countClose + 1
                print("You have been too close to your screen " + str(countClose)+ " times.")
                                
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

