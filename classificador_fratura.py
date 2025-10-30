import os
import pathlib
import nrrd # pip install pynrrd
import matplotlib.pyplot as plt

imgs_path = pathlib.Path('./images')

for file_name in os.listdir(imgs_path):
    print(file_name)

seg_folder = '3-Segmentation_NRRD'
seg_path = imgs_path / seg_folder

masks = {}
masks_header = {}

# Preenchendo os dicionarios masks e masks_header

for file_name in os.listdir(seg_path):
    if(file_name.endswith('.nrrd')):
        file_path = str(seg_path / file_name)
        start = file_path.index(file_name)
        end = file_path.index('.seg.nrrd')
        mask_id = file_path[start:end]
        masks[mask_id], masks_header[mask_id] = nrrd.read(file_path)


plt.imshow(masks['P1L1'][:,:,0], cmap='gray')



rescaled_folder = '2-Rescaled_256_NRRD'
rescaled_imgs = imgs_path / rescaled_folder
images = {}
rescaled_imgs

for img_name in os.listdir(rescaled_imgs):
    if(file_name.endswith('.nrrd')):
        img_path = str(rescaled_imgs / img_name)
        start = img_path.index(img_name) 
        end = img_path.index('.nrrd')
        pacient_id = img_path[start:end]
        images[pacient_id] = nrrd.read(img_path)[0]


plt.imshow(images['P1'][:,:,5], cmap='gray')
