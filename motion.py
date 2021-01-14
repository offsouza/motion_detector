import cv2

cap = cv2.VideoCapture('videoplayback.mp4')

last_frame = None


sensibilidade =  1000  #quanto menor mais sensivel (detecta movimento menores)

while cap.isOpened():

    _, frame = cap.read()
    frame_copy = frame.copy()  
    if last_frame is None:
        last_frame = frame  
        cv2.imshow('frame', last_frame)        
        #cv2.waitKey(0)
    else:
        diff = cv2.absdiff(last_frame, frame)        
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (7, 7), 0)
        _, thresh = cv2.threshold(blur, 5, 255, cv2.THRESH_BINARY)            
        dilated = cv2.dilate(thresh, None, iterations=5)                        
        contours, hirarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)         
        for contour in contours:
                (x, y, w, h) = cv2.boundingRect(contour)                    
                if cv2.contourArea(contour) > sensibilidade:                       
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)                 
                    print('moving')                
        cv2.imshow('frame', frame )            
        if cv2.waitKey(1) == ord('q'):
            break            
        last_frame = frame_copy

