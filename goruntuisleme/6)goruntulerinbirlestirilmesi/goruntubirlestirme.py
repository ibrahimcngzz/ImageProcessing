import cv2
import numpy as np

img = cv2.imread("lenna.png")
cv2.imshow("Orijinal",img)

img2 = cv2.resize(img,(300,300))
cv2.imshow("kucultme",img2)
#yatay birleştirme
hor = np.hstack((img2,img2)) #resimleri yatay birleştirmek için kullanılıyor
cv2.imshow("yatay",hor)

ver = np.vstack((img2,img2)) #resimleri dikey birleştirmek için kullanılıyor
cv2.imshow("dik",ver)
if cv2.waitKey(0) &0xFF == ord("q"):
    cv2.destroyAllWindows()
