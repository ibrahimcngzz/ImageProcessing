import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("img1.JPG")
#opencv bir fotoğraf yüklerken BGR formatında yükleniyor bunu RGB çevirmek gerek
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) #renkleri konvört etmek
img1 = cv2.resize(img1, (800,800)) #resimin boyutunu ayarlama
plt.figure()
plt.imshow(img1) #matplotlib kütüphanesinde görselleştirme
plt.axis("off")

img2 = cv2.imread("img2.JPG")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB) #renkleri konvört etmek
img2 = cv2.resize(img2, (800,800)) #resimin boyutunu ayarlama
plt.figure()
plt.imshow(img2) #matplotlib kütüphanesinde görselleştirme
plt.axis("off")

print(img1.shape) #resimin boyutunu gösterme
print(img2.shape) #resimin boyutunu gösterme


#karıştırılmış resim = alpha * img1 + beta*img2
#addWeighted bu formülü yerine getirmeye yarıyor src1 = sours bir demek
blended = cv2.addWeighted(src1= img1, alpha=0.5, src2= img2, beta= 0.5, gamma=0)
plt.figure()
plt.imshow(blended) #matplotlib kütüphanesinde görselleştirme
plt.axis("off")
plt.show()
