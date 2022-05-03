from cvzone.HandTrackingModule import HandDetector
import cv2
import SpoutGL
from OpenGL import GL

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
spoutSender = SpoutGL.SpoutSender()
spoutSender.setSenderName('cvzone')

while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    hands, img = detector.findHands(img)  # with draw
    # hands = detector.findHands(img, draw=False)  # without draw

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)


    # Display
    cv2.imshow("Image", img)
    spoutSender.sendImage(img, img.shape[1], img.shape[0], GL.GL_RGB, False, 1)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()