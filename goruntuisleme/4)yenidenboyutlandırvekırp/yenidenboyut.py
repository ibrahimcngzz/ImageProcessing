import cv2

img = cv2.imread("lenna.png")
print("resim boyutu",img.shape)
cv2.imshow("orijinal",img)
#resized yeniden boyutlandırma
yeni = cv2.resize(img, (700,700)) #yeniden boyutlandırma komutu
cv2.imshow("yeni resim",yeni)
yeni2 = cv2.resize(img, (50,50)) #yeniden boyutlandırma komutu
cv2.imshow("yeni2 resim",yeni2)

kirp = img[:400,:300]  #ilk yükseklik sonra genişlik
cv2.imshow("kirpilmis resim",kirp)

cv2.waitKey(0) &0xFF == ord("s")

