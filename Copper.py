import cv2 as cv
import numpy as np
import argparse as arg
from MainSS import Copp_RGB 
from MainSS import Copp_HSV

CH = Copp_HSV[0]
CS = Copp_HSV[1]
CV = Copp_HSV[2]
Cr = Copp_RGB[0]
Cg = Copp_RGB[1]
Cb = Copp_RGB[2]

#color area 1
if CH > 40 and CH <= 50:
	Copp_value= 0
#color area 2 
elif CH >= 30 and CH <= 40:
	Copp_value= 1
#color area n
elif CH >= 70 and CH <=80:
	Copp_value= 10
elif CH >= 200 and CH <= 212:
	Copp_value= 30
#color area n
elif CH > 212 and CH <220:
	Copp_value= 100
elif CH >=220 and CH <=230:
	Copp_value= 300
else:
	Copp_value = [1000 ,'error. please manually inspect image for any opjects obstructing camera view or skewing color detection']