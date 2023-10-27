import cv2
import time
#video ismi
videoName = "VID_148460213_042151_833.mp4"

#videoyu içe aktarma: capture, cap diye kısaltılır genelde
cap = cv2.VideoCapture(videoName) #Bu videoyu cap içerisine aktar demek
print("Genişlik: ", cap.get(3)) #Videonun genişliğini elde ederim
print("Yükseklik: ", cap.get(4)) #Videonun yüksekliğini elde ederim

if cap.isOpened() == False: #Video açıldımı
    print("Hata") #açılmadıysa hata mesajı ver
#frame dediğimiz şey videonun içinde bulunan her bir resim
#Return dediğimiz şeyde bu işlemin başarılı olup olmadığı
#Bir video bir çok frameden oluştuğu için bu işlemleri tekrarlamak için while döngüsü içinde getiriyruz frameleri
while True:
    ret, frame = cap.read()

    if ret == True:
        time.sleep(0.01) #kullanmazsak çok hızlı akar frameler ard arda çok hızlı oynar normalde
        cv2.imshow("Video",frame)
    else: break

    if cv2.waitKey(1) &0xFF == ord("q"):
        break  #eğer klavyemizden bastığımız tuş çıkma tuşuna eşitse döngüyü kır

cap.release() #video almayı bırakıyoruz
cv2.destroyAllWindows()