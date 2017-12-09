from skimage.io import imread, imsave
from numpy import clip
from skimage import img_as_ubyte 
import math
import numpy as np

img = imread ('https://stepik.org/media/attachments/lesson/61037/tiger-gray-small.png')

sigma = 0.66
def gauss (sigma, x, y):
    g = 1/(2*np.pi*sigma**2)*np.exp((-x**2-y**2)/(2*sigma**2))
    return g

k=int(2*round(3*sigma)+1)
gg = np.array(np.ones((k,k)))
for i in range (k):
    for j in range (k):
        gg [i,j] = gauss (sigma, i-k//2, j-k//2)
gg = gg/sum(sum(gg))

img_out = img.copy()
for i in range (2, img.shape[0]-2):
    for j in range (2, img.shape[1]-2):
        img_out [i,j] = sum (sum(img[(i-2):(i+3),(j-2):(j+3)] * gg))

img_out = img_out [2:(img_out.shape[0]-2), 2:(img_out.shape[1]-2)]
img_out = clip(img_out, 0, 255)
img_out = np.array (img_out, dtype=np.uint8)


im2 = imread ('https://stepik.org/media/attachments/lesson/61037/gaussian-tiger.png')
np.array_equal (img_out, im2)
