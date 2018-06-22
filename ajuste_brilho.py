import cv2
import numpy as np

img  = cv2.imread('original.png')

alpha = 2

#beta < 0, a imagem fica escura
#beta > 0, a imagem fica mais clara
beta = -250

resut = cv2.addWeighted(img, alpha, np.zeros(img.shape, img.dtype), 0, beta)
cv2.imwrite('ajuste.png', resut)