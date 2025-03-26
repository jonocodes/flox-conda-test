import numpy as np
import bottleneck as bn

a = np.array([1, 2, np.nan, 4, 5])
b = bn.nanmean(a)

print(b)
