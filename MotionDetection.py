import cv2

cap = cv2.VideoCapture('vtest.avi')
while cap.isOpened():
    ret, frame1 = cap.read ()
    ret, frame2 = cap.read ()
    diff = cv2.absdiff(frame1, frame2)
    imgray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(imgray, (5,5), 0)
    _,thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours,_ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)
        if cv2.contourArea(contour)<700:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame1,"status : {}".format("movement"), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 3)
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    if cv2.waitKey(1) == ord('d'):
        break
    cv2.imshow ( 'vtest.avi', frame1 )
    #frame1 = frame2
    #ret, frame2 = cap.read()
cv2.destroyAllWindows()
cap.release()