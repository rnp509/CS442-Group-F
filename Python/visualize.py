import numpy as np
import matplotlib.pyplot as plt

t = np.array([1, 2, 3, 4, 5])

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

