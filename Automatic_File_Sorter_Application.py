#!/usr/bin/env python
# coding: utf-8

# # Automatic File Sorter Functions.py

# In[4]:


#importing some important libraries for OS interaction as well as a user input function which better handles raw inputs
#pip install pyinstaller
import os, shutil
from six.moves import input
import pandas as pd


# In[5]:


## Small function to take in a the directory info dataframe and create the folders needed based on all file types
def folder_maker(path, directory_info):
    
    folders = directory_info['Folder Name'].unique()
    
    for folder in folders:
        folder_path = os.path.join(path,folder)
        if not(os.path.exists(folder_path)):
            os.makedirs(folder_path)
            print(f"{folder} folder made")
        else:
            print(f"{folder} Already exists!")
            continue


# In[6]:


## Small function to execute the move of the files into their respective folders, takes in the directory info df again

def sort_files(path, directory_info):    
    for i,j in directory_info.iterrows():
        source_folder = os.path.join(path,j['File Name'])
        destination_folder = os.path.join(path,(j['Folder Name']),(j['File Name']))
        
        if(j['File Type'] in j['File Name']):
            if not (os.path.exists(destination_folder)):
                shutil.move(source_folder, destination_folder)
                print(f"Moved: {j['File Name']} to {j['Folder Name']}")
            
            else:
                print(f"Skipped: {j['File Name']} - Already exists in proper destination")
        else:
            print(f"Skipped: {j['File Name']} - Not designated as a file to be moved")


# In[19]:


## Essentially the main function which will take in the user directory and create the df with info. 
## It will pass the info to the folder maker function and then again to the official sorter function.

def file_sorter():
    path = input("Enter your Folder path:")
    
    if not path.endswith(os.sep):
        path += os.sep
    
    if not os.path.exists(path):
        print("Error: Directory does not exist! Please Try Again.")
        return
    
    files_in_dir = os.listdir(path)
    
    # Creating a small dataframe containing the files in the directory, their respective types & folders to sort them into
    directory_info = []
    
    for i in files_in_dir:
        try: 
            file_type = i.split('.')[1]
            folder_name = (file_type + ' files')
            folder_info = ({"File Name": i,
                               "File Type": file_type,
                               "Folder Name": folder_name})
            directory_info.append(folder_info)
        
        except IndexError:
            print(f"Skipped: {file_name} (No File Extension exists here)")
            continue
        
    if not directory_info:
        print("No files found to sort!")
        return
    
    directory_info = pd.DataFrame(directory_info)
    
    continue_check = input("Fully prepared to sort - Type Yes to continue\n").upper()
    
    if continue_check == "YES":
        pass
    else:
        print("Exiting program. Please try again if you exited by mistake.")
        return
    
    print("\nCreating Folders")
    folder_maker(path, directory_info)
    
    print("\nSorting Files")
    sort_files(path, directory_info)
    
    print("\nFile Sorting has completed Succesfully")
    input("Press Enter to exit...")


# In[20]:


def main():
    try:
        file_sorter()
    except KeyboardInterrupt:
        print("\nOperation was cancelled or user error occured.")
    except Exception as e:
        print(f"\nAn error has occured: {e}")


# In[22]:


if __name__ == "__main__":
    main()

