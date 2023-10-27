import cv2
import time

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("Kamera 1 genişlik: ",width)
print("Kamera 1 yükseklik: ",height)
print("Kamera 2 genişlik: ",width2)
print("Kamera 2 yükseklik: ",height2)
writer = cv2.VideoWriter("video1.mp4",cv2.VideoWriter_fourcc(*"DIVX"), 20, (width,height))
writer2 = cv2.VideoWriter("Kamera2.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20, (width2,height2))
if cap.isOpened() and cap2.isOpened() == False:
    print("Hata")

while True:
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()

    if ret and ret2 == True:
        time.sleep(0.02)
        cv2.imshow("kamera1",frame)
        cv2.imshow("kamera2", frame2)
        writer.write(frame)
        writer2.write(frame2)
    else: break

    if cv2.waitKey(1) &0xFF == ord("s"): break
cap.release()
cap2.release()
writer.release()
writer2.release()
cv2.destroyAllWindows()