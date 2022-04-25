from contextlib import AbstractAsyncContextManager
from re import A
import cv2 as cv
import numpy as np
import argparse as arg
import MainSS_Clean as MC
import MainSS_Dirty as MD
import Bromine as Brom
import Copper as Copp
import Iron
import Lead as Lead
import Mercury as Merc
import Ph 



List_of_Clean_Values = [Ph.c1_Ph_value,Iron.c1_Iron_value,Lead.c1_Lead_value,Copp.c1_Copp_value,Merc.c1_Merc_value,Brom.c1_Brom_value]
List_of_Dirty_Values = [Ph.c2_Ph_value,Iron.c2_Iron_value,Lead.c2_Lead_value,Copp.c2_Copp_value,Merc.c2_Merc_value,Brom.c2_Brom_value]

print(*MC.clc, sep = "\n")
print(*MD.cld, sep = "\n")
print(*List_of_Clean_Values, sep = "\n")
print(*List_of_Dirty_Values, sep = "\n")
