import math
import numpy as np

x=[1,2,3,4,5,6]
y=[1,4,9,16,25,36]
coff= np.polyfit(x,y,2)
for i in coff:
    x= round(i)
    print(x)