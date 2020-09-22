from skimage import io
from matplotlib import pyplot as plt
from os import listdir
from skimage.viewer import ImageViewer
import numpy as np
card_dict = {}
a = io.imread("imagea.jpg")
b = io.imread("imageb.jpg")
c = io.imread("imagec.jpg")
who = io.imread("whoami.jpg")

a_slice = a[150:500,100:500]
b_slice = b[150:500,100:500]
c_slice = c[150:500,100:500]
who_slice = who[150:500,100:500]

card_dict['phyrexian_arena'] = a_slice
card_dict['hypnotic_specter'] = b_slice
card_dict['cryptbreaker'] = c_slice
# viewer = ImageViewer(a_slice)
# viewer.show()
# print(card_dict)
min_mse = 9999

for candidate_name,candidate_image in card_dict.items():
    mse = np.linalg.norm(who_slice - candidate_image)
    if (mse < min_mse):
        min_mse = mse
        min_candidate = candidate_name
print(min_candidate)


card_dict = {}
directory = "Cards/"
file_list = listdir(directory)
min_mse = 9999
for fname in file_list:
    img_name = fname.split('.')[0]
    image = io.imread(directory + fname)
    size = image.shape
    n_slice = image[150:500,100:500]
    card_dict[img_name] = n_slice
        
for candidate_name,candidate_image in card_dict.items():
    mse = np.linalg.norm(who_slice - candidate_image)
    if (mse < min_mse):
        min_mse = mse
        min_candidate = candidate_name
print(min_candidate)