import cv2
face_mask = cv2.CascadeClassifier('classifier\cascade.xml')
#img = cv2.imread('with.jpeg')
#img = cv2.resize(img,(240,300))
#cap = cv2.VideoCapture('face2.mp4')
cap = cv2.VideoCapture('videos\Videoclip2.wmv')



while cap.isOpened():
    
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_mask.detectMultiScale(gray,1.1,4)
    for(x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color=img[y:y+h, x:x+w]
        font = cv2.FONT_HERSHEY_SIMPLEX
		#fontScale = 1
        cv2.putText(img, 'Using Mask',(55,280), font,2.5,(255,0,0),cv2.LINE_AA)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'Without Mask',(20,200), font,2.5,(255,255,255))
    cv2.imshow('SAI',img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    #cv2.waitKey()
cap.release()
cv2.destroyAllWindows()

