#!/usr/bin/env python

import numpy as np
import bottleneck as bn
from lolpython import lol_py 

a = np.array([1, 2, np.nan, 4, 5])
b = bn.nanmean(a)

print(b)

lol_py("It worked........")
