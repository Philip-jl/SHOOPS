import cv2 as cv
import numpy as np
import argparse as arg
from MainSS_Dirty import c2_Lead_RGB 
from MainSS_Dirty import c2_Lead_HSV
from MainSS_Clean import c1_Lead_RGB 
from MainSS_Clean import c1_Lead_HSV

LHC = c1_Lead_HSV[0]
LHD = c2_Lead_HSV[0]


#color area 1
if LHC > 30 and LHC < 43:
	#number of if and elif will be deternimed by how many tabs are in the color area
	if LHC > 27 and LHC < 35:
		c1_Lead_value= 0
	elif LHC >= 35 and LHC <= 43:
		c1_Lead_value= 5
	else:
		#value will be in the general range of where it is at
		c1_Lead_value= 5
#color area 2 
elif LHC > 11 and LHC < 26:
	if LHC >= 18 and LHC <= 22  :
		c1_Lead_value= 15 #if lower hue higher concentrate?
	elif LHC >= 22 and LHC <= 25:
		c1_Lead_value= 15
	else :
		c1_Lead_value= 15
#color area n
elif LHC > 0 and LHC < 10: 
	if LHC > 0 and LHC < 10 :
		c1_Lead_value= 30
	else:
		c1_Lead_value= 30
elif LHC > 340 and LHC < 350: 
	if LHC > 340 and LHC < 350:
		c1_Lead_value= 50
	else:
		c1_Lead_value= 50
else:
	c1_Lead_value = [1000 ,'error']




#color area 1
if LHD > 30 and LHD < 43:
	#number of if and elif will be deternimed by how many tabs are in the color area
	if LHD > 30 and LHD < 35:
		c2_Lead_value= 0
	elif LHD >= 35 and LHD <= 43:
		c2_Lead_value= 5
	else:
		#value will be in the general range of where it is at
		c2_Lead_value= 5
#color area 2 
elif LHD > 15 and LHD < 25:
	if LHD >= 18 and LHD <= 22  :
		c2_Lead_value= 15 #if lower hue higher concentrate?
	elif LHD >= 22 and LHD <= 25:
		c2_Lead_value= 15
	else :
		c2_Lead_value= 15
#color area n
elif LHD > 0 and LHD < 10: 
	if LHD > 0 and LHD < 10 :
		c2_Lead_value= 30
	else:
		c2_Lead_value= 30
elif LHD > 340 and LHD < 350: 
	if LHD > 340 and LHD < 350:
		c2_Lead_value= 50
	else:
		c2_Lead_value= 50
else:
	c2_Lead_value = [1000 ,'error']

#print(c1_Lead_value)
#print(c2_Lead_value)

