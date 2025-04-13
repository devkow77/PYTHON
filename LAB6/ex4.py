import matplotlib.pyplot as plt

# Zad 4
# Narysuj wykres funkcji y = x^2 dla x ∈ [ − 5 , 5 ].

x = range(-5, 6)

plt.plot(x, [value**2 for value in x])
plt.show()
