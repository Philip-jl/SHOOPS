import cv2 as cv
import numpy as np
import argparse as arg
from MainSS_Clean import c1_Iron_RGB  
from MainSS_Clean import c1_Iron_HSV
from MainSS_Dirty import c2_Iron_RGB  
from MainSS_Dirty import c2_Iron_HSV

IHD = c2_Iron_HSV[0]
ISD = c2_Iron_HSV[1]
IHC = c1_Iron_HSV[0]
ISC = c1_Iron_HSV[1]


#color area 1
if IHC > 316 and IHC <= 324:

	c1_Iron_value= 0
#color area 2 
elif IHC > 351 and IHC <= 359:

	c1_Iron_value= 0.3	
elif IHC > 3 and IHC <= 11:	
	c1_Iron_value= 0.5
#color area n
elif IHC > 11 and IHC <= 20:
	if ISC > 12 and ISC <= 16:
		c1_Iron_value= 0.5
	elif ISC > 20 and ISC <= 26:
		c1_Iron_value= 1.0
	elif ISC > 33 and ISC <= 38:
		c1_Iron_value= 3.0
	else:
		c1_Iron_value = 5.0
else:
	c1_Iron_value = [1000 ,'error']


	
#color area 1
if IHD > 316 and IHD <= 324:

	c2_Iron_value= 0
#color area 2 
elif IHD > 351 and IHD <= 359:

	c2_Iron_value= 0.3	
elif IHD > 3 and IHD <= 11:	
	c2_Iron_value= 0.5
#color area n
elif IHD > 11 and IHD <= 20:
	if ISC > 12 and ISC <= 16:
		c2_Iron_value= 0.5
	elif ISC > 20 and ISC <= 26:
		c2_Iron_value= 1.0
	elif ISC > 33 and ISC <= 38:
		c2_Iron_value= 3.0
	else:
		c2_Iron_value = 5.0
else:
	c2_Iron_value = [1000 ,'error']

#print(c1_Iron_value)
#print(c2_Iron_value)
