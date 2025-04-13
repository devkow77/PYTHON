import matplotlib.pyplot as plt
import requests
import datetime

# Zakres dat
date_to = datetime.date.today()
date_from = date_to - datetime.timedelta(days=14)

# Waluta bazowa
base = "EUR"

# API URL
url = f'https://api.exchangerate.host/timeseries?start_date={date_from}&end_date={date_to}&base={base}'

# Pobranie danych
response = requests.get(url)
data = response.json()

# Sprawdzenie poprawności
if data["success"]:
    dates = []
    pln_rates = []
    usd_rates = []

    for date in sorted(data["rates"].keys()):
        rates = data["rates"][date]
        if "PLN" in rates and "USD" in rates:
            dates.append(date)
            pln_rates.append(rates["PLN"])
            usd_rates.append(rates["USD"])

    # Rysowanie wykresu
    plt.plot(dates, pln_rates, label="EUR/PLN", marker='o')
    plt.plot(dates, usd_rates, label="EUR/USD", marker='x')
    plt.xlabel("Data")
    plt.ylabel("Kurs")
    plt.title("Kursy walut (EUR/PLN i EUR/USD) z ostatnich 14 dni")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.grid(True)
    plt.show()

else:
    print("Błąd podczas pobierania danych:", data)
