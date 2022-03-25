import cv2 as cv
import numpy as np
import argparse as arg
from MainSS import Iron_RGB  
from MainSS import Iron_HSV

IH = Iron_HSV[0]
IS = Iron_HSV[1]
IV = Iron_HSV[2]
Ir = Iron_RGB[0]
Ig = Iron_RGB[1]
Ib = Iron_RGB[2]

#color area 1
if IH > 316 and IH <= 324

	Iron_value= 0
	
#color area 2 
elif IH > 351 and IH <= 359	

	Iron_value= 0.3
	
elif IH > 3 and IH <= 11	

	Iron_value= 0.5
#color area n
elif IH > 11 and IH <= 20
	if IS > 12 and IS <= 16
		Iron_value= 0.5
	elif IS > 20 and IS <= 26
		Iron_value= 1.0
	elif IS > 33 and IS <= 38
		Iron_value= 3.0
	else 
		Iron_value = 5.0

else
	Iron_value = [1000 ,'error. please manually inspect image for any opjects obstructing camera view or skewing color detection']
