# -*- coding: utf-8 -*-
"""IR_project_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XzTe1sg1wDopO5KDu7hg87EkR0kzXbAN
"""

import pickle
# from train_phase import clean_str, detokenize, preprocessing
import pandas as pd
import numpy as np

def load_database():
  #insert twitter scrapper for retrieving tweets
  
  #dummy data because the twitter scrape does not work
  df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/IR/dataset.csv')
  df = df.drop('labels', axis = 1)

  #preprocess the data
  # df = [preprocessing(sent) for sent in df]

  
  #returns csv file containing 1 column
  return df

def search(df, col, query):
  return df[df[col].str.contains(query.lower())]


def predict_sentiment(df):
  model_path = "/content/drive/MyDrive/Colab Notebooks/IR/model.pkl" #model.pkl's path
  vectorizer_path = "/content/drive/MyDrive/Colab Notebooks/IR/vectorizer.pkl" #vectorizer's path

  vect = pickle.load(open(vectorizer_path,'rb'))
  mod = pickle.load(open(model_path,'rb'))

  vector = vect.transform(np.array(df['reviews']))
  predictions = mod.predict(vector)
  
  return predictions

def count(predictions):
  neg = 0
  pos = 0
  neutral = 0;

  for prediction in predictions:
    if prediction == 'positif':
      pos+=1;
    elif prediction == 'negatif':
      neg+=1
    else:
      neutral +=1

  total = len(predictions)
  pos = pos/total *100
  neg = neg/total *100
  neutral = neutral/total *100

  return pos, neg, neutral

if __name__ == "__main__":

  #available query:
  #harddisk
  #laptop
  #smart tv
  #flash drives
  #televisi digital
  print("Masukan Query: ")
  user_input =  input()

  
  df = load_database()
  col = 'reviews'
  df = search(df,col,user_input)

  if df.shape[0]==0:
    print()
    print("Produk yang kamu cari tidak ada!")
  else:
    data = predict_sentiment(df)
    pos, neg, neutral = count(data)
    print()
    print("==============HASIL==============")
    print("ULASAN POSITIF : "+str(pos)+"%")
    print("ULASAN NEGATIF : "+str(neg)+"%")
    print("ULASAN NETRAL  : "+str(neutral)+"%")