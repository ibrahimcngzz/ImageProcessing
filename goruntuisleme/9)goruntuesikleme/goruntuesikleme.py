import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img1.JPG")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure("Orijinal"), plt.imshow(img, cmap= "gray"), plt.axis("off")

#eşikleme
#threshold metodu (resim), (alt sınır)thresold değeri üzerindeki yerleri beyaz gösterir, (maksimum değer), (TYPE)
_,tresh_img = cv2.threshold(img,thresh=60, maxval= 255, type=cv2.THRESH_BINARY) #THRESH_BINARY 60 ile 255 arasındaki değerleri beyaz yapıyor invers tam tersini yapar
plt.figure("Thresoldbınary"), plt.imshow(tresh_img, cmap= "gray"), plt.axis("off")

_,tresh_img2 = cv2.threshold(img,thresh=60, maxval= 255, type=cv2.THRESH_BINARY_INV) #THRESH_BINARY_INV 60 ile 255 arasındaki değerleri siyah yapıyor
plt.figure("Thresoldınv"), plt.imshow(tresh_img2, cmap= "gray"), plt.axis("off")

#Uyarlamalı eşik değeri
#Adaptive thresold yöntemini kullanıyoruz = ((resim),(maksimum valuemuz),(adaptivmetodu yöntemi)c sabitine göre ortalama alınıyor,(eşikleme türü), blocksize)
tresh_img3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8 )
plt.figure("AdaptivThresold"), plt.imshow(tresh_img3, cmap= "gray"), plt.axis("off")

plt.show()




