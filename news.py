import requests
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep

dados = []

url = 'https://g1.globo.com/'

response = requests.get(url)

site = BeautifulSoup(response.content, 'html.parser')
sleep(1)
 
noticias = site.findAll('div', attrs={'class':'feed-post-body'})

for noticia in noticias:
    titulo = noticia.find('a', attrs={'class':'feed-post-link'})
              
    subtitulo = noticia.find('span', attrs={'class':'feed-post-header-chapeu'})

    if subtitulo:
        dados.append([titulo.text, subtitulo.text, titulo.get('href')])
    else:
        dados.append([titulo.text, '', titulo.get('href')])

noiticias_G1 = pd.DataFrame(dados, columns=['Titulo', 'SubTitulo', 'Link'])
noiticias_G1.to_excel('Notícias_G1.xlsx', index=False)
