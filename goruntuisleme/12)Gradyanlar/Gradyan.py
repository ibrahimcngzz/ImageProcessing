import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("sudoku.jpg",0)
plt.figure(), plt.imshow(img,"gray"),plt.axis("off"),plt.title("Orijinal")

#x gradyan
sobelX = cv2.Sobel(img, ddepth= cv2.CV_16S , dx=1,dy=0, ksize=5) #işlevi kullanılarak X gradyan işlemi uygulanır. Bu, görüntü üzerinde yatay kenarları vurgular
plt.figure(), plt.imshow(sobelX,"gray"),plt.axis("off"),plt.title("X gradyanı")

#Y gradyan
sobelY = cv2.Sobel(img, ddepth= cv2.CV_16S , dx=0,dy=1, ksize=5) #işlevi kullanılarak y gradyan işlemi uygulanır. Bu, görüntü üzerinde yatay kenarları vurgular
plt.figure(), plt.imshow(sobelY,"gray"),plt.axis("off"),plt.title("y gradyanı")

#Laplacian
laplacian = cv2.Laplacian(img, ddepth= cv2.CV_16S)
plt.figure(), plt.imshow(laplacian,"gray"),plt.axis("off"),plt.title("Laplas gradyanı")




plt.show()