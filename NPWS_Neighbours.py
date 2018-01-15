import arcpy
from arcpy import env
import time

arcpy.env.overwriteOutput = True

basedir = 'B:\\NPWS_neighbours\\FGDB\\NPWS_Neighbours.gdb\\'
clip_estate = basedir + 'estate'
region_select = basedir + 'region'
buffer_out = basedir + 'buffer'
holding_clip = basedir + 'holding'

#datasets
region = 'P:\LLS_Data\Working Data\Corporate.gdb\NPWS_Boundary\NPWS_Areas'
estate = 'P:\LLS_Data\Working Data\Working_data.gdb\Parks\National_Parks_June_2015_1_Clip'
holding ='C:\Database_connections\GIS101Delivery_Restricted.sde\GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS'

#process
arcpy.MakeFeatureLayer_management (region, "region_lyr")
arcpy.SelectLayerByAttribute_management ('region_lyr', "NEW_SELECTION","NAME = 'Northern Tablelands'")
arcpy.CopyFeatures_management('region_lyr', region_select)
arcpy.SelectLayerByAttribute_management('region_lyr', "CLEAR_SELECTION")
arcpy.Clip_analysis(region_select,estate, clip_estate,)
arcpy.Buffer_analysis(clip_estate, buffer_out, "3000 METERS", "FULL", "ROUND", "ALL")
arcpy.Clip_analysis(holding, buffer_out, holding_clip)

