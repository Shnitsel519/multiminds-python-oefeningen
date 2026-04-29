import pandas as pd
import numpy as np

# CSV inlezen
df = pd.read_csv('verkoop.csv')

# Eerste verkenning
print(df.head()) # eerste 5 rijen
print(df.info()) # kolomtypes en missing values
print(df.describe()) # statistieken (min, max, gemiddelde...)
print(df.shape) # (rijen, kolommen)
print(df.columns.tolist()) # kolomnamen als lijst

# Één kolom selecteren → Series
producten = df['product']
print(producten)

# Meerdere kolommen → nieuw DataFrame
overzicht = df[['product', 'prijs', 'aantal']]
print(overzicht)

# Filteren: alleen Elektronica
elektronica = df[df['categorie'] == 'Elektronica']
print(elektronica)

# Filteren: prijs boven 100 euro
duur = df[df['prijs'] > 100]
print(duur)

# Combineren: Elektronica EN prijs boven 100
combo = df[(df['categorie'] == 'Elektronica') & (df['prijs'] > 100)]
print(combo)

# Totale omzet per rij = prijs × aantal
df['omzet'] = df['prijs'] * df['aantal']
print(df[['product', 'prijs', 'aantal', 'omzet']])

# Totale omzet van alle verkopen
print(f"Totale omzet: €{df['omzet'].sum():.2f}")
print(f"Gemiddelde omzet per verkoop: €{df['omzet'].mean():.2f}")
print(f"Hoogste omzet: €{df['omzet'].max():.2f}")

# Totale omzet per categorie
per_categorie = df.groupby('categorie')['omzet'].sum()
print(per_categorie)

# Meerdere berekeningen tegelijk
omzet_per_cat = df.groupby('categorie')['omzet'].sum()
gem_omzet_per_cat = df.groupby('categorie')['omzet'].mean()
aantal_per_cat = df.groupby('categorie')['aantal'].sum()
print(omzet_per_cat)
print(gem_omzet_per_cat)
print(aantal_per_cat)

# Meest verkochte product (op aantal)
per_product = df.groupby('product')['aantal'].sum().sort_values(ascending=False)
print(per_product)

# Gefilterd resultaat opslaan
elektronica = df[df['categorie'] == 'Elektronica']
elektronica.to_csv('elektronica_verkoop.csv', index=False)
print('Opgeslagen: elektronica_verkoop.csv')

# Samenvatting opslaan
samenvatting = df.groupby('categorie')['omzet'].sum().reset_index()
samenvatting.columns = ['categorie', 'totale_omzet']
samenvatting.to_csv('omzet_per_categorie.csv', index=False)
print('Opgeslagen: omzet_per_categorie.csv')

# Zet de datum-kolom om naar een echt datum-type
df['datum'] = pd.to_datetime(df['datum'])

# Jaar, maand en weekdag extraheren
df['jaar'] = df['datum'].dt.year
df['maand'] = df['datum'].dt.month
df['weekdag'] = df['datum'].dt.day_name()

# Omzet per maand berekenen
omzet_per_maand = df.groupby('maand')['omzet'].sum()
print(omzet_per_maand)

# Filteren: alleen januariverkopen
januari = df[df['datum'].dt.month == 1]
print(f"Aantal januariverkopen: {len(januari)}")

# Sorteren op prijs (goedkoopste eerst)
gesorteerd = df.sort_values('prijs')
print(gesorteerd[['product', 'prijs']])

# Sorteren op omzet (duurste eerst)
gesorteerd_desc = df.sort_values('omzet', ascending=False)
print(gesorteerd_desc[['product', 'omzet']].head())

# Top 3 duurste verkopen
top3 = df.nlargest(3, 'omzet')
print(top3[['product', 'omzet']])

# Hoe vaak werd elk product verkocht?
print(df['product'].value_counts())

