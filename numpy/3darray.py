import numpy as np
arr= np.array([[[1, 2, 3], [4, 5, 6],[7,8,9]], 
               [[7, 8, 9], [10, 11, 12],[13,14,15]]])
print(arr)
print("dimensions:", arr.ndim)
print("shape:", arr.shape)
print("size:", arr.size)
print("type:", type(arr))
print(arr[0][2][0])