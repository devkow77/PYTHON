import matplotlib.pyplot as plt
import numpy as np
import requests

# Twój klucz API (upewnij się, że jest ważny)
api_key = "7a44285f2b6c4bee04cb011236bcb5a0"

# Lista współrzędnych miast: dodajemy Warszawę
coordinates = [
    (51.509865, -0.118092),   # Londyn
    (48.856613, 2.352222),    # Paryż
    (52.520008, 13.404954),   # Berlin
    (40.416775, -3.703790),   # Madryt
    (41.902782, 12.496366),   # Rzym
    (52.229676, 21.012229)    # Warszawa
]

# Nazwy miast (pamiętaj o pustym stringu na początku, żeby zgadzał się z `set_yticklabels`)
towns = ['', 'Londyn', 'Paryż', 'Berlin', 'Madryt', 'Rzym', 'Warszawa']

# Pobierz dane temperatur
temperatures = []
for latitude, longitude in coordinates:
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=imperial&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if 'main' in data:
        temperature = data['main']['temp']
        temperatures.append(temperature)
    else:
        print(f"Nie udało się pobrać danych dla: ({latitude}, {longitude})")

# Konwersja do numpy
temperatures = np.array(temperatures).reshape(-1, 1)

# Rysowanie wykresu
plt.imshow(temperatures, cmap='coolwarm')
plt.colorbar(label='Temperatura (°F)')

ax = plt.gca()
ax.get_xaxis().set_visible(False)
ax.set_yticklabels(towns)

plt.title("Mapa temperatur europejskich miast")
plt.tight_layout()
plt.show()
