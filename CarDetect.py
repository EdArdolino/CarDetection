import cv2
from tracker import *

# Create tracker
tracker = EuclideanDistTracker()

#Video Source
# If issues arise, paste the path of 'highway.mp4' into the quotes below
cap = cv2.VideoCapture("highway.mp4")

# Object Detector
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape


    # Extract an aoi (Area of interest)
    aoi = frame[350: 750, 500: 800] 

    # Object Detection
    mask = object_detector.apply(aoi)
    # 0 = black, 255, completly white
    # Threshold allows us to only consider objects that are completly white
    # Remove anything under 254
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    for cnt in contours:

        #Calc area and remove small (not needed) elements
        area = cv2.contourArea(cnt)
        if area > 90:
            #cv2.drawContours(roi, [cnt], -1, (0,255,0), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            
            detections.append([x,y,w,h])

    # Object Tracking
    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        
        # Creates a rectangle aroud the detected vehicles
        # Adds a number above the detected vehicles to keep count
        cv2.putText(aoi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
        cv2.rectangle(aoi, (x, y), (x + w, y + h), (0, 0, 255), 3)


    cv2.imshow("Area of Interst", aoi)
    cv2.imshow("MP4", frame)
    cv2.imshow("Mask",mask)

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()