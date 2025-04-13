import matplotlib.pyplot as plt

# Przykładowe dane: [(wzrost w cm, masa w kg)]
dane = [
    (160, 55),
    (165, 60),
    (170, 65),
    (175, 72),
    (180, 78),
    (185, 85),
    (190, 90)
]

# Rozdziel dane na dwie listy
wzrost = [x[0] for x in dane]
masa = [x[1] for x in dane]

# Tworzenie wykresu punktowego
plt.scatter(wzrost, masa, color='teal', marker='o')

# Opisy osi i tytuł
plt.xlabel("Wzrost (cm)")
plt.ylabel("Masa ciała (kg)")
plt.title("Zależność masy ciała od wzrostu")

plt.grid(True)
plt.show()
