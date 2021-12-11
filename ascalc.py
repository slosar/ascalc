#!/usr/bin/env python
from math import *
from astropy.units import *
from astropy.constants import *

import astropy.units as unitsmod
import readline
import re as regexp

# now get the list of all units (so that we can process 10K into 10*K)
# units string themselves into units
units = []
for un in dir(unitsmod):
    if eval(f'str(unitsmod.{un})=="{un}"'):
        units.append(un)
units.sort(key=len,reverse=True)

while True:
    text = input('> ')
    for un in units:
        text = regexp.sub(f"[0123456789 ]{un}",
                          lambda x:x[0][0]+f"*({un})",text)
    try:
        result = eval(text)
        print(" = ",result.si)
    except:
        print (" Error.")
