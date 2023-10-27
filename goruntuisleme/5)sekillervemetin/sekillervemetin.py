import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) #siyah resim oluşturduk
print(img.shape) #boyutunu öğrendik
cv2.imshow("siyah resim",img)

#resime çizgi çizmek
#((resim),(başlangıç noktası), (bitiş noktası), (renk), (kalınlık) renk BGR
cizgi = cv2.line(img,(0,0),(512,512),(0,255,0),1)
cv2.imshow("cizgili resim",cizgi)

#dikdörtgen çizme
#((resim),(başlangıç noktası), (bitiş noktası), (renk), (kalınlık) renk BGR
rectangel = cv2.rectangle(img, (0,100) ,(200,200) ,(255,0,0),2 )#cv2.FILLED bu komut dikdörtgenin içini dolduruyor
cv2.imshow("dikdörtgen",rectangel)

#çember
#((resim),(başlangıç noktası), (yariçap), (renk), (kalınlık) renk BGR
cember = cv2.circle(img,(300,300),45,(0,255,0),2)
cv2.imshow("cember",cember)

#metin
#((resim), (yazdırılcak metin), (başlangıç noktası), (font), (kalınlık), (renk)
metin = cv2.putText(img, ("RESIM"), (250,250), (cv2.FONT_HERSHEY_COMPLEX), 1, (255,255,255))
cv2.imshow("cember",metin)

cv2.waitKey(0) &0xFF == ord("q")