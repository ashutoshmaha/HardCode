#!/usr/bin/env python
# coding: utf-8

# In[67]:


import os 
import glob
import shutil 


# Task 2A,2B, 2C: sort, move and delete:

# In[ ]:


def tifproc():   
    #Task 2A(2)- sorting files by increasing file size in bytes:
    def sortup():
        allfiles = filter( os.path.isfile, glob.glob(directr + '/**/*', recursive=True)) #get files list
        allfiles2 = sorted( allfiles,key =  lambda x: os.stat(x).st_size) #get files size
        for elem in allfiles2: #print size for each file
            sortby_size  = os.stat(elem).st_size 
            print(sortby_size, elem)
            print("\n")
    sortup()      

#    Task 2A(1)- pulling all the files without file size,optional to 2A(2)
#    def dirnames():
#        directr= "C:/Users/mahaj/Downloads/co-challenge-main/co-challenge-main/2019-10-15/patch_size_128_patch_overlap_16/patches/"
#        print("Patches folder with all row offset subfolders\n")
#        for files in os.walk(directr):
#            print("\n TIF_file_folders \n", files)
#            print("\n .tif files in subsequent subfolder--> \n")
#     dirnames()
    
#     Task 2B- move all files to all_tifs:
    def moveto_alltifs():
        os.chdir("C:/Users/mahaj/Downloads/co-challenge-main/co-challenge-main/2019-10-15/patch_size_128_patch_overlap_16")
        os.mkdir("all_tifs")
        destination= r"C:/Users/mahaj/Downloads/co-challenge-main/co-challenge-main/2019-10-15/patch_size_128_patch_overlap_16/all_tifs/" + "\\"
        mystart= r"C:/Users/mahaj/Downloads/co-challenge-main/co-challenge-main/2019-10-15/patch_size_128_patch_overlap_16/patches" + "\\"
        for path, dir, files in os.walk(mystart):
            if files:
                for file in files:
                    if not os.path.isfile(destination+ file):
                        os.rename(path+ "\\"+ file, destination+ file )
    moveto_alltifs()

#      Task 2C -delete old folders     
    def deleteempty():
        tobedeleted="C:/Users/mahaj/Downloads/co-challenge-main/co-challenge-main/2019-10-15/patch_size_128_patch_overlap_16/patches"
        shutil.rmtree(tobedeleted) #remove all subfolders
    deleteemptyeteempty()

tifproc() #call to container function


# #Task 2D: moving files to folders based on band:

# In[ ]:


def bandsort():
    #create folders
    path= r"C:\Users\mahaj\Downloads\co-challenge-main\co-challenge-main\2019-10-15\patch_size_128_patch_overlap_16\all_tifs\."
    new_folders=['B02','B03','B04','B08']
    for data in range(0,4):
        if not os.path.exists(path+ new_folders[data]):
            os.makedirs(path+ new_folders[data])
            
    #root folder
    fromfolder = r"C:\Users\mahaj\Downloads\co-challenge-main\co-challenge-main\2019-10-15\patch_size_128_patch_overlap_16\all_tifs"
            
    # move files related to B02 
    targetfolder = r"C:\Users\mahaj\Downloads\co-challenge-main\co-challenge-main\2019-10-15\patch_size_128_patch_overlap_16\all_tifs\.B02\."
    patterninname = fromfolder + "\patched_sentinel_2_2019-10-15_B02*"
    for file in glob.iglob(patterninname, recursive=True):
        # extract file name from file path
        file_name = os.path.basename(file)
        shutil.move(file, targetfolder + file_name)
        print("Relocation successful for following file:-", file)
                
    # move files related to B03
    targetfolder = r"C:\Users\mahaj\Downloads\co-challenge-main\co-challenge-main\2019-10-15\atch_size_128_patch_overlap_16\all_tifs\.B03\."
    patterninname = fromfolder + "\patched_sentinel_2_2019-10-15_B03*"
    for file in glob.iglob(patterninname, recursive=True):
        file_name = os.path.basename(file)
        shutil.move(file, targetfolder + file_name)
        print("Relocation successful for following file:-", file)

    # move files related to B04
    targetfolder = r"C:\Users\mahaj\Downloads\co-challenge-main\co-challenge-main\2019-10-15\patch_size_128_patch_overlap_16\all_tifs\.B04\."
    patterninname = fromfolder + "\patched_sentinel_2_2019-10-15_B04*"
    
    for file in glob.iglob(patterninname, recursive=True):
        file_name = os.path.basename(file)
        shutil.move(file, targetfolder + file_name)
        print("MRelocationove successful for following file:-", file)
    
    # move files related to B08   
    targetfolder = r"C:\Users\mahaj\Downloads\co-challenge-main\co-challenge-main\2019-10-15\patch_size_128_patch_overlap_16\all_tifs\.B08\."
    patterninname = fromfolder + "\patched_sentinel_2_2019-10-15_B08*"
    for file in glob.iglob(patterninname, recursive=True):
        file_name = os.path.basename(file)
        shutil.move(file, targetfolder + file_name)
        print("Relocation successful for following file:-", file)
        
bandsort()


# In[2]:


#Ashutosh Mahajan

