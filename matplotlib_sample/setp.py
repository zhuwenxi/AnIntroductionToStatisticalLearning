import matplotlib.pyplot as plt
import numpy as np


lines = plt.plot([3, 4, 5])
# use keyword args
plt.setp(lines, color='r', linewidth=2.0)
# or MATLAB style string value pairs
plt.setp(lines, 'color', 'r', 'linewidth', 2.0)

plt.show()