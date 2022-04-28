import cv2 as cv
import numpy as np
import argparse as arg
from MainSS_Dirty import c2_Merc_RGB
from MainSS_Dirty import c2_Merc_HSV
from MainSS_Clean import c1_Merc_RGB
from MainSS_Clean import c1_Merc_HSV

MHC = c1_Merc_HSV[0]
MSC = c1_Merc_HSV[1]
MVC = c1_Merc_HSV[2]
MrC = c1_Merc_RGB[0]
MgC = c1_Merc_RGB[1]
MbC = c1_Merc_RGB[2]

MHD = c2_Merc_HSV[0]
MSD = c2_Merc_HSV[1]
MVD = c2_Merc_HSV[2]
MrD = c2_Merc_RGB[0]
MgD = c2_Merc_RGB[1]
MbD = c2_Merc_RGB[2]

#color area 1
if MHC >= 315 and MHC <= 325:
	if MHC >= 315 and MHC <= 325:
		c1_Merc_value= 0
	else:
		c1_Merc_value= 0
#color area 2 
elif MHC >= 213 and MHC <= 217:
	if MHC >= 213 and MHC <= 217:
		c1_Merc_value= 0.002
	else:
		c1_Merc_value= 0.002
elif MHC >= 277 and MHC <= 293:
	if MgC >= 160 and MgC <= 170:
 		c1_Merc_value = 0.005
	elif MgC >= 140 and MgC <= 150:
		c1_Merc_value = 0.01
	elif MgC >= 90 and MgC <= 110:
		c1_Merc_value = 0.02
	else:
		c1_Merc_value=0.02
elif MHC >= 240 and MHC <= 260:
	if MrC <= 90 and MrC >= 103:
		c1_Merc_value = 0.04
	elif MrC <= 48 and MrC >= 60:
		c1_Merc_value = 0.08
	else:
		c1_Merc_value=0.08
else:
	c1_Merc_value = [1000 ,'error']


#color area 1
if MHD >= 315 and MHD <= 325:
	if MHD >= 315 and MHD <= 325:
		c2_Merc_value= 0
	else:
		c2_Merc_value= 0
#color area 2 
elif MHD >= 213 and MHD <= 217:
	if MHD >= 213 and MHD <= 217:
		c2_Merc_value= 0.002
	else:
		c2_Merc_value= 0.002
elif MHD >= 277 and MHD <= 293:
	if MgD >= 160 and MgD <= 170:
 		c2_Merc_value = 0.005
	elif MgD >= 140 and MgD <= 150:
		c2_Merc_value = 0.01
	elif MgD >= 90 and MgD <= 110:
		c2_Merc_value = 0.02
	else:
		c2_Merc_value=0.02
elif MHD >= 240 and MHD <= 260:
	if MrD <= 90 and MrD >= 103:
		c2_Merc_value = 0.04
	elif MrD <= 48 and MrD >= 60:
		c2_Merc_value = 0.08
	else:
		c2_Merc_value=0.08
else:
	c2_Merc_value = [1000 ,'error']

#print(c1_Merc_value)
#print(c2_Merc_value)