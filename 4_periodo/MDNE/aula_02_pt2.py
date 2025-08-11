#Damos contunuidade da aula 02:
import spacy 
import pandas as pd

spacy.cli.download("pt_core_news_sm")
nlp = spacy.load('pt_core_news_sm') 

texto1 = 'Os gatos estão caçando ratos no jardim'

doc = nlp(texto1)

lemmas =[token.lemma_ for token in doc]
print(lemmas)

for token in doc:
    print(token.text, token.lemma_)

print("----------------------------")
#Construindo um datafraeme com as palavras lematizadas:

#fazemos primeiro uma função para lematizar um texto:
def lemmatize_text(texto2):
    doc = nlp(texto2)
    lemmas =[token.lemma_ for token in doc]
    return ''.join(lemmas)

dados = {'texto': ['Os gatos estão caçando ratos no jardim',
                   'Ele gostava de correr todas as manhãs',
                   'Ela canta muito bem']}

df = pd.DataFrame(dados)
df['Texto Lematizado'] = df['texto'].apply(lemmatize_text)

print(df)

print("----------------------------")
#Remoção de Stopwords:
tokens_sem_stopwords = [token.text for token in doc if not token.is_stop]
print(tokens_sem_stopwords)
print("----------------------------")

#Normalização
Texto3= "Olá! Me chamo CAROL e gosto de treinar,treinar, treinar : "
doc = nlp(Texto3)

tokens_normalizados = [
    token.lemma_.lower()
    for token in doc
    if not token.is_stop and not token.is_punct and not token.is_stop
]
print('Texto normalizado', tokens_normalizados)