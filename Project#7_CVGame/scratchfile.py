import numpy as np
import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

cap = cv.VideoCapture(0)
h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(h, w)

detector = HandDetector(detectionCon=0.8, maxHands=1)

# Player paddle
pw = 10
ph = 80
pc = (200, 0, 150)
pX1 = (0, int(h / 2 - ph / 2))
pX2 = (pw, int(h / 2 + ph / 2))

# Opponent paddle
Ow = 10
Oh = 80
Oc = (200, 150, 10)
Otop = h / 2 - Oh / 2  # Set opponent paddle at the center vertically
Obottom = Otop + Oh
OpX1 = (w - Ow, int(Otop))
OpX2 = (w, int(Obottom))

# Ball properties
ballC = (200, 200, 200)
ballPos = [int(w / 2), int(h / 2)]
Crad = 10
ballVx = 5
ballVy = 5
ypos = h / 2

while True:
    success, frame = cap.read()
    frame = cv.flip(frame, 1)
    hand, frame = detector.findHands(frame, draw=True)

    # Update player paddle position based on hand position
    if hand:
        landmark = hand[0]['lmList']
        ypos = landmark[9][1]
        if ypos - ph / 2 < 0:
            ypos = ph / 2
        if ypos + ph / 2 > h:
            ypos = h - ph / 2
        pX1 = (0, int(ypos - ph / 2))
        pX2 = (pw, int(ypos + ph / 2))

    # Ball movement
    ballPos[0] += ballVx
    ballPos[1] += ballVy

    # Ball collision with walls (top and bottom)
    if ballPos[1] + Crad > h or ballPos[1] - Crad < 0:
        ballVy *= -1

    # Ball collision with paddles
    if ballPos[0] - Crad <= pw and pX1[1] <= ballPos[1] <= pX2[1]:
        ballVx *= -1

    if ballPos[0] + Crad >= w - Ow and OpX1[1] <= ballPos[1] <= OpX2[1]:
        ballVx *= -1

    # Move the opponent paddle towards the ball's vertical position
    if ballPos[1] < Otop + Oh / 2:
        Otop -= ballVy  # Move opponent paddle up
    elif ballPos[1] > Otop + Oh / 2:
        Otop += ballVy  # Move opponent paddle down

    # Ensure the opponent paddle stays within screen bounds
    if Otop < 0:
        Otop = 0
    if Otop + Oh > h:
        Otop = h - Oh

    Obottom = Otop + Oh
    OpX1 = (w - Ow, int(Otop))
    OpX2 = (w, int(Obottom))

    # Draw paddles and ball
    

    # Display frame
    cv.imshow("Pong", frame)

    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()
