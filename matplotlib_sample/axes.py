import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 5)

plt.axes([0.5, 0.5, .5, .5])
plt.plot(x, x, label='linear')


plt.show()