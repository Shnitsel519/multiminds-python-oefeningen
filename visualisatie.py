import pandas as pd
import matplotlib.pyplot as plt
from pyfonts import load_google_font
font = load_google_font("Rubik")

df = pd.read_csv('verkoop.csv')
df['datum'] = pd.to_datetime(df['datum'])
df['omzet'] = df['prijs'] * df['aantal']

# Omzet per datum als lijndiagram
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(df['datum'], df['omzet'], marker='o', color='steelblue', linewidth=2)

ax.set_title('Omzet per verkoopdatum', fontsize=14, fontweight='bold')
ax.set_xlabel('Datum')
ax.set_ylabel('Omzet (euro)')
ax.tick_params(axis='x', rotation=45)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('omzet_lijn.png', dpi=150)      # opslaan
plt.show()

# Omzet per categorie berekenen
omzet_cat = df.groupby('categorie')['omzet'].sum()

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(omzet_cat.index, omzet_cat.values, color=['steelblue', 'coral'], edgecolor='white')

ax.set_title('Totale omzet per categorie', fontsize=14, fontweight='bold')
ax.set_xlabel('Categorie')
ax.set_ylabel('Omzet (euro)')

# Waarde boven elke balk tonen
for i, v in enumerate(omzet_cat.values):
    ax.text(i, v + 20, f'€{v:.0f}', ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('omzet_staaf.png', dpi=150)
plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Links grafiek: omzet per categorie
omzet_cat = df.groupby('categorie')['omzet'].sum()
ax1.bar(omzet_cat.index, omzet_cat.values, color='steelblue')
ax1.set_title('Omzet per categorie')
ax1.set_ylabel('Omzet (euro)')

# Rechtse grafiek: aantal verkopen per product
aantal_prod = df.groupby('product')['aantal'].sum().sort_values()
ax2.barh(aantal_prod.index, aantal_prod.values, color='coral')
ax2.set_title('Aantal verkopen per product')
ax2.set_xlabel('Aantal')

fig.suptitle('Verkoop overzicht', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('dashboard1.png', dpi=150)
plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# Taartdiagram: aandeel omzet per categorie
omzet_cat = df.groupby('categorie')['omzet'].sum()
ax1.pie(omzet_cat.values, labels=omzet_cat.index, autopct='%1.1f%%', colors=['steelblue', 'coral'], startangle=90)
ax1.set_title('Aandeel omzet per categorie')

# Spreidingsdiagram: prijs vs. omzet
ax2.scatter(df['prijs'], df['omzet'], color='steelblue', alpha=0.7, edgecolors='white', s=80)
ax2.set_title('Prijs vs. Omzet')
ax2.set_xlabel('Prijs (euro)')
ax2.set_ylabel('Omzet (euro)')
ax2.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
plt.savefig('taart_scatter.png', dpi=150)
plt.show()


# Oefeningen

prijs_per_product = df.groupby('product')['prijs'].mean().sort_values()

fig, ax = plt.subplots(figsize=(8, 5))

tabel = ax.barh(prijs_per_product.index, prijs_per_product.values, color=['steelblue', 'coral'], edgecolor='white')

ax.set_title('Gemiddelde prijs per product')
ax.bar_label(tabel)
ax.set_xlabel('Gemiddelde prijs')
ax.set_ylabel('Product')

plt.tight_layout()
plt.savefig('prijs_per_product.png', dpi=150)
plt.show()

# lettertipen rubik
plt.rcParams.update({'font.family': 'Rubik'})

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

ax1.plot(df['datum'], df['omzet'], marker='o', color='orange', linewidth=2)
gemiddelde = df['omzet'].mean()
ax1.set_title('Omzet per verkoopdatum', color='red')
ax1.set_xlabel('Datum')
ax1.set_ylabel('Omzet (euro)')
ax1.tick_params(axis='x', rotation=45)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.axhline(y=gemiddelde, color='r', linestyle='--')

omzet_cat = df.groupby('categorie')['omzet'].sum()
ax2.bar(omzet_cat.index, omzet_cat.values, color='orange')
ax2.set_title('Omzet per categorie', color='red')
ax2.set_ylabel('Omzet (euro)')

# Rechtse grafiek: aantal verkopen per product
aantal_prod = df.groupby('product')['aantal'].sum().sort_values()
ax3.barh(aantal_prod.index, aantal_prod.values, color='red')
ax3.set_title('Aantal verkopen per product', color='gold')
ax3.set_xlabel('Aantal')

tabel = ax4.barh(prijs_per_product.index, prijs_per_product.values, color=['orange', 'gold'], edgecolor='red')

ax4.set_title('Gemiddelde prijs per product')
ax4.bar_label(tabel)
ax4.set_xlabel('Gemiddelde prijs')
ax4.set_ylabel('Product')

fig.suptitle('Dashboard', fontsize=16, fontweight='bold', color='orange')
plt.tight_layout()
plt.savefig('dashboard.png', dpi=150)
plt.show()