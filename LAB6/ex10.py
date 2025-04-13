import matplotlib.pyplot as plt

# Przykładowe dane – wyniki procentowe
dane = [60, 70, 80, 90, 100, 70, 80, 80, 85, 95]

# Tworzenie histogramu
plt.hist(dane, bins=5, edgecolor='black', color='skyblue')

# Opisy osi i tytuł
plt.xlabel('Wynik (%)')
plt.ylabel('Liczba studentów')
plt.title('Rozkład wyników testu studentów')

plt.grid(axis='y')
plt.tight_layout()
plt.show()
