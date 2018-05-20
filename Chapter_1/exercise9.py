import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import math

#
# (e):
#

dataset = pd.read_csv('../data/Auto.csv')

columns = list(dataset.columns)
columns_type = dataset.dtypes
numerical_columns = []

def type_is_numerical(t):
	return t == np.float32 or t == np.float64 or t == np.int32 or t == np.int64

# find columns who's type is numerical
for i in range(len(columns_type)):
	if type_is_numerical(columns_type[i]):
		numerical_columns.append(columns[i])

columns_len = len(numerical_columns)
figure_num = math.ceil(columns_len * (columns_len - 1) / 2)




for x_index in range(columns_len):
	i = 0
	# fig, axs = plt.subplots(1, columns_len - x_index - 1)
	for y_index in range(x_index + 1, columns_len - x_index - 1):
		x_series = dataset[numerical_columns[x_index]]
		y_series = dataset[numerical_columns[y_index]]

		

		# axs[i].scatter(x_series, y_series)
		# axs[i].set_xlabel(numerical_columns[x_index])
		# axs[i].set_ylabel(numerical_columns[y_index])

		# plt.scatter(x_series, y_series)
		plt.scatter(y_series, x_series)
		plt.ylabel(numerical_columns[x_index])
		plt.xlabel(numerical_columns[y_index])
		plt.show()

		i += 1
	plt.show()
	break

