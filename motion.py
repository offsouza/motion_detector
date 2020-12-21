import cv2



def motion(img,last):
    diff = cv2.absdiff(last, img)        
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    cv2.imshow('thresh', thresh)
    dilated = cv2.dilate(thresh, None, iterations=4)             
    cv2.imshow('dilated', dilated)
    contours, hirarchy = cv2.findContours(dilated.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            print(cv2.contourArea(contour))
            if cv2.contourArea(contour) > 5000:                   
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)                 
                print('moving')
                return True
            print('not')
    return False


def main():
    cap = cv2.VideoCapture(0)

    last_frame = None

    while cap.isOpened():
        _, frame = cap.read()
        frame2 = frame.copy()

        if last_frame is None:
            last_frame = frame.copy()
            
            print('update')
        else:
            motion(frame, last_frame)
            #cv2.imshow('img', img)
            cv2.imshow('frame', frame)
            #cv2.imshow('lastframe', last_frame)
            if cv2.waitKey(1) == ord('q'):
                break
            last_frame = frame2






if __name__ == '__main__':
    main()