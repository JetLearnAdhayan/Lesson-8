import cv2
import os

haarfile = "C:/Users/Adhay/OneDrive/Desktop/Open CV/Lesson 8/haarcascade_frontalface_default.xml"
dataset = "C:/Users/Adhay/OneDrive/Desktop/Open CV/Lesson 8/dataset"
sub_folder = "Adhayan"

path =os.path.join(dataset, sub_folder)

if not os.path.isdir(path):
    os.mkdir(path)

#defining the size of images 
(width, height) = (130,100)

face_cascade = cv2.CascadeClassifier(haarfile)

webcam = cv2.VideoCapture(0)

count = 1
while count <= 30:
    return_val,img=webcam.read()
    grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayscale, 1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        face = grayscale[y:y + h, x:x + w]
        face_resize = cv2.resize(face,(width,height))
        cv2.imwrite('% s/% s.png' % (path, count), face_resize) 
    count +=1    
    cv2.imshow("OpenCV",img)
    key = cv2.waitKey(0)
    if key == 27:
        break
