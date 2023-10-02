import os
from os import listdir
from os.path import isfile, join, exists
import sys

import DLFuncs

#Path to Downloads folder
path = "C:\\Users\\Markku\\Downloads\\"
target_path:str = "C:\\Users\\Markku\\CleanDownload\\"
extensions:str

#Create file named FILES MOVED TO CLEAN DOWNLOADS.txt to variable path folder
if not os.path.exists(path + "FILES MOVED TO CLEAN DOWNLOADS.txt"):
    open(path + "FILES MOVED TO CLEAN DOWNLOADS.txt","w+")

#Error check paths
if not exists(path) or not exists(target_path):
    print("Error! One of the paths specified does not exist")
    exit()

#Create folder structure for files to live in
DLFuncs.createFolderStructure(target_path)

for file in DLFuncs.fileInDirectory(path):
    
    #Move images
    extensions = [".jpg",".png",".gif",".webp",".ico"]
    for extension in extensions:
        if file.endswith(extension):
            DLFuncs.moveFile(path + file,target_path + "Images\\" + file)

    #Move videos
    extensions = [".mp4",".avi",".mpg",".mpeg"]
    for extension in extensions:
        if file.endswith(extension):
            DLFuncs.moveFile(path + file,target_path + "Videos\\" + file)

    #Move executables
    extensions = [".exe",".msi"]
    for extension in extensions:
        if file.endswith(extension):
            DLFuncs.moveFile(path + file,target_path + "Executables\\" + file)

    #Move zips
    extensions = [".zip","rar",".tar"]
    for extension in extensions:
        if file.endswith(extension):
            DLFuncs.moveFile(path + file,target_path + "Zips\\" + file)

    #Move music
    extensions = [".mp3","wav"]
    for extension in extensions:
        if file.endswith(extension):
            DLFuncs.moveFile(path + file,target_path + "Music\\" + file)
    


