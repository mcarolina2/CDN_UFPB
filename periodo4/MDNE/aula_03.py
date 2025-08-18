#Iniciamos o assunto de web scraping

import requests as req 


resposta = req.get('https://dados.pb.gov.br:443/getjson?nome=empenho_suplementacao&exercicio=2024&mes=6') 
print(resposta)

#resposta.