import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 5)

plt.plot(x, x, label='linear')
plt.plot(x, x ** 2, label='quadratic')
plt.plot(x, x ** 3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title('simple plot')
plt.legend()

plt.show()