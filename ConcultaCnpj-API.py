import time

from bs4 import BeautifulSoup
import requests

# https://www.sintegraws.com.br/api/v1/execute-api.php?token=972BA777-FA69-40B7-B287-504AA10201D8&cnpj=29603548000108&plugin=RF

while True:
    '''placa = input("Qual é a placa? ")'''
    cnpj = input("Qual o CNPJ? ") # 29603548000108
    token = '972BA777-FA69-40B7-B287-504AA10201D8'
    html = requests.get('https://www.sintegraws.com.br/api/v1/execute-api.php?token='+token+'&cnpj='+cnpj+'&plugin=RF').content
    soup = BeautifulSoup(html, 'html.parser')
    resultado = soup.prettify()
    print(html.decode(encoding='UTF-8'))
    time.sleep(200000)
    continue
