#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install streamlit pandas scikit-learn joblib')


# In[2]:


from sklearn.ensemble import IsolationForest
import joblib
import pandas as pd

# Example: Training a model
# Assuming you have a stock price dataframe called `stock_data`
stock_data = pd.read_csv(r"C:\Users\shrey\Downloads\train_processed.csv")
model = IsolationForest(contamination=0.05)
model.fit(stock_data[['Close']])

# Save the trained model
joblib.dump(model, 'anomaly_detection_model.pkl')


# In[6]:


import streamlit as st
import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.impute import SimpleImputer

# Load pre-trained model
model = joblib.load('anomaly_detection_model.pkl')

# Set up Streamlit interface
st.title("Anomaly Detection for Stock Prices")

st.markdown("Upload a CSV file containing stock price data (with a 'Date' and 'Close' column)")

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load the data from CSV
    stock_data = pd.read_csv(r"C:\Users\shrey\Downloads\train_processed.csv")

    if 'Date' in stock_data.columns and 'Close' in stock_data.columns:
        st.write("Data Preview:")
        st.write(stock_data.head())

        # Handle missing values in the 'Close' column
        # Option 1: Drop rows with missing values
        stock_data = stock_data.dropna(subset=['Close'])

        # Option 2: Impute missing values (uncomment if using imputation)
        # imputer = SimpleImputer(strategy='median')
        # stock_data['Close'] = imputer.fit_transform(stock_data[['Close']])

        # Predict anomalies
        anomalies = model.predict(stock_data[['Close']])

        # Add anomaly column
        stock_data['Anomaly'] = anomalies
        stock_data['Anomaly'] = stock_data['Anomaly'].map({1: 'Normal', -1: 'Anomaly'})

        # Show the detected anomalies
        st.write("Detected Anomalies:")
        st.write(stock_data[stock_data['Anomaly'] == 'Anomaly'][['Date', 'Close', 'Anomaly']])

        # Plot the results
        st.subheader("Anomaly Detection Plot")
        st.line_chart(stock_data[['Date', 'Close']].set_index('Date'))

    else:
        st.error("CSV file must contain 'Date' and 'Close' columns.")


# In[7]:


get_ipython().system('streamlit run anomaly_detection_app.py')

