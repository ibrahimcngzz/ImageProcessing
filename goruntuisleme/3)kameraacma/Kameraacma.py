import time
import cv2

#capture
cap = cv2.VideoCapture(0) #kendi kameranı kullanırsan 0 başka kamera takarsan 1

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #Frame genişliğini al demek
hight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  #Frame yüksekliğini al demek

print(width, hight) #Ekrana kameranın genişlik ve yüksekliğini yazma

#video kaydet
#fourcc windows için kullanılıyor çerçeveleri sıkıştırmak için kullanılan codec kodu
writer = cv2.VideoWriter("video kaydı.mp4", cv2.VideoWriter_fourcc(*"DIVX"),20, (width,hight)) #her saniyede görüceğimiz resim sayısı
#frame dediğimiz şey videonun içinde bulunan her bir resim
#Return dediğimiz şeyde bu işlemin başarılı olup olmadığı
#Bir video bir çok frameden oluştuğu için bu işlemleri tekrarlamak için while döngüsü içinde getiriyruz frameleri
while True:
    ret, frame = cap.read()
    if ret == True: #eğer video sorunsuz oynarsa
        time.sleep(0.01)
        cv2.imshow("video",frame) #frameleri göster
        writer.write(frame) #frameleri kaydetme
    else: break
    if cv2.waitKey(1) &0xFF == ord("q"): break
cap.release() #video almayı bırakıyoruz
writer.release() #writera yazma işlemi bitti diyoruz
cv2.destroyAllWindows()





