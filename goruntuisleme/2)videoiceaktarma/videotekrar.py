import cv2
import time

name = "VID_148460213_042151_833.mp4"
cap = cv2.VideoCapture(name)

print("Genişlik: ",cap.get(3))
print("Yükseklik: ",cap.get(4))

if cap.isOpened() == False:
    print("Hata")

while True:
    ret, frame = cap.read()

    if ret == True:
        time.sleep(0.01)  # kullanmazsak çok hızlı akar frameler ard arda çok hızlı oynar normalde
        cv2.imshow("Video",frame)
    else: break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break  # eğer klavyemizden bastığımız tuş çıkma tuşuna eşitse döngüyü kır

cap.release()  # video almayı bırakıyoruz
cv2.destroyAllWindows()
