articles = ['Pommes', 'Poires', 'Fraises', 'Bananes', 'Oranges', 'Clémentines', 'Endives', 'Laitues']
prix =[5.27, 7.12, 4.98, 3.46, 4.02, 5.27, 1.67,2.78]
dico = {}
for i in range(len(prix)):
    dico[articles[i]]=prix[i]

print(dico)