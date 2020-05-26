#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pa
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.backend import clear_session


# In[30]:


data=pa.read_csv('wines.csv')


# In[31]:


Y=data['Class']


# In[32]:


y=pa.get_dummies(Y)


# In[33]:


X=data.drop('Class',axis=1)


# In[34]:


clear_session()
model=Sequential()
sc=StandardScaler()


# In[35]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=50)
X_train=sc.fit_transform(X_train)


# In[36]:


model.add(Dense(units=5, input_shape=(13,),activation='relu', kernel_initializer='he_normal'))


# In[37]:


for i in range(15):
    model.add(Dense(units=8,activation='relu', kernel_initializer='he_normal'))


# In[38]:


model.add(Dense(units=3,activation='softmax'))


# In[39]:


model.compile(optimizer=RMSprop(learning_rate=0.001),loss='categorical_crossentropy',metrics=['accuracy'])


# In[40]:


accuracy=model.fit(X,y,epochs=100)


# In[41]:


model.save('trained2.h5')

acc=accuracy.history['accuracy'][-1:][0]



