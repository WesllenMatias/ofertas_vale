from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import os


caminho = os.getcwd()
html = urlopen("https://www.valedopara.com.br/ofertas")
bs = BeautifulSoup(html, 'html.parser')

l_titulos = bs.find_all('div',{'class':'oferta-title'})
l_preco = bs.find_all('div',{'class':'oferta-value'})

titulo,preco = [],[]

for t in l_titulos:
    titulo.append(t.text)

for p in l_preco:
    preco.append(p.text)


df = pd.DataFrame({'Produto':titulo,'Preço':preco})

#df.head()

#df.to_excel(f'{caminho}/ofertas.xlsx')
#df.to_xml(f'{caminho}/ofertas.xml')
df.to_csv(f'{caminho}/ofertas.csv',index=False)