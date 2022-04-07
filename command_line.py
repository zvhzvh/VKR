# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 10:31:11 2022

@author: user
"""

# подключение библиотек
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow import keras
from tensorflow.keras import layers
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification

from keras import models
from keras.models import load_model

model = load_model('./models/model.h5')
df_all = pd.read_excel('all.xlsx')

col = df_all.columns

#Ввод данных пользователем dfuser
dfuser = df_all.copy(deep = True)
dfuser = dfuser.reset_index()
dfuser = dfuser.drop(labels=range(1, 936), axis=0)
dfuser.drop(['index'], inplace=True, axis=1)

print('Введите параметры:') 
a = 0 
for i in df_all.columns: 
    if a != 0 and a != 7 and a !=8: 
        print(col[a]) 
        y = input() 
        dfuser[col[a]].values[0] = float(y) 
    else: 
        dfuser[col[a]].values[0] = 0 
    a+=1
    if a == 13:
        break
    
dfuser.drop('Соотношение матрица-наполнитель', inplace=True, axis=1)
pred = model.predict(dfuser)
print ('ped = ', pred)