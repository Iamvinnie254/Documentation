# This is data that has mostly unused elements (elements that do not not carry any information
# CSC = compressed sparse column
# CSR - compressed sparse row


import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0,0,0,0,1,1,0,2])

print(csr_matrix(arr))