from contextlib import AbstractAsyncContextManager
from re import A
import cv2 as cv
import numpy as np
import argparse as arg
import MainSS 
import Aluminium as Alum
import Bromine as Brom
import Copper as Copp
import Iron
import Lead as Lead
import Mercury as Merc
import Ph 
import Sulfate as Sulf

List_of_Values = [Ph.Ph_value,Iron.Iron_value,Lead.Lead_value,Copp.Copp_value,Alum.Alum_value,Merc.Merc_value,Sulf.Sulf_value]
