# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:30:07 2018

@author: Acer
"""

example_words=["python","pyhtoner","pyhtoning","pyhtoned"]

from nltk.stem import PorterStemmer
ps=PorterStemmer()

for words in example_words:
    print(ps.stem(words))
    
new_text ="It is important to by very pythonly while you are pyhtoning with python. All pythoners have pythoned poor atleast once."

import nltk
nltk.download('punkt')

nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize

words= word_tokenize(new_text)
review=[ps.stem(word) for word in words if not word in set(stopwords.words('english'))]



