import cv2 as cv
import numpy as np
import argparse as arg
from MainSS import Lead_RGB 
from MainSS import Lead_HSV

LH = Lead_HSV[0]
LS = Lead_HSV[1]
LV = Lead_HSV[2]
Lr = Lead_RGB[0]
Lg = Lead_RGB[1]
Lb = Lead_RGB[2]

#color area 1
if LH > 30 and LH < 43:
	#number of if and elif will be deternimed by how many tabs are in the color area
	if LH > 30 and LH < 35:
		Lead_value= 0
	elif LH >= 35 and LH <= 43:
		Lead_value= 5
	else:
		#value will be in the general range of where it is at
		Lead_value= 5
#color area 2 
elif LH > 15 and LH < 25:
	if LH >= 18 and LH <= 22  :
		Lead_value= 15 #if lower hue higher concentrate?
	elif LH >= 22 and LH <= 25:
		Lead_value= 15
	else :
		Lead_value= 15
#color area n
elif LH > 0 and LH < 10: 
	if LH > 0 and LH < 10 :
		Lead_value= 30
	else:
		Lead_value= 30
elif LH > 340 and LH < 350: 
	if LH > 340 and LH < 350:
		Lead_value= 50
	else:
		Lead_value= 50
else:
	Lead_value = [1000 ,'error. please manually inspect image for any opjects obstructing camera view or skewing color detection']
print("lead value is", Lead_value)

