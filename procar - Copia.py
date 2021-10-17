#!/bin/env python
# -*- coding: utf-8 -*-
import re
import sys,socket
from urllib.request import urlopen

'''import requests
import selenium

r = requests.get('https://api.hinova.com.br/api/sga/v2/sincronismo-produto-fornecedor/buscar/placa/nly5315',headers={'Authorization': 'Bearer c8738ab46de5e1c15c5f421f70f3cee4a73dd5f20d63bc73201d3470ebf20689f8be62eaedb7b0a9f78a4c42dba37c2e4f14a0d33dc918fea62a9063d22f4b68d3e2eec55021cf864eb52ee1ad6996be81ad7d5306327adec249827897f4fe16'}).content
headers = {"content-type": "application/json; charset=UTF-8",'Authorization':'Bearer {}'.format('c8738ab46de5e1c15c5f421f70f3cee4a73dd5f20d63bc73201d3470ebf20689f8be62eaedb7b0a9f78a4c42dba37c2e4f14a0d33dc918fea62a9063d22f4b68d3e2eec55021cf864eb52ee1ad6996be81ad7d5306327adec249827897f4fe16')}


response = requests.post('https://api.hinova.com.br/api/sga/v2/sincronismo-produto-fornecedor/buscar/placa/nly5315', data={"placa":"NLY5315"})
print(r)'''



from bs4 import BeautifulSoup
import requests
import pandas as pd

while True:
    placa = input("Qual é a placa? ")
    html = requests.get('https://api.hinova.com.br/api/sga/v2/sincronismo-produto-fornecedor/buscar/placa/'+placa,headers={'Authorization': 'Bearer c8738ab46de5e1c15c5f421f70f3cee4a73dd5f20d63bc73201d3470ebf20689f8be62eaedb7b0a9f78a4c42dba37c2e4f14a0d33dc918fea62a9063d22f4b68d3e2eec55021cf864eb52ee1ad6996be81ad7d5306327adec249827897f4fe16'}).content
    soup = BeautifulSoup(html, 'html.parser')
    resultado = soup.prettify()
    print(html.decode(encoding='UTF-8'))
    continue