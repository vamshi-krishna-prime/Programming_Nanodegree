# Udacity > Intro to the Programming Nanodegree >
# Python part 3 > 1. Working with Files >

# Execute as 'python -u filename.py' for unbufferred/time delayed output

'''
Program checkpoints:
1. Get a list of the file names
2. Extract the place names from the file names
3. Make a directory for each place name
4. Move files into the right directories
'''

import os


# extract places from filenames - another approach 1 (unused)
def extract_place_1(filename):
    first = filename.find("_")
    partial = filename[first+1:]
    second = partial.find("_")
    return partial[:second]


# extract places from filenames - another approach 2 (unused)
def extract_place_2(filename):
    # Get a list containing all the parts
    parts = filename.split("_")
    # Use the index operator to select the second list item
    place_name = parts[1]
    return place_name


# extract places from filenames - shortest approach (used)
def extract_place(filename):
    # handle IndexError, which is thrown if there already exists dirs
    try:
        return filename.split("_")[1]
    except IndexError:
        return filename.split("_")[0]


# make directories using the 'places' list
def make_place_directories(places):
    files = os.listdir()
    for place in places:
        # make new dir, only if another dir with same name does not exist
        if place not in files:
            os.mkdir(place)


def organize_photos(directory):
    # change the working directory to 'Photos'
    os.chdir(directory)

    # 1. List the files in the 'Photos' directory and assign them to a variable
    originals = os.listdir()

    # 2. Extract the place names from the file names
    places = []
    for filename in originals:
        place = extract_place(filename)
        # avoid duplicating place names
        if place not in places:
            places.append(place)

    # 3. Make a directory for each place name
    make_place_directories(places)

    # 4. Move files into the right directories
    for filename in originals:
        place = extract_place(filename)
        # only move the pictures but not dirs if exist
        if '.jpg' in filename:
            os.rename(filename, os.path.join(place, filename))


if __name__ == '__main__':
    organize_photos("Photos")
