import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import database as db
from profile import *


def faceRecog():
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    recognizer.read("recognizer/training.yml")
    font = cv2.FONT_HERSHEY_PLAIN
    counter = 0
    id = 0
    profile = []
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret:
            counter += 1 

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        
        # Detect face
        face = faceCascade.detectMultiScale(
            gray,
            scaleFactor = 1.1,
            minNeighbors = 5
            )
        
        
        # Draw rectangle around faces
        for x,y,w,h in face:
            id, conf= recognizer.predict(gray[y:y+h, x:x+w])
            profile = db.getProfile(id)
            if profile != None and conf < 85:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, str(profile[1]),(x, y+h+30), font, 1, (0, 255, 0), 2)
            break
        
        
        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or counter == 50:
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    if profile != None  and id != None:
        std_details(profile)


def QRscan():
    cap = cv2.VideoCapture(0)                               #capture live video from webcam
    font=cv2.FONT_HERSHEY_PLAIN

    while True:
        _, frame =cap.read()                                #capture frame
        decodedObjects = pyzbar.decode(frame)               #decode qr code from frame
        cv2.putText(frame,str('Please show the QR code on the camera!'),(150,50),font,1,(0,0,0),2)
        for x in decodedObjects:
            data=x.data.decode("utf-8")
            print("DATA: ", data)
            cv2.putText(frame,str(data),(50,150),font,2,(255,0,0),3)
            cv2.waitKey(1000)

        cv2.imshow("Frame",frame)
        key = cv2.waitKey(1)
        if key == 27:                                       #press Esc to close camera #also ord('q') can be used i.e. press q to exit
            break
    print("Decoded QR code is : ", data)
    cap.release()
    cv2.destroyAllWindows()

