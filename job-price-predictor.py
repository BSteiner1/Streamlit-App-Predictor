import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.subheader("""
Simple House Renovation App
""")

st.write("""
This app predicts the price of a house renovation!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
     bedroom_input = st.sidebar.slider('Bedrooms', 0, 10, 3)
     bathroom_input = st.sidebar.slider('Bathrooms', 1, 5, 2)
     kitchen_input = st.sidebar.slider('Kitchen', 0, 1, 1)
     painting_input = st.sidebar.slider('Rooms Painted', 1, 10, 4)
     
     data = {'Bedrooms': bedroom_input,
            'Bathrooms': bathroom_input,
            'Kitchen': kitchen_input,
            'Rooms Painted': painting_input
     }
     features = pd.DataFrame(data, index=[0])
     return features

input = user_input_features()

st.subheader('User Input parameters')
st.write(input)

df = pd.read_csv(r"C:\Users\bbste\Documents\Coding\Python\Machine Learning\Estimates Data.csv")
X = df[['Bedrooms', 'Bathrooms', 'Kitchen', 'Rooms Painted']]
Y = df['Price']

model = LinearRegression()
model.fit(X, Y)

prediction = model.predict(input)

st.subheader('Prediction')
st.write(prediction)

# st.subheader('Prediction')
# st.write(df[prediction])
# #st.write(prediction)

# st.subheader('Prediction Probability')
# st.write(prediction)