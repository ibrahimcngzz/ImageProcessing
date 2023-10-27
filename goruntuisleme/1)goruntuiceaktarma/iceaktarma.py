import cv2

img = cv2.imread("IMG-20220904-WA0024.jpg",0)  #Bu komut görüntüyü okuyup img değişkenine atıyor ,0 koyarsak resimi siyah beyaz yapıyor
cv2.imshow("Resim",img) #resimi görüntülemek için kullanılır
k = cv2.waitKey(0) &0xFF #Klaveden komut bekleme
if k == 27:  #esc komutu
    cv2.destroyAllWindows() #tüm pencereleri kapat
elif k == ord("s"):
    cv2.imwrite("Resim_gray.png",img)  #eğer klavhyeden s tuşu girildiyse bu resimi kaydet
    cv2.destroyAllWindows()
