import cv2 as cv
import numpy as np
import argparse as arg
from MainSS import Brom_RGB 
from MainSS import Brom_HSV 

BH = Brom_HSV[0]
BS = Brom_HSV[1]
BV = Brom_HSV[2]
Br = Brom_RGB[0]
Bg = Brom_RGB[1]
Bb = Brom_RGB[2]

#color area 1
if BH > 250 and BH <= 266: 
	Brom_value = 0 
	
#color area 2 
elif BH > 200 and BH < 210:
	
	if BS > 6 and BS <= 20:
		Brom_value= 1
	elif BS > 25 and BS <= 39:
		Brom_value= 5
	elif BS > 66 and BS <= 80:
		Brom_value= 10
	else 
		Brom_value= 20



else
	Brom_value = [1000 ,'error. please manually inspect image for any opjects obstructing camera view or skewing color detection']
