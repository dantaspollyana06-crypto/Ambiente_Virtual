from bs4 import BeautifulSoup
import requests
import csv

pagina = requests.get("https://quotes.toscrape.com")
if pagina.status_code==200:
    soup = BeautifulSoup(pagina.text, "html.parser")


frases = soup.find_all("span", class_="text")
author = soup.find_all("small", class_="author")
quote = soup.find_all("div", class_="quote")
titulos = []
autores = []
tags = []
lista_tags =[]
for f  in frases:
    titulos.append(f.text)
for a in author:
    autores.append(a.text)
for t in quote:
    tags_html = t.find_all("a", class_="tag")
    for tg in tags_html:
        lista_tags.append(tg.text)
    tags.append(lista_tags)
for i in range(len(titulos)):
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.-.-.-.-.-.")
    print("Citação: ")
    print(f'{titulos[i]}')
    print("Autor: ")
    print(f'{autores[i]}')
    print("Tags:")
    print(f"{lista_tags[i]}")
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.-.-.-.-.-.")
    arquivo = open("citacoes.csv","w", newline="", encoding="UTF-8")

escritor = csv.writer(arquivo)
escritor.writerow( ["Citaçaõ", "Autor", "Tags" ])

for i in range(len(titulos)):
    escritor.writerow([titulos [i] ,autores[i],",".join(tags[i])])

arquivo.close()
print()
print("Arquivo citações.csv criados com sucesso")
