import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore") #hata almama kütüphanesi
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #BGR formatından RGB formatına dönüştürülür.
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("Orijinal")
#blurring (detayı azaltır, gürültüyü engeller)
#ortalama bulanıklaştırma yöntemi
dst2 = cv2.blur(img, ksize= (3,3)) #işlevi kullanılarak görüntüye 3x3 boyutunda bir ortalama (mean) bulanıklaştırma filtresi uygulanır.
#plt.figure(),plt.imshow(dst2),plt.axis("off"),plt.title("Ortalama Blur")

#gaussian blur
# işlevi kullanılarak görüntüye 3x3 boyutunda bir Gaussian bulanıklaştırma filtresi uygulanır.
#"sigmaX" parametresi, Gaussian filtresinin standart sapmasını kontrol eder ve bu değer büyüdükçe daha fazla bulanıklaştırma olur.
gb = cv2.GaussianBlur(img, ksize=(3,3), sigmaX=7)
#plt.figure(),plt.imshow(gb),plt.axis("off"),plt.title("Gaussian Blur")

#Medyan blur
#işlevi kullanılarak görüntüye 3x3 boyutunda bir medyan (median) bulanıklaştırma filtresi uygulanır.
mb = cv2.medianBlur(img, ksize=3)
#plt.figure(),plt.imshow(mb),plt.axis("off"),plt.title("Medyan blur")

#gausnois oluşturma
def gaussianNoise(image):
    row, col, ch = image.shape #giriş görüntüsünün satır sayısı, sütun sayısı ve renk kanalı sayısıdır.
    mean = 0 #eklenen Gaussian gürültüsünün ortalamasıdır.
    var = 0.05 #Gaussian gürültüsünün varyansını temsil eder.
    sigma = var**0.5 #varyansın karekökü olarak hesaplanır.

    gauss = np.random.normal(mean,sigma,(row,col,ch)) #Gaussian dağılıma sahip rastgele sayılar üretilir. Bu sayılar, görüntü boyutlarına ve kanal sayısına uygun bir şekilde düzenlenir.
    gauss = gauss.reshape(row,col,ch) #yeniden şekillendirilir ve orijinal görüntüye eklenir, bu da gürültülü bir görüntüyü elde eder.
    noisy = image + gauss
    return noisy
#içe aktar normalize et
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255 #BGR formatından RGB formatına dönüştürülür. Ardından, görüntüyü 0 ile 1 arasında ölçeklemek için 255'e bölünür
#plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("pikselo-1")
#gausnois görünümünü Gaussian Blur ile azaltma
gaussianNoisyImage = gaussianNoise(img)
#plt.figure(),plt.imshow(gaussianNoisyImage),plt.axis("off"),plt.title("gaussianNoisy olusturma")
gb2 = cv2.GaussianBlur(gaussianNoisyImage, ksize=(5,5), sigmaX=5) #gaussianNoisyImage üzerine Gaussian bulanıklaştırma uygulanır.
#plt.figure(),plt.imshow(gb2),plt.axis("off"),plt.title("Gaussian Blur2")

def saltPepperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    noisy = np.copy(image)

    #salt beyaz
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy[coords] = 1

    #pepper siyah
    num_pepper = np.ceil(amount * image.size * (1 - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy[coords] = 0

    return noisy
spImage = saltPepperNoise(img)
plt.figure(),plt.imshow(spImage),plt.axis("off"),plt.title("Median Blur2")

mb2 = cv2.medianBlur(spImage.astype(np.float32), ksize = 3)
plt.figure(), plt.imshow(mb2), plt.axis("off"), plt.title("with Medyan Blur")
plt.show()
matplotlib.use('TkAgg')