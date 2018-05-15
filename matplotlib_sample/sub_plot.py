import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.2)
y = np.sin(x)
y2 = x ** 2

fig = plt.figure()

ax1, ax2 = fig.subplots(1, 2)

ax1.plot(x, y)
ax2.plot(x, y2)

plt.show()