import cv2 as cv
import numpy as np
import argparse as arg
from MainSS_Dirty import c2_Brom_RGB 
from MainSS_Dirty import c2_Brom_HSV 
from MainSS_Clean import c1_Brom_RGB 
from MainSS_Clean import c1_Brom_HSV 

BHC = c1_Brom_HSV[0]
BSC = c1_Brom_HSV[1]
BHD = c2_Brom_HSV[0]
BSD = c2_Brom_HSV[1]


#color area 1
if BHC > 250 and BHC <= 266: 
	c1_Brom_value = 0 	
#color area 2 
elif BHC > 200 and BHC < 210:
	
	if BSC > 6 and BSC <= 20:
		c1_Brom_value= 1
	elif BSC > 25 and BSC <= 39:
		c1_Brom_value= 5
	elif BSC > 66 and BSC <= 80:
		c1_Brom_value= 10
	else:
		c1_Brom_value= 20
else:
	c1_Brom_value = [1000 ,'error']


#color area 1
if BHD > 250 and BHD <= 266: 
	c2_Brom_value = 0 	
#color area 2 
elif BHD > 200 and BHD < 210:
	
	if BSD > 6 and BSD <= 20:
		c2_Brom_value= 1
	elif BSD > 25 and BSD <= 39:
		c2_Brom_value= 5
	elif BSD > 66 and BSD <= 80:
		c2_Brom_value= 10
	else:
		c2_Brom_value= 20
else:
	c2_Brom_value = [1000 ,'error']

#print(c1_Brom_value)
#print(c2_Brom_value)