from TP5.tp5 import *

articles = ['Pommes', 'Poires', 'Fraises', 'Bananes', 'Oranges', 'Clémentines', 'Endives', 'Laitues']
prix = [5.27, 7.12, 4.98, 3.46, 4.02, 5.27, 1.67, 2.78]
panier = {}
for i in range(len(prix)):
    panier[articles[i]] = prix[i]

# print(getPrix(panier, "Poires")) # Devrait afficher 7.12
# print(getPrix(panier, "Clémentines")) # Devrait afficher 5.27
# print(getPrix(panier, "Cerises")) # Devrait afficher 0.0

#print(getPrixTotal(panier)) # Devrait afficher 34.57
afficherPanier(panier)