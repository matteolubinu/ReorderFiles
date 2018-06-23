import time
import glob
import shutil
import os

pathToSearchIn = '/Users/matteolubinu/Downloads'

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
        newFile = ""
        newFile = divideFiles()
        if newFile.endswith('.pdf'): #PDF file if
            destination = '/Users/matteolubinu/Libri' #Change the folder destination
            shutil.move(newFile, destination)
            main()
        if newFile.endswith('.mkv') or newFile.endswith('.mp4') : #Video file if
            destination = '/Users/matteolubinu/Video' #Change the folder destination
            shutil.move(newFile, destination)
            main()
    else: 
        print ("No changes")
    sizeChecker(newFolderSize) #run again the function after time set

def divideFiles():
   latestFile = ""
   listOfFiles = glob.glob('/Users/matteolubinu/Downloads/*')
   latestFile = sorted(listOfFiles, key=os.path.getmtime)[0]
   print(latestFile)
   return latestFile
    
def main():
    folderSize = init()
    sizeChecker(folderSize)  

main()

    