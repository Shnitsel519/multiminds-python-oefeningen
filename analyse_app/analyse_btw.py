import pandas as pd
import numpy as np
df = pd.read_csv('verkoop.csv')
df['omzet'] = df['prijs'] * df['aantal']

df['omzet_btw'] = df['omzet'] * 1.21

df.to_csv('/app/output/resultaat_btw.csv', index=False)