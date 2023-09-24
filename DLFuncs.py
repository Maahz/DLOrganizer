import os
import sys
import shutil
from os import listdir
from os.path import isfile, join

#List files in a specific directory
def fileInDirectory(directory: str):
    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
    return(onlyfiles)

#Move files to where they belong
def moveFile(file: str, target: str):
    #If file already exists return and dont do anything
    if os.path.exists(target):
        print(target + " file already exists!")
        return
    
    #Otherwise copy the file and then REMOVE THE ORIGINAL
    shutil.copy(file,target)
    os.remove(file)
    

#Create folder structure for files to be put in
def createFolderStructure(path: str):

    #List folders to create
    folders = ["Videos","Images", "Executables", "Zips","Music"]

    #Create said folders
    for folder in folders:
        if not os.path.exists(path + folder):
            os.mkdir(path + folder)