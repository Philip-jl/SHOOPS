import cv2 as cv
import numpy as np
import argparse as arg
from MainSS import Alum_RGB
from MainSS import Alum_HSV 

AH = Alum_HSV[0]
AS = Alum_HSV[1]
AV = Alum_HSV[2]
Ar = Alum_RGB[0]
Ag = Alum_RGB[1]
Ab = Alum_RGB[2]

if AH >= and AH <= :

elif AH >= and AH <= :

else:
	Alum_value = [1000 ,'error. please manually inspect image for any opjects obstructing camera view or skewing color detection']
