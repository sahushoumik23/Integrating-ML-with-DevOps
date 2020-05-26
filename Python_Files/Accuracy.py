#!/usr/bin/env python
# coding: utf-8

# In[35]:


from keras.models import load_model
import pandas as pa

# In[36]:


dataset=pa.read_csv('wines.csv')


# In[37]:


X=dataset.drop('Class',axis=1)


# In[38]:


Y=dataset['Class']


# In[39]:


y=pa.get_dummies(Y)


# In[40]:


model=load_model('trained2.h5')


# In[41]:


print("Number of layers are : ",len(model.layers))


# In[42]:


accuracy=model.fit(X,y,epochs=100)


# In[43]:


acc=accuracy.history['accuracy'][-1:][0]
acc=acc*100


# In[44]:


while int(acc) < 80:
    accuracy=model.fit(X,y,epochs=100)
    acc=accuracy.history['accuracy'][-1:][0]
    acc=acc*100

    

# In[ ]:




