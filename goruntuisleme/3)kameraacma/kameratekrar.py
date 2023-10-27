import cv2
import time

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
hight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
hight2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, hight)
print(width2, hight2)

writer = cv2.VideoWriter("video kaydı.mp4", cv2.VideoWriter_fourcc(*"DIVX"),20, (width,hight))
writer2 = cv2.VideoWriter("video kaydı2.mp4", cv2.VideoWriter_fourcc(*"DIVX"),20, (width2,hight2))
while True:
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()
    if ret == True and ret2 == True:
        time.sleep(0.02)
        cv2.imshow("video",frame)
        writer.write(frame)
        cv2.imshow("video2", frame2)
        writer2.write(frame2)
    else: break
    if cv2.waitKey(1) & 0xFF == ord("q"): break
cap.release()
cap2.release()
writer.release()
writer2.release()
cv2.destroyAllWindows()