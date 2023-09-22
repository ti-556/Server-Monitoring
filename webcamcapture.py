import cv2
import time

#time interval between each screenshot (seconds)
interval = 5

def capture():
    
    #create cv2 camera & window
    camera = cv2.VideoCapture(0)
    cv2.namedWindow("Webcam Capture")
    
    imagecounter = 0
    
    while(True):
        #break from loop if cv2 can't receive frame data
        ret,frame = camera.read()
        if not ret:
            print("frame error")
            break
        
        else:
            time.sleep(interval)
            #saving image frame
            imagename = "frame_{}.jpg".format(imagecounter)
            cv2.imwrite(imagename, frame)
            print(f"{imagename} saved")
            imagecounter += 1

    #destroy camera & window after loop
    camera.release()
    cv2.destroyAllWindows()