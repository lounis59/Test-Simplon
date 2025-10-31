import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')

ventes = données

ventes["chiffre_affaires"] = ventes["prix"] * ventes["qte"]

print(ventes['chiffre_affaires'].sum())

total_ca = ventes["chiffre_affaires"].sum()

print(f"Chiffre d’affaires total : {total_ca} €")

ca_par_produit = ventes.groupby("produit", as_index=False)["chiffre_affaires"].sum()

print(f"les vente par produit : {ca_par_produit}")

fig1 = px.bar(
    ca_par_produit,
    x="produit",
    y="chiffre_affaires",
    color="produit",
    title="Chiffre d'affaires par produit",
    text_auto=".2s"
)
fig1.write_html("chiffre-d'affaire-par-produit.html")

ventes_par_produit = ventes.groupby("produit", as_index=False)["qte"].sum()

print(f"ventes par produits : {ventes_par_produit}")

fig2 = px.bar(
    ventes_par_produit,
    x="produit",
    y="qte",
    color="produit",
    text_auto=True,
    title=" Nombre de ventes par produit"
)

fig2.write_html("vente-par-produits.html")