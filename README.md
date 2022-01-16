# Flower Power III 
Veneta Angelova, Lia Boyadzhieva, Kristina Krasteva, Filip Vangelov
#### [DEX](https://dex.software/project/details/172-Flower-Power-III)

## Goal 
The goal of the project is to monitor and differentiate between different types of flower species over large areas, which would have a great impact on biodiversity and ecosystem related complications. 

## Data
For this project, the Big Data Lectoraat provided our team with a dataset containing approximately 11GB of image data of flower species alongside an Excel sheet providing additional information regarding each image. The image dataset can be found on the Fontys Research Drive. The spreadsheet can be found in several of the folders of this project (the original one -> [**data/datasets/Eindhoven Flower Dataset 2021 WiP.xlsx**](https://github.com/krisxtinaa/flower-power/blob/main/data/datasets/Eindhoven%20Flower%20Dataset%202021%20WiP.xlsx) & the processed one -> [**Data_Preparation/Flowers-new.xlsx**](https://github.com/krisxtinaa/flower-power/blob/main/Data_Preparation/Flowers-new.xlsx)). Additionally, the cropped images of the 30 flower species that were used for training can be found in [**CNN_model/Flower-Data_CNN**](https://github.com/krisxtinaa/flower-power/tree/main/CNN_models/Flower-Data_CNN).

## Structure 
The 3 branches currently in use are **main, develop and cnn** and main is up-to-date, meaning all information from the other branches (also the deleted ones is already merged). The following folders exist: 
- data -> the original [Excel sheet](https://github.com/krisxtinaa/flower-power/blob/main/data/datasets/Eindhoven%20Flower%20Dataset%202021%20WiP.xlsx) stored in a subfolder called datasets

- Label_Images -> [Jupyter notebook](https://github.com/krisxtinaa/flower-power/blob/main/Label_Images/image_labeling_prototype.ipynb) & [Python version](https://github.com/krisxtinaa/flower-power/blob/main/Label_Images/image_labeling.py) for reorganizing the image dataset by storing the images by the english name (this code is also present in one of the Data Preparation notebooks) 

- EDA -> 1 notebook [EDA_FlowerPower.ipynb](https://github.com/krisxtinaa/flower-power/blob/main/EDA/EDA_FlowerPower.ipynb) with the EDA and visualizations we performed + a processed excel file [Flowers-new.xlsx](https://github.com/krisxtinaa/flower-power/blob/main/EDA/Flowers-new.xlsx) and the [html](https://github.com/krisxtinaa/flower-power/blob/main/EDA/EDA_FlowerPower.html) version of the notebook

- Data_Preparation -> 1 notebook [Data_Preparation.ipynb](https://github.com/krisxtinaa/flower-power/blob/main/Data_Preparation/Data_Preparation.ipynb) where the data was preprocessed (the label images code is also included in this notebook), the [html](https://github.com/krisxtinaa/flower-power/blob/main/Data_Preparation/Data_Preparation.html) version of the notebook + [the final Excel file](https://github.com/krisxtinaa/flower-power/blob/main/Data_Preparation/Flowers-new.xlsx). Additionally, the output from the notebook (Extra images folder and duplicated_photo_ids.csv are present, but they could be generated again by running the above mentioned Data Preparation notebook). 

- Crop_Images -> the automated cropping approach [Crop images by HSV.ipynb](https://github.com/krisxtinaa/flower-power/blob/main/Crop_Images/Crop%20images%20by%20HSV.ipynb) + the old version with [RGB](https://github.com/krisxtinaa/flower-power/blob/main/Crop_Images/crop_images_F.ipynb) and [HSV](https://github.com/krisxtinaa/flower-power/blob/main/Crop_Images/crop_images_D.ipynb) color detection. 

- CNN_models -> 1 folder for the [Faster R-CNN](https://github.com/krisxtinaa/flower-power/tree/main/CNN_models/Faster%20R-CNN) where the notebook and model are present; the cropped images of the 30 flower species [Flower-Data_CNN](https://github.com/krisxtinaa/flower-power/tree/main/CNN_models/Flower-Data_CNN) which is used for the [custom model](https://github.com/krisxtinaa/flower-power/blob/main/CNN_models/CNN%20on%2030%20flowers.ipynb) + [html version](https://github.com/krisxtinaa/flower-power/blob/main/CNN_models/CNN%20on%2030%20flowers.html) and the [pre-trained model](https://github.com/krisxtinaa/flower-power/blob/main/CNN_models/CNN_pretrained.ipynb) + [html version](https://github.com/krisxtinaa/flower-power/blob/main/CNN_models/CNN_pretrained.html); one folder with older experiments on the models.

## Conclusion 
We would recommend getting familiar with all of the models since they approach the problem in different ways, however the following things have to be considered:
 - for the faster r-cnn manually labeled data and a powerful PC are needed (trained on 5 species) 
 - for the custom model more in-depth research on adding more layers is needed (78% val accuracy)
 - for the pre-trained model further experiments are needed with more species or trying different pre-trained models i.e., VGG-16 (98% val accuracy)
