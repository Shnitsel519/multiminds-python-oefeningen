import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# --- 1. Data ophalen via de API -------------------------
url = "https://api.open-meteo.com/v1/forecast"

parameters = {
    "latitude":     50.93,          #Aalst
    "longitude":    4.04,
    "hourly":       "temperature_2m",
    "forecast_days": 3,
    "timezone":     "Europe/Brussels"
}

print("Data ophalen...")
response = requests.get(url, params=parameters)

# Controleer of de aanroep gelukt is
if response.status_code != 200:
    print("Fout:", response.status_code)
    exit()

data = response.json()
# data is een dictinary - zo ziet de structuur eruit:
# data["hourly"]["time"]        --> lijst van tijdstippen als tekst
# data["hourly"]["temperature_2m"]  --> lijstvan temperaturen (evenveel als tijdstippen)
print("Data ontvangen!")

# --- 2. Data uitpakken ---------------------------------
tijden = []
for t in data["hourly"]["time"]:
    tijden.append(datetime.fromisoformat(t))
temperaturen = data["hourly"]["temperature_2m"]

print(f"Aantal datapunten: {len(temperaturen)}")
print(f"Min: {min(temperaturen):.1f}°C  Max: {max(temperaturen):.1f}°C")

# --- 3. Grafiek maken --------------------------------------
fig, ax = plt.subplots(figsize=(14, 5))

ax.plot(tijden, temperaturen, color="steelblue", linewidth=2, label="Temperatuur")
ax.fill_between(tijden, temperaturen, alpha=0.1, color="steelblue")

ax.set_title("Temperatuur in Aalst - komende 3 dagen", fontsize=14, fontweight="bold")
ax.set_xlabel("Datum en tijd")
ax.set_ylabel("Temperatuur (°C)")
ax.grid(True, alpha=0.3)
ax.legend()

# Datum op de x-as netjes formatteren
ax.xaxis.set_major_formatter(mdates.DateFormatter("%a %d/%m"))
ax.xaxis.set_major_locator(mdates.DayLocator())
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("temperatuur_Aalst.png", dpi=150)
plt.show()
print("Grafiek opgeslagen als temperatuur_Aalst.png")