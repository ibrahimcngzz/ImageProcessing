import cv2
import numpy as np

img = cv2.imread("kart.png")
print(img.shape)
cv2.imshow("Orijinal",img)

width = 400 #genişlik
height = 500 #yükseklik


pts1 = np.float32([[204,2],[1,474],[541,146],[340,618]]) #resmimizin köşeleri
pts2 = np.float32([[0,0], [0,height], [width,0], [width,height]]) #çevirmek istediğimiz resmin köşeleri

#transformu gerçekleştirmek için matrisi elde etmek gerekiyor
matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)
#nihai dönüştürülmüş resim
#resim , rotasyon matrisi , nihai olarak elde etmek istediğimiz boyut
imgOutput = cv2.warpPerspective(img, matrix , (width,height)) #(0,0) resimin en sol üst köşe yapar
cv2.imshow("Nihai",imgOutput)


cv2.waitKey(0)