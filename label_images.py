import argparse
import pandas as pd
from image_labeling import label_images

def main (args):

    if args.images_location in ['Eindhoven']:
        path = './data/images/Eindhoven_Flower_DataSet_2021/'
    if args.data_name in ['flowers']:
        data = pd.read_excel('./data/datasets/Flower Details.xlsx')

    label_images(path, data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--images_location',
        choices=['Eindhoven'],
        default='Eindhoven',
        type=str)
    parser.add_argument(
        '--data_name',
        choices=['flowers'],
        default='flowers',
        type=str)

    args = parser.parse_args()

    main(args)