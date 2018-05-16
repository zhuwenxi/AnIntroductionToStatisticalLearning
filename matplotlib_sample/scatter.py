import matplotlib.pyplot as plt
import numpy as np

data = {
	'a': np.arange(50),
	'b': np.random.randint(0, 50, 50)
}

plt.scatter('a', 'b', c='c', data=data)

plt.show()