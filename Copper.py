import cv2 as cv
import numpy as np
import argparse as arg
from MainSS_Clean import c1_Copp_HSV  
from MainSS_Dirty import c2_Copp_HSV

CHC = c1_Copp_HSV[0]
CHD = c2_Copp_HSV[0]

#color area 1
if CHC > 40 and CHC <= 50:
	c1_Copp_value= 0
#color area 2 
elif CHC >= 30 and CHC <= 40:
	c1_Copp_value= 1
#color area n
elif CHC >= 70 and CHC <=80:
	c1_Copp_value= 10
elif CHC >= 200 and CHC <= 212:
	c1_Copp_value= 30
#color area n
elif CHC > 212 and CHC <220:
	c1_Copp_value= 100
elif CHC >=220 and CHC <=230:
	c1_Copp_value= 300
else:
	c1_Copp_value = [1000 ,'error']

#color area 1
if CHD > 40 and CHD <= 50:
	c2_Copp_value= 0
#color area 2 
elif CHD >= 30 and CHD <= 40:
	c2_Copp_value= 1
#color area n
elif CHD >= 70 and CHD <=80:
	c2_Copp_value= 10
elif CHD >= 200 and CHD <= 212:
	c2_Copp_value= 30
#color area n
elif CHD > 212 and CHD <220:
	c2_Copp_value= 100
elif CHD >=220 and CHD <=230:
	c2_Copp_value= 300
else:
	c2_Copp_value = [1000 ,'error']

#print(c1_Copp_value)
#print(c2_Copp_value)