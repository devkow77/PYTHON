import matplotlib.pyplot as plt
import numpy as np

# Dane
year = ['Rok 2020', 'Rok 2021', 'Rok 2022', 'Rok 2023']
data = [(100, 90), (110, 95), (120, 105), (130, 110)]

# Rozdziel dane na chłopców i dziewczynki
boys = [d[0] for d in data]
girls = [d[1] for d in data]

x = np.arange(len(year))  # pozycje słupków
width = 0.35  # szerokość słupka

fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, boys, width, label='Chłopcy', color='tab:blue')
bars2 = ax.bar(x + width/2, girls, width, label='Dziewczynki', color='tab:orange')

# Opis osi i legenda
ax.set_ylabel('Liczba urodzeń')
ax.set_title('Liczba urodzeń wg płci w latach 2020–2023')
ax.set_xticks(x)
ax.set_xticklabels(year)
ax.legend()

plt.tight_layout()
plt.show()

