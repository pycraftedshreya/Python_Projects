import os 
import shutil 

# Get the path from user
path = input("Enter your path (remove \"\" quotes): ")

# List of files and directories
files = os.listdir(path)

for i in files:
    filename , extension  = os.path.splitext(i)
    extension_1 = extension[1:]
    folder_path = path+"\\"+extension_1
    if os.path.exists(folder_path):    
        # move the file to the folder
        shutil.move(path+"\\"+i, path+"\\"+extension_1+"\\"+i)
    else:
        # create the folder
        os.makedirs(folder_path)
        shutil.move(path+"\\"+i, path+"\\"+extension_1+"\\"+i)
