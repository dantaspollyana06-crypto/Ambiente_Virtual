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
    print("="*60)
"""
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
print("="*60)
print("Arquivo citacoes.csv criado com sucesso.")
print("="*60)
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

'''✔ Média de caracteres das frases
✔ Média de Tags por frase
✔ Frase mais longa e mais curta
✔ Frase com maior quantidade de Tags
✔ Autor da maior e da menor frase'''

media_tags = []
for quote in tags:
    media_tags.append(len(quote))
    array_tags = np.array(media_tags)
print(np.mean(array_tags))
print(f"{np.mean(array_tags)}.:2f")
print(f"Média de tags por frase: {np.mean(array_tags)}.:2f")
indice_maior = np.argmax(array_frases)
indice_menor= np.argmin(array_frases)
print("\nFrase mais longa:")
print(titulos[indice_maior])
print("\nFrase mais curta:")
print(titulos[indice_menor])
indice_tags = np.argmax(array_tags)
print("\nFrase com maior quantidade de Tags:")
print(titulos[indice_tags])
print(f"Quantidade de Tags: {array_tags[indice_tags]}")
print("\nAutor da maior frase:")
print(autores[indice_maior])
print("\nAutor da menor frase:")
print(autores[indice_menor])
print(".,"*50)
