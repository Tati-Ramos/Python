from bs4 import BeautifulSoup # extração de dados de arquivos HTML e XML

import requests #envie solitações HTTP em Python

site = requests.get("https://www.climatempo.com.br").content
#objeto site recebendo o conteudo da requisação http do site....

soup = BeautifulSoup(site, 'html.parser')
#objeto soup baixando do site o html

print(soup.prettify())
#transforma html em strign e o print vai exibir o html

#temperatura = soup.find("span", class_="_block _margin-b-5 -gray")

# print(temperatura.string)

# print(soup.a)
# print(soup.p.string)

# print(soup.title.string)


