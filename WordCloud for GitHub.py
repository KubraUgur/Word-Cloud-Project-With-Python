#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install wordcloud matplotlib numpy


# In[5]:


from wordcloud import WordCloud 
import matplotlib.pyplot as plt


# In[44]:


word_freq={
    'Success':5,
    'Motivation':2,
    'Coffee':2,
    'Hard Working':3,
    'Sleepless Nights':3,
    'Dedication':3,
    'Goals': 3}

def color_function(word, font_size, orientation, position, randon_state=42, **kwargs):
        colors = {
            'Success':'Red',
            'Motivation':'Blue',
            'Coffee':'Brown',
            'Hard Working':'Green',
            'Sleepless Nights':'black',
            'Dedication':'Yellow',
            'Goals':'purple'            
        }
        return colors.get(word, 'black')
wordcloud = WordCloud(width=800, height=400, color_func=color_function, prefer_horizontal=0.8, background_color='white').generate_from_frequencies(word_freq)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()


# In[45]:


wordcloud.to_file('wordcloud2.png') 


# In[ ]:




