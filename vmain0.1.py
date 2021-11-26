import cv2
import time

# load face detection model
face_cascade = cv2.CascadeClassifier('model/haarcascade_frontalface_default.xml')
# open camera
cap = cv2.VideoCapture(0)

crowdDef = 2 # or more
crowdCount = 0

while 1:
    # reset count
    crowdCount = 0

    # read camera frame
    ret, img = cap.read()
    
    img = cv2.flip(img, 1)
    img2 = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detect face/people 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # read faces
    for (x,y,w,h) in faces:
        # mark faces identified
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        # increment faces/people count
        crowdCount = crowdCount + 1

    print("Crowd Count")
    print(crowdCount)

    # if people count greater than crowd defination alert Crowd Detected
    if crowdCount >= crowdDef:
        print("Crowd recorded")
        crowdDetectedFile = "crowd-detected-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"
        cv2.imwrite(crowdDetectedFile, img)
        print("Crowd alert")
        # Area is over crowded. Please maintain social distance.

    cv2.imshow('img',img)

    # check key press, if q key preessed exit application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    #time.sleep(0.5)

# release object created
cap.release()
cv2.destroyAllWindows()
