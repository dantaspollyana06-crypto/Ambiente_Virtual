from bs4 import BeautifulSoup
import requests
import csv
import numpy as np
pagina = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(pagina.text, "html.parser")
frases = soup.find_all("span", class_="text")
author = soup.find_all("small", class_="author")
quote = soup.find_all("div", class_="quote")
titulos = []
autores = []
tags = []
for f in frases:
    titulos.append(f.text)
for a in author:
    autores.append(a.text)
for t in quote:
    tags_html = t.find_all("a", class_="tag")
    lista_tags = []
    for tg in tags_html:
        lista_tags.append(tg.text)
    tags.append(lista_tags)

"""for i in range(len(titulos)):

    print("CITAÇÃO: ")
    print(f'{titulos[i]}')
    print("-"*60)
    print("AUTOR: ")
    print(f'{autores[i]}')
    print("-"*60)
    print("TAGS: ")
    print(f'{tags[i]}')
    print("="*60)"""

arquivo = open(
    "citacoes.csv",
    "w",
    newline="",
    encoding="utf-8")

escritor = csv.writer(arquivo)

escritor.writerow(
    ["Citação","Autor","Tags"]
)

for i in range(len(titulos)):
    escritor.writerow(
        [
        titulos[i],
        autores[i],
        ", ".join(tags[i])
        ]
    )
arquivo.close()
"""""print("="*60)
print("Arquivo citacoes.csv criado com sucesso.")
print("="*60)"""

tamanho_frases= []
for frases in titulos:
    tamanho_frases.append(len(frases))
    """for j in tamanho_frases:
        print(j)"""
    
quantidade_tags = []
for quote in tags:
    quantidade_tags.append(len(quote))

array_frases = np.array(tamanho_frases)  
array_tags= np.array(quantidade_tags)
print(array_tags)
print(array_frases)  
print(np.mean(array_frases))
print(np.min(array_frases))
print(np.max(array_frases))
indice = np.argmax(array_frases)
print(titulos[indice])
print(tamanho_frases[9])

