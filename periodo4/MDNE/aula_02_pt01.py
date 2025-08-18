import re 
import spacy
#import en_core_web_sm 
import pandas as pd



#Expressões Regulares:
#Testando o re.search():
s = 'foo123bar'
teste= re.search('123', s)
print(teste)

print("----------------------------")
#Testando o re.findall():
texto = 'Envie um email para contato@empresa.com ou suporte@empresa.org'
emails= re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', texto)
print(emails) 

print("----------------------------")
#Testando o re.sub():
tex = 'EnvIe uma meNsagem parA eLa.'
exemplo= re.sub(r'[A-Z]',lambda m: m.group(0).lower(), tex)
print(exemplo)

print("----------------------------")
#Testando o re.split():
text = 'maçã, banana; Laranja, abacaxi: uva'
emails= re.split(r'[;,]\s*', text)
print(emails)

print("----------------------------")
#Testando o Spacy
texto ="Contact us via email at cliente@empresa.com or visit our website."
texto_sem_emails= re.sub(r'\b[\w.-]+@[\w.-]+\.\w+\b', '', texto)

nlp = spacy.load('en_core_web_sm')
#doc = nlp(texto_sem_emails)
#print(doc)


print("----------------------------")
#Testanto a Tokenização com spacy:
info = "hello my name is carol!"

documento = nlp(info)

tokens= [token.text for token in documento]
print("tokens:", tokens)

dados_tokens = []
for token in documento:
    dados_tokens.append({
        'Token': token.text,
        'Índice de início': token.idx,
        'É pontuação?': token.is_punct,
        'É espaço em branco?': token.is_space,
        'Parte do discurso': token.pos_,
        'Dependência sintática': token.dep_
    })

# Criando DataFrame com os dados dos tokens
df_tokens = pd.DataFrame(dados_tokens)

# Exibindo o DataFrame
df_tokens