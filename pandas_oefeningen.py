import pandas as pd
import numpy as np
# CSV inlezen
df = pd.read_csv('verkoop.csv')

df['omzet'] = df['prijs'] * df['aantal']

gemiddelde_per_categorie = df.groupby('categorie')['omzet'].mean()
print(gemiddelde_per_categorie)

duur = df[df['prijs'] > 500]
aantal_duur = len(duur)
print(aantal_duur)

df['omzet_btw'] = df['omzet'] * 1.21
df['datum'].to_csv('verkoop_met_btw.csv')
df['product'].to_csv('verkoop_met_btw.csv')
df['categorie'].to_csv('verkoop_met_btw.csv')
df['prijs'].to_csv('verkoop_met_btw.csv')
df['aantal'].to_csv('verkoop_met_btw.csv')
df['omzet'].to_csv('verkoop_met_btw.csv')
df['omzet_btw'].to_csv('verkoop_met_btw.csv')

totale_omzet = df.groupby('product')['omzet'].sum().nlargest(1)
print(totale_omzet)

df['datum'] = pd.to_datetime(df['datum'])
df['maand'] = df['datum'].dt.month

omzet_per_maand = df.groupby('maand')['omzet'].sum().idxmax()
print(omzet_per_maand)

top3 = df.nlargest(3, 'omzet')
print(top3)

bottom3 = df.nsmallest(3, 'omzet')
print(bottom3)

df_met_nan = df.copy()
df_met_nan.loc[2, 'prijs'] = np.nan
df_met_nan.loc[5, 'aantal'] = np.nan

df_met_nan[df_met_nan.columns] = df_met_nan[df_met_nan.columns].apply(pd.to_numeric, errors='coerce')
df_met_nan =df_met_nan.fillna(df_met_nan.median())

omzetten = np.array(df['omzet'])
labels = np.where(omzetten < 100, 'goedkoop', 'duur')
print(labels)

cum_omzet = np.cumsum(omzetten)
print(cum_omzet)