# Sorteren op meerdere kolommen: categorie + prijs
df.sort_values(['categorie', 'prijs'], ascending=[True, False])

# Simuleer ontbrekende waarden door ze toe te voegen
import numpy as np
df_met_nan = df.copy()
df_met_nan.loc[2, 'prijs'] = np.nan # rij 2, kolom prijs leeg
df_met_nan.loc[5, 'categorie'] = np.nan # rij 5, kolom categorie leeg

# Controleer welke waarden ontbreken
print(df_met_nan.isnull().sum()) # aantal NaN per kolom

# Optie 1: rijen met NaN verwijderen
schoon = df_met_nan.dropna()
print(f"Rijen na dropna: {len(schoon)}")

# Optie 2: NaN in prijs vervangen door het gemiddelde
gem_prijs = df['prijs'].mean()
df_met_nan['prijs'] = df_met_nan['prijs'].fillna(gem_prijs)
print(df_met_nan.isnull().sum()) # controleer: nog NaN?

# Arrays aanmaken
reeks = np.arange(0, 10, 2) # [0, 2, 4, 6, 8]
verdeel = np.linspace(0, 1, 5) # [0.0, 0.25, 0.5, 0.75, 1.0]
nullen = np.zeros(5) # [0. 0. 0. 0. 0.]
print(reeks, verdeel, nullen)

# Broadcasting: bewerking op heel de array
omzetten = np.array(df['omzet'])
omzet_btw = omzetten * 1.21 # BTW op elke waarde tegelijk
print(omzet_btw.round(2))

# np.where: label hoog/laag per omzet
labels = np.where(omzetten > 500, 'hoog', 'laag')
print(labels)

# Cumulatieve omzet (lopend totaal)
cum_omzet = np.cumsum(omzetten)
print('Lopend totaal:', cum_omzet)

# Random getallen (reproduceerbaar met seed)
np.random.seed(42)
steekproef = np.random.randint(1, 100, size=5) # 5 willekeurige getallen
print('Steekproef:', steekproef)




# Oefeningen
print()
print()
print("Oefeningen")

gemiddelde_per_categorie = df.groupby('categorie')['omzet'].mean()
print(gemiddelde_per_categorie)

duur2 = df[df['prijs'] > 500]
aantal_duur = len(duur2)
print(f"Aantal hoger dan 500 euro: {aantal_duur}")

df['omzet_btw'] = df['omzet'] * 1.21
df['datum'].to_csv('verkoop_met_btw.csv')
df['product'].to_csv('verkoop_met_btw.csv')
df['categorie'].to_csv('verkoop_met_btw.csv')
df['prijs'].to_csv('verkoop_met_btw.csv')
df['aantal'].to_csv('verkoop_met_btw.csv')
df['omzet'].to_csv('verkoop_met_btw.csv')
df['omzet_btw'].to_csv('verkoop_met_btw.csv')

totale_omzet_per_product = df.groupby('product')['omzet'].sum().idxmax()
print(f"Hoogste totale omzet: {totale_omzet_per_product}")


hoogste_omzet_per_maand = df.groupby('maand')['omzet'].sum().idxmax()
print(f"Hoogste omzet per maand: {hoogste_omzet_per_maand}")

top3_zelf = df.nlargest(3, 'omzet')
print("De drie producten met hoogste omzet:")
print(top3_zelf[['product', 'omzet']])

bottom3 = df.nsmallest(3, 'omzet')
print("De drie producten met laagste omzet:")
print(bottom3[['product', 'omzet']])

df_met_nan.loc[2, 'prijs'] = np.nan
df_met_nan.loc[5, 'aantal'] = np.nan

df_met_nan[df_met_nan.columns] = df_met_nan[df_met_nan.columns].apply(pd.to_numeric, errors='coerce')
df_met_nan =df_met_nan.fillna(df_met_nan.median())

labels = np.where(omzetten < 100, 'goedkoop', 'duur')
print(labels)

print(cum_omzet)