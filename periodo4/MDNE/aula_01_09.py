import pandas as pd
import nltk

nltk.download('averaged_perceptron_tagger_eng')
nltk.download('punkt_tab')

sentece ="US unveils world's mostpowerful supercomputer, beats china." 
nltk_pos_tagged = nltk.pos_tag(nltk.word_tokenize(sentece))
pd.DataFrame(nltk_pos_tagged, columns=['Word', 'POS tag']).T