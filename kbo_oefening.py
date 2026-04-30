import requests
import pandas as pd
import time                             # voor de pauze tussen aanroepen
from api_config import API_KEY              # importeer de hey uit het aparte bestand


# -- 1. API-instellingen ------------------------------
#   De header vertelt de API wie je bent (via je key)
headers = {
    "Authorization": API_KEY
}
basis_url = "https://cbeapi.be/api/v1/company/"


# -- 2. CSV inlezen ----------------------------------
df = pd.read_csv("ondernemingen.csv")
print(f"Aantal ondernemingen in CSV: {len(df)}")


# -- 3. Lege lijst voorbereiden voor de resultaten ----------------------
resultaten = []


# -- 4. Loop over elke rij in de csv -------------------
for index, rij in df.iterrows():
    naam_csv    = rij["naam"]
    nummer_csv  = str(rij["ondernemingsnummer"])
    nummer_clean = nummer_csv.replace(".", "").replace(" ", "")

    print(f"Opvragen: {naam_csv} ({nummer_clean})...")

    url     = basis_url + nummer_clean
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        # Haal velden op met .get() zodat een ontbrekend veld geen fout geeft
        # Pas de veldnamen aan op basis van wat je in Stap 4 gezien hebt
        resultaten.append({
            "naam_csv"          : naam_csv,
            "ondernemingsnr"    : nummer_csv,
            "naam_kbo"          : data.get("data", {}).get("cbe_number", "onbekend"),
            "rechtsvorm"        : data.get("data", {}).get("juridical_form", "onbekend"),
            "status"            : data.get("data", {}).get("status", "onbekend"),
            "oprichtingsdatum"  : data.get("data", {}).get("start_date", "onbekend"),
            "straat"            : data.get("data", {}).get("address", {}).get("street", "onbekend"),
            "postcode"          : data.get("data", {}).get("address", {}).get("post_code", "onbekend"),
            "gemeente"          : data.get("data", {}).get("address", {}).get("city", "onbekend"),
        })
    elif response.status_code == 404:
        print(f"   X  Niet gevonden in KBO")
        resultaten.append({
            "naam_csv": naam_csv, "ondernemingsnr": nummer_csv,
            "naam_kbo" : "NIET GEVONDEN", "rechtsvorm": "",
            "status": "", "oprichtingsdatum": "",
            "straat": "", "postcode": "", "gemeente": "",
        })
    else:
        print(f"   !  FOUT  {response.status_code}")

    # Korte pauze tussen aanroepen (beleefd naar de API)
    time.sleep(0.5)

print(f"\nKlaar!  {len(resultaten)} ondernemingen verwerkt.")

# -- 5. Resultaten omzetten naar DataFrame en opslaan ----------
df_resultaat = pd.DataFrame(resultaten)

# Overzicht in de terminal
print("\nResultaten:")
print(df_resultaat[["naam_kbo", "rechtsvorm", "status", "gemeente"]])

# Opslaan als CSV
df_resultaat.to_csv("kbo_resultaten.csv", index=False, encoding="utf-8-sig")
print("\nOpgeslagen als kko_resultaten.csv")

# Statistieken
print(f"\nActieve ondernemingen : {len(df_resultaat[df_resultaat['status'] == 'active'])}")
print(f"Unieke rechtsvorm   : {df_resultaat['rechtsvorm'].nunique()}")
print(df_resultaat['rechtsvorm'].value_counts())