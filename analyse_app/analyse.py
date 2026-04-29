import pandas as pd
import numpy as np
df = pd.read_csv('verkoop.csv')
df['omzet'] = df['prijs'] * df['aantal']

print('=== Verkoop analyse ===')
print(f"Totaal records: {len(df)}")
print(f"Totale omzet:   eur{df['omzet'].sum():.2f}")
print(f"Gemiddeld/vekoop: eur{df['omzet'].mean():.2f}")
print()
print('Omzet per categorie:')
print(df.groupby('categorie')['omzet'].sum().to_string())
print(df.sort_values(by='omzet', ascending=False).head(3))


df.to_csv('/app/output/resultaat.csv', index=False)