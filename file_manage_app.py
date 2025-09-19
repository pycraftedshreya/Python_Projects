import os 
import shutil 

# Get the path from user
path = input("Enter your path (remove \"\" quotes): ")

# List of files and directories
files = os.listdir(path)

for i in files:
    file_path = os.path.join(path,i)
    
    if os.path.isfile(file_path):
      filename , extension  = os.path.splitext(i)
      extension_1 = extension[1:] if extension else "Others"
    
    folder_path = os.path.join(path, extension_1)
    
    if  not os.path.exists(folder_path):    
        # create the folder
        os.makedirs(folder_path)

    # move the file to the folder
    shutil.move(file_path, os.path.join(folder_path,i))
