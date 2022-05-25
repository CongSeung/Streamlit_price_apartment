import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import random
import seaborn as sns
from fbprophet import Prophet
import streamlit as st
import joblib

def run_prophet():
    st.text('부동산 실제 거래가를 지수로 나타내어 월별 동향을 쉽게 파악할 수 있다.')
    st.text('실거래가 지수의 기준은 17년 1월이다.')  

    df = pd.read_csv('data/Actual_transaction_price_apartment.csv', encoding= 'cp949')
    df = df.rename(columns={'지 역':'날짜'})
    df = df.set_index('날짜')
    df = df.transpose()
    df = df.reset_index()
    df = df.rename(columns={'index':'날짜'})

    region_menu_p = df.columns.to_list()[1:]

    select_region = st.sidebar.selectbox('지역 입력',region_menu_p)

    num_choice = st.sidebar.slider('단위값 입력',1 , 30)

    # str_choice = st.sidebar.text_input('날짜 단위 입력')
    
    if st.sidebar.button('예측하기') :

        price_apartment_prophet_df = df[['날짜', select_region]]
        price_apartment_prophet_df.columns = [ 'ds', 'y' ]

        prophet= joblib.load('data/prophet.pkl')

        future = prophet.make_future_dataframe(periods = num_choice , freq = 'Y' )

        forecast = prophet.predict(future)

        st.dataframe(forecast['yhat'])

        
        fig3 = prophet.plot(forecast)
        st.pyplot(fig3)

    
        fig4 = prophet.plot_components(forecast)
        st.pyplot(fig4)