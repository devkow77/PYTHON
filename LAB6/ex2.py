import matplotlib.pyplot as plt

# zad 2
# Utwórz wykres słupkowy przedstawiający temperatury w tygodniu.

days = ['Monday', 'Thuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures = [18,16,10,8,12,20,22]
bar_labels = ['orange', '_orange', 'blue', '_blue', '_orange', 'red', '_red']
bar_colors = ['tab:orange', 'tab:orange', 'tab:blue', 'tab:blue', 'tab:orange', 'tab:red', 'tab:red']

fig, ax = plt.subplots()
ax.bar(days, temperatures, label=bar_labels, color=bar_colors)
ax.set_ylabel('Temperatures in Celsius')
ax.set_title('Temperatures in next week')
ax.legend(title='Temperatures color')
plt.show()
