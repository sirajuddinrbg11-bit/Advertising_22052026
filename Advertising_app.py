import streamlit as st
import pickle
import numpy as np
model = pickle.load(open('lr.sav','rb')
st.title('Sales Prediction App')
# Input Features
TV = st.number_input('TV adv budget', min_val=0.0)
Radio = st.number_input('Radio Adv Budget',min_value=0.0)
Newspaper = st.number_input('Newspaper budget',min_value=0.0)
if st.button('predict sales'):
  input_data=np.array([[TV,Radio,Newspaper]])
  Prediction = model.predict(input_data)[0]
  st.success(f'predicted Sales: {Prediciton:.2f}')
