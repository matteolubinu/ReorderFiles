import time
import glob
import shutil
import os

path = '/Users/matteolubinu'
pathToSearchIn = path+'/Downloads'

def init():
    folderSize = len([file for file in glob.glob(glob.escape(pathToSearchIn) + '/**/*', recursive=True)])
    return folderSize

def sizeChecker(folderSize):
    oldFolderSize = folderSize
    print("Folder size (old size):" , oldFolderSize , "Elements" )
    time.sleep(10) #in seconds
    newFolderSize = len([file for file in glob.glob(glob.escape(pathToSearchIn) + '/**/*', recursive=True)])
    print("Folder size (new size):" , newFolderSize , "Elements")
    if newFolderSize > oldFolderSize:
        print ("Changes detected")
        reOrderFiles()
    else: 
        print ("No changes")
    sizeChecker(newFolderSize) #run again the function after time set

def divideFiles():
   latestFile = ""
   listOfFiles = glob.glob(pathToSearchIn+'/*')
   latestFile = max(listOfFiles, key=os.path.getmtime)
   print(latestFile)
   return latestFile

def reOrderFiles():
    newFile = divideFiles()
    #PDF files
    if newFile.endswith('.pdf'): 
            destination = path+'/Libri' #change the folder destination (Must NOT be a system directory)
            shutil.move(newFile, destination)
            main()
    #Image files
    if newFile.endswith('.png') or newFile.endswith('.jpeg') or newFile.endswith('.jpg') : 
            destination = path+'/Immagini' #change the folder destination (Must NOT be a system directory)
            shutil.move(newFile, destination)
            main()
    #Video files
    if newFile.endswith('.mkv') or newFile.endswith('.mp4'): 
            destination = path+'/Anime' #change the folder destination (Must NOT be a system directory)
            shutil.move(newFile, destination)
            main()
    
def main():
    folderSize = init()
    sizeChecker(folderSize)  

inputUser = input("Do you also want to reorder the files already present in the folder? [y/n] ")
if (inputUser == "y"):
    reOrderFiles()
else:
    main()

    