import matplotlib.pyplot as plt
import numpy as np

# Zakres wartości x
x = np.linspace(0, np.pi, 100)

# Funkcje sinus i odbicie lustrzane
y1 = np.sin(x)
y2 = -np.sin(x)

# Rysowanie dwóch symetrycznych "półserc"
plt.plot(x, y1, color='red')
plt.plot(x, y2, color='red')

# Dodanie lustrzanego odbicia względem osi Y
plt.plot(-x, y1, color='red')
plt.plot(-x, y2, color='red')

# Stylizacja
plt.axis('equal')  # zachowuje proporcje
plt.title("Serce z funkcji sinus")
plt.axis('off')    # ukrywa osie

plt.show()
