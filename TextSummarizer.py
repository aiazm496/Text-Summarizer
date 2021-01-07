#!/usr/bin/env python
# coding: utf-8

# In[176]:


import nltk
from nltk.corpus import stopwords
#from nltk.cluster.util import cosine_distance  #for similarity b/w sentences
#import numpy as np
#import networkx as nx  #for similarity graphs


# In[177]:


import os


# In[178]:


def read_feedback(file):
    if os.path.exists(file):
        file_name = os.path.abspath(file)
        with open(file_name,'r',encoding='utf-8') as fob:
            return fob.read().replace('\n','')
    else:
        print("Please check file path!")


# In[179]:


from gensim.summarization.summarizer import summarize


# In[180]:


from gensim.summarization import keywords


# In[181]:


from textblob import TextBlob


# In[182]:


file_path = input("Please enter file path: ")
file_reader = read_feedback(file_path)


# In[183]:


file_reader


# In[184]:


file_blob = TextBlob(file_reader)


# In[185]:


def translator(blob):
    if blob.detect_language()!='en':
        return blob.translate(to='en')
    else:
        return blob
            


# In[186]:


en_blob = translator(file_blob)


# In[200]:


en_blob.sentiment.polarity


# In[201]:


en_blob.sentiment.subjectivity


# In[187]:


en_file = en_blob.string


# In[188]:


file_summary = summarize(en_file,ratio = 0.3)   #summary is 30% of the original text.
#print(editorial_summary)


# In[189]:


#print(keywords(file_summary,lemmatize=True))


# In[190]:


import docx


# In[191]:


from docx import Document


# In[192]:


response = Document()


# In[193]:


response.add_heading('Summary', 0)


# In[194]:


response.add_paragraph(file_summary)


# In[195]:


#%pwd


# In[196]:


name_of_file = input("Please enter the file name to save the summary here: ")


# In[197]:


response.save('{}.docx'.format(name_of_file))


# In[ ]:




