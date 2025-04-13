import matplotlib.pyplot as plt
import numpy as np

# Zad 5
# Narysuj wykres sin(x) i cos(x) dla x ∈ [ 0 , 2 π ] .

x = np.arange(0., 2 * np.pi, 0.1)

plt.plot(x, np.sin(x), 'r', x, np.cos(x), 'b')
plt.show()