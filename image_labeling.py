import os
from os import listdir


# taking the photo ids
def get_photo_ids(data):
    # initializing an empty array
    photo_ids = []
    
    # adding all ids to the array
    for i in range(len(data)):
        current_id = data.iloc[i, 0]
        # adding .JPG to the photo id so it matches with the id of the photo
        photo_ids.append(str(current_id) + '.JPG')
    
    return photo_ids


# taking the english name of each flower
def get_eng_names(data):
    # initializing an empty array
    names = []
    
    # adding all names to the array
    for i in range(len(data)):
        current_name = data.iloc[i, 3]
        names.append(current_name)
    return names


def get_unique_names(data):
    # getting the english names
    eng_names = get_eng_names(data)

    # initialize an empty array for the unique values
    unique_names = []

    # traverse for all elements
    for x in eng_names:
        # check if exists in unique_names or not
        if x not in unique_names:
            unique_names.append(x)

    return unique_names


def to_one_folder(path):
    
    # loading the images 
    images = listdir(path)
    
    # looping through all three dates 
    for i in range(len(images)):
        new_path = os.path.join(path, images[i])
        new_images = listdir(new_path)
        # looping though each folder for each date
        for j in range(len(new_images)):
            current_path = os.path.join(new_path, new_images[j])
            current_images = listdir(current_path)
            # moving the images to the parent directory and deleting the previous two
            for img in current_images:
                os.rename(current_path + '/' + img, path + img)
            os.rmdir(current_path)
        os.rmdir(new_path)


def check_data_for_missing_photos(path, data):
    
    # checking tha data for duplicating ids (the original and the copy)
    if data['Photo ID'].duplicated().sum() > 0:
        # saving the duplicated entries so they can be examinied 
        duplicates = data[data['Photo ID'].duplicated(keep=False)]
        duplicates.to_csv('./data/duplicated_photo_ids.csv')
        # Dropping the duplicated entries
        entries_to_drop = data[data['Photo ID'].duplicated(keep='first')].index
        data.drop(entries_to_drop, axis=0, inplace=True)
        print('Not all ids were unique. Only the first instances were kept. Find the duplicated ids by loading duplicated_photo_ids.csv\n')
        #raise Exception('Not all ids are unique. See the duplicated ids by loading duplicated_photo_ids.csv.')
   
    photo_ids = get_photo_ids(data)
    
    extra_images = []
    images = listdir(path)
    
    for img in images:
         if img not in photo_ids:
            extra_images.append(img)
    
    if len(extra_images) == 0:
        print('There are no extra photos\n')
    else:
        # Drop the extra images and add them in separate folder
        destination = './data/Extra images/'
        isDir = os.path.isdir(destination)
        if not isDir:
            os.mkdir(destination)
        for i in extra_images:
            for j in images:
                if i == j:
                    os.rename(path + i, destination + i)
            else:
                continue
        print(f'There were {len(extra_images)} extra photos that are not in the dataset. They have been moved to data/Extra images. \n')
        return extra_images


# Function that renames the images by adding their english name to the photo id
def rename_images(path, data):
    # loading the images
    images = listdir(path)
    
    # taking all photo ids
    photo_ids = get_photo_ids(data)
    
    # taking the english name of each flower
    names = get_eng_names(data)

    new_captions = []
    for i in range(len(images)):
        for j in range(len(photo_ids)):
            if images[i] == photo_ids[j]:
                caption = names[j] + images[i]
                original_path = os.path.join(path, images[i])
                new_path = os.path.join(path, caption)
                os.replace(original_path, new_path)


def label_images(path, data):

    to_one_folder(path)

    extra_images = check_data_for_missing_photos(path, data)

    rename_images(path, data)

    # load the images
    images = listdir(path)
    
    # get the unique names of the flowers
    u_names = get_unique_names(data)
    
    # taking all photo ids
    photo_ids = get_photo_ids(data)
  
    # create a directory for each name and move the corresponding pictures to the new directories
    for u_n in u_names:
        for img in images:
            for ids in photo_ids:
                if u_n + ids == img:
                    destination = os.path.join(path, u_n)
                    isDir = os.path.isdir(destination)
                    if isDir:
                        # add / to the unique names to they can be used as directories
                        os.rename(path + img, destination + '/' + img)
                    else:
                        os.mkdir(destination)
                        os.rename(path + img, destination + '/' + img)

    print('Labeling has finished!')


