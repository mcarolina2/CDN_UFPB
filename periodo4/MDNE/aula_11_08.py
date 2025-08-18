import nltk
import numpy as np 
from nltk.corpus import gutenberg
from nltk.corpus import europarl_raw


# carregando o texto: 
#nltk.download('gutenberg')
#alice = gutenberg.raw(fileids='carroll-alice.txt')
#print (alice) 

    #verificando o tamanho do texto
#print (len(alice)) 

    #primeiros 100 caracteres do texto
#print (alice[0:100])

    #Acessando o texto com numpy
#nltk.download('punkt_tab')
#default_st = nltk.sent_tokenize
#alice_senteces = default_st(text=alice)
    #Testando 
#print('\nTotal de sentenças dealice:', len(alice_senteces))
#print('Cinco primeiras sentenças de alice:-', np.array(alice_senteces[0:5]))

    #Testanto outro idioma:
nltk.download('europarl_raw')
german_text = europarl_raw.german.raw(fileids='ep-00-01-17.de')
#total de caracteres do corpo:
print(len(german_text))