import cv2
import face_recognition


cap = cv2.VideoCapture(-1)


while True:

    success,img = cap.read()
    img = cv2.rotate(img, cv2.ROTATE_180)
    faceLoc1 = face_recognition.face_locations(img)
    print("faces" + str(faceLoc1))

    print(faceLoc1)

    if(faceLoc1):
        faceLoc = faceLoc1[0]
        print(faceLoc)
        cv2.rectangle(img,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)
    
    cv2.imshow("Image",img)
    cv2.waitKey(1)


#------------------------

# img = cv2.imread('download.jpeg')
# print(img.shape)
# faceLoc = face_recognition.face_locations(img)[0]

# cv2.rectangle(img,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

# cv2.imshow("Image",img)
# cv2.waitKey(0)