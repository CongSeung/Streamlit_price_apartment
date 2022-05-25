from base64 import standard_b64encode
import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import random
import seaborn as sns
from fbprophet import Prophet
import streamlit as st

######### 차트의 한글 안 깨지게
import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')
#########################################

def run_eda():
    st.text('과거 데이터를 분석해보자.')
    
    df = pd.read_csv('data/Actual_transaction_price_apartment.csv', encoding= 'cp949')
    df = df.rename(columns={'지 역':'날짜'})
    df = df.set_index('날짜')
    df = df.transpose()

    st.title('데이터')
    st.dataframe(df)

    st.title('기본 통계')
    st.dataframe(df.describe())

    # 지역 선택 시 실거래가지수 동향 차트로 보여주기
    st.title('06년 1월 - 21년 6월까지 지역별 실거래가격지수 동향')
    region_menu = df.columns.to_list()
    region_choice = st.selectbox('지역 선택', region_menu)

    st.set_option('deprecation.showPyplotGlobalUse', False)  # 경고창 뜨는 거 무시하는 옵션
    fig1 = plt.figure()
    df[region_choice].plot()
    st.pyplot(fig1)

    # 지역 여러 개 선택 시 서로 어떤 상관관계가 있는지 차트로 파악하기
    st.title('지역 간 실거래가지수의 상관관계 알아보기')
    region_menu = df.columns.to_list()
    region_mul_choice = st.multiselect('지역 2개 이상 선택',region_menu)
    
    if st.button('상관관계 파악하기') :
        
        fig2 =sns.pairplot(df[region_mul_choice])
        st.pyplot(fig2)

        st.dataframe(df[region_mul_choice].corr())
    


    