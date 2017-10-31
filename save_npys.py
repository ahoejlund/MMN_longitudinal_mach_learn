# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import numpy as np
import scipy.io as sio

for filename in files:
    a = sio.loadmat(filename)['a']
    b = a.reshape((-1,a.shape[-1])).T
    
    np.save(os.join(filename[:-4],'.npy'),b)
    
    
