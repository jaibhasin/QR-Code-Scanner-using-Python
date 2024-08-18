import cv2 
from pyzbar.pyzbar import decode 
import time 


cam = cv2.VideoCapture(0)
# cam.set(5,640)
# cam.set(6,480)

camera = True 
while camera==True :
    success , frame = cam.read()
 
    cv2.imshow("OurQr_Code_Scanner",frame)

    for i in decode(frame):
        # cv2.imshow("OurQr_Code_Scanner",frame)
        print(i.type)
        print(i.data.decode('utf-8'))
        print("Successful")
        time.sleep(3)
        camera = False

        cv2.waitKey(3)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# if (i.data.decode('utf-8')) == "okay okay" :
#     print("Passed")
# else :
#     print("Failed")

