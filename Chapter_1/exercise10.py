import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import regex as re

#
# Parsing the original "txt" file, to retrieve data sections. 
# 
with open('../data/boston.txt') as f:
	lines = f.readlines()
	start_line = -1
	for i, line in enumerate(lines):
		if re.search('[a-zA-Z]', line) is None and re.search('\d', line) is not None:
			# data section starts from this line.
			start_line = i
			break

	odd_lines = []
	even_lines = []

	for i, line in enumerate(lines[start_line:]):
		if re.search('\d', line) is None:
			continue
		even_lines.append(line) if i % 2 is 0 else odd_lines.append(line)

	assert len(odd_lines) == len(even_lines)

	data_lines = []
	for even, odd in zip(even_lines, odd_lines):
		data_lines.append(even[0:-1] + odd)
		
#
# Prepare dataset
#
raw_data = []
for line in data_lines:
	words = list(filter(lambda x: len(x) != 0, line.split(' ')))
	data = list(map(lambda x: float(x), words))
	raw_data.append(data)

np_data = np.array(raw_data, dtype=np.float32)

columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
dataset = pd.DataFrame(np_data, columns=columns)

#
# Plot scatter-plot for "CRIM" with other predictors
#
other_predictors = columns[1:]
for predictor in other_predictors:
	x_axis = dataset[predictor]
	y_axis = dataset['CRIM']

	plt.scatter(x_axis, y_axis)
	plt.xlabel(predictor)
	plt.ylabel('CRIM')

	plt.show()