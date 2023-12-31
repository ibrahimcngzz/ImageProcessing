import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("datai_team.jpg",0)
plt.figure(),plt.imshow(img,cmap="gray"),plt.axis("off"),plt.title("Orijinal resim")

#erozyon
kernel = np.ones((5,5), dtype= np.uint8) #kutucuk belirliyoruz resim üzerinde dolaşıcak ve sınırı düşürücek
result = cv2.erode(img, kernel, iterations=1)
plt.figure(),plt.imshow(result,cmap="gray"),plt.axis("off"),plt.title("Erozyon resim")

#genişleme dilation
result2 = cv2.dilate(img, kernel, iterations=1)
plt.figure(),plt.imshow(result2,cmap="gray"),plt.axis("off"),plt.title("Genisleme resim")

#white noise beyaz gürültü oluşturma
whiteNoise = np.random.randint(0,2, size= img.shape[:2])
whiteNoise = whiteNoise*255
plt.figure(),plt.imshow(whiteNoise,cmap="gray"),plt.axis("off"),plt.title("Beyaz gürültü")
noise_img = whiteNoise + img
plt.figure(),plt.imshow(noise_img,cmap="gray"),plt.axis("off"),plt.title("Beyaz gürültülü resim")

#açılma
opening = cv2.morphologyEx(noise_img.astype(np.float32),cv2.MORPH_OPEN,kernel)
plt.figure(),plt.imshow(opening,cmap="gray"),plt.axis("off"),plt.title("Acilma resim")

#black noise
blackNoise = np.random.randint(0,2, size= img.shape[:2])
blackNoise = blackNoise*-255
plt.figure(),plt.imshow(blackNoise,cmap="gray"),plt.axis("off"),plt.title("Siyah gürültü")

black_noise_img = blackNoise + img
black_noise_img[black_noise_img <= -245] = 0 #filtreye sokmak
plt.figure(),plt.imshow(black_noise_img,cmap="gray"),plt.axis("off"),plt.title("Siyah gürültülü resim")

#kapatma
closing = cv2.morphologyEx(black_noise_img.astype(np.float32),cv2.MORPH_CLOSE,kernel)
plt.figure(),plt.imshow(closing,cmap="gray"),plt.axis("off"),plt.title("Kapama")

#gradyan
gradyan = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
plt.figure(),plt.imshow(gradyan,cmap="gray"),plt.axis("off"),plt.title("Gradyan")
plt.show()