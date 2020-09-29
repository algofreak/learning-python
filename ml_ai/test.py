import numpy as np
import pandas as pd

array_1 = np.array([[4, 9], [7, 6]])
print(array_1)

print((np.linalg.eig(array_1)))

print((np.linalg.eigvals(array_1)))

n = int(input())
array_1 = np.array(range(1, n))
array_2 = np.square(array_1)
series_3 = pd.Series(array_2, index=range(1, n))
print("Series: {}".format(series_3))
