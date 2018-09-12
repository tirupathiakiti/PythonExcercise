
# coding: utf-8

# In[42]:


import pandas as pd
import numpy as np
#import csv
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
#from nltk import tokenizer
#nltk.download()
import re
import tokenize
from nltk.corpus import stopwords
#import tensorflow as tf
#Anaconda promp run below command before running importing textblob
#pip install -U textblob
#python -m textblob.download_corpora
from textblob import TextBlob
#from tensorflow.python.keras.preprocessing.text import Tokenizer
from nltk.stem import PorterStemmer


# In[6]:


imdbtrain = pd.read_csv ('C:/ML Guild/IMDB/datasets/train.csv',delimiter = ',')


# In[47]:


#print(imdbtrain)


# In[7]:


imdbtrain.head(10)


# In[8]:


imdbtext = imdbtrain['text']


# In[9]:


print(word_tokenize(imdbtext[0]))


# In[10]:


imdbtext = imdbtrain['text']


# In[11]:


print(len(imdbtrain))


# In[12]:


#Number of Words
imdbtrain['word_count'] = imdbtrain['text'].apply(lambda x: len(str(x).split(" ")))


# In[13]:


imdbtrain[['text','word_count']].head()


# In[14]:


#Number of characters
imdbtrain['char_count'] = imdbtrain['text'].str.len() ## this also includes spaces


# In[15]:


imdbtrain[['text','char_count']].head()


# In[16]:


stop = stopwords.words('english')


# In[18]:


#Number of stopwords
imdbtrain['stopwords'] = imdbtrain['text'].apply(lambda x: len([x for x in x.split() if x in stop]))


# In[19]:


imdbtrain[['text','stopwords']].head()


# In[20]:


# Lower case
imdbtrain['text'] = imdbtrain['text'].apply(lambda x: " ".join(x.lower() for x in x.split()))


# In[21]:


imdbtrain['text'].head()


# In[22]:


#Removing Punctuation
imdbtrain['text'] = imdbtrain['text'].str.replace('[^\w\s]','')


# In[23]:


imdbtrain['text'].head()


# In[24]:


#Removal of Stop Words
stop = stopwords.words('english')


# In[25]:


imdbtrain['text'] = imdbtrain['text'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))


# In[26]:


imdbtrain['text'].head()


# In[27]:


#Common word removal
freq = pd.Series(' '.join(imdbtrain['text']).split()).value_counts()[:10]


# In[28]:


freq


# In[80]:


#Rare words removal
freq = pd.Series(' '.join(imdbtrain['text']).split()).value_counts()[-10:]


# In[81]:


freq


# In[29]:


#Spelling correction
imdbtrain['text'][:5].apply(lambda x: str(TextBlob(x).correct()))


# In[31]:


#Stemming
st = PorterStemmer()


# In[32]:


imdbtrain['text'][:5].apply(lambda x: " ".join([st.stem(word) for word in x.split()]))


# In[33]:


#Lemmatization
from textblob import Word


# In[34]:


imdbtrain['text'] = imdbtrain['text'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))


# In[35]:


imdbtrain['text'].head()


# In[36]:


tf1 = (imdbtrain['text'][1:2]).apply(lambda x: pd.value_counts(x.split(" "))).sum(axis = 0).reset_index()


# In[37]:


tf1.columns = ['words','tf']


# In[38]:


tf1


# In[43]:


for i,word in enumerate(tf1['words']):
  tf1.loc[i, 'idf'] = np.log(imdbtrain.shape[0]/(len(imdbtrain[imdbtrain['text'].str.contains(word)])))


# In[44]:


tf1


# In[45]:


tf1['tfidf'] = tf1['tf'] * tf1['idf']


# In[46]:


tf1


# In[47]:


#Bag of Words
from sklearn.feature_extraction.text import CountVectorizer


# In[49]:


bow = CountVectorizer(max_features=1000, lowercase=True, ngram_range=(1,1),analyzer = "word")


# In[50]:


train_bow = bow.fit_transform(imdbtrain['text'])


# In[51]:


train_bow


# In[53]:


imdbtrain['text'][:5].apply(lambda x: TextBlob(x).sentiment)


# In[54]:


imdbtrain['sentiment'] = imdbtrain['text'].apply(lambda x: TextBlob(x).sentiment[0] )


# In[61]:


imdbtrain[['text','sentiment']]


# In[62]:


imdbtrain.to_csv('imbdtrain.csv')


# In[63]:


imdbtrain.to_csv('C:\ML Guild\IMDB\imbdtrain.csv')

