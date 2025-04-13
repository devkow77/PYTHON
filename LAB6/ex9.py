import matplotlib.pyplot as plt

# Dane: (nazwa owocu, liczba sztuk)
data = [('jabłka', 30), ('gruszki', 20), ('śliwki', 15), ('banany', 25), ('cytryny', 10)]

# Rozdziel dane na etykiety i wartości
labels = [item[0] for item in data]
sizes = [item[1] for item in data]

# Tworzenie wykresu kołowego
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)

# Dodanie tytułu
plt.title("Rozkład owoców w koszu")

# Równe proporcje – żeby wykres był okrągły
plt.axis('equal')

plt.show()
