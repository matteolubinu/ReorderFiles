import os
import time

def init():
    folderSize = os.path.getsize("C:/Users/IBM_ADMIN/Downloads")
    return folderSize

def sizeChecker(folderSize=null, newFolderSize):
    
    if folderSize:
        oldFolderSize = folderSize
    if newFolderSize:
        oldFolderSize = newFolderSize
    print("Folder size (old data):" , folderSize/1073741824 , "Gb")
    time.sleep(10) #in seconds
    newFolderSize = os.path.getsize("C:/Users/IBM_ADMIN/Downloads")
    
    print("Folder size (new data):" , newFolderSize/1073741824 , "Gb")
    if newFolderSize > oldFolderSize:
        print ("Changes detected")
    return newFolderSize
    sizeChecker(newFolderSize) #run again the function after time set

init()
sizeChecker()  
    