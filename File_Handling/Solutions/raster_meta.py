#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Conda environment created as 'myenv'


# In[2]:


#Checking raster properties:

from osgeo import gdal

file_loc= r"C:\Users\mahaj\Downloads\co-challenge-main\co-challenge-main\2019-10-15\patch_size_128_patch_overlap_16\all_tifs\.B02\.patched_sentinel_2_2019-10-15_B02_10m_33_N578_W06_1000cm_roff_0_coff_0.tif"
tif_analysis= gdal.Open(file_loc) #read tif
type(tif_analysis) #check file's type


# In[3]:


print("X Dimention: ",tif_analysis.RasterXSize) #get dimentions 


# In[4]:


print("Y Dimention: ",tif_analysis.RasterYSize) #get dimentions 


# In[5]:


tif_analysis.GetProjection() #get projection


# In[6]:


print("Metadata is as follows:")
tif_analysis.GetMetadata() #get details of data


# In[7]:


print(" Fetching raster count: ", tif_analysis.RasterCount) #get no. of raters


# In[8]:


tif_band= tif_analysis.GetRasterBand(1) #get raster band 
gdal.GetDataTypeName(tif_band.DataType) #know datatype of band values


# In[9]:


type(tif_band) #getting type of that band


# In[10]:


#Processing values of band

if tif_band.GetMinimum() is None or tif_band.GetMaximum() is None: #computing stats in case required
    tif_band.ComputeStatistics(0)
    print("Optional stats are calculated!") #print will function if stats are fetched 


# In[11]:


#get details of band data
print("Following information is the Metadata for this band:\n\n ",tif_band.GetMetadata()) 


# In[17]:


print (" NO DATA VALUE FOR BAND ---> ", tif_band.GetNoDataValue()) # none
print (" MIN VAL ---> ", tif_band.GetMinimum())
print (" MAX VAL ---> ", tif_band.GetMaximum())


# In[18]:


#Raster's pixel resolution:

myraster = gdal.Open(file_loc)

geo_coord =myraster.GetGeoTransform()
print("File's transformed geographical co-ordinates are: ",geo_coord)

pxl_SizeX = geo_coord[1]
pxl_SizeY =-geo_coord[5]

print("X value--->",pxl_SizeX)
print("Y value--->",pxl_SizeY)


# In[13]:


#Saving this file as raster_meta.ipynb and reading it in JSON if needed-->


# In[14]:


import json 

with open("raster_meta.ipynb", mode= "r", encoding= "utf-8") as rast:
    raster_meta = json.loads(rast.read()) 
    print(raster_meta)
    
# .ipynb is itself an encoded .json file which can be converted to other formats like .py easily. 


# In[19]:


#Ashutosh Mahajan


# In[ ]:





# In[ ]:





# In[16]:





# In[ ]:




