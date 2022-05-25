import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import random
import seaborn as sns
from fbprophet import Prophet
import streamlit as st

from app_eda import run_eda
from app_home import run_home
from app_prophet import run_prophet

def main():
    st.title('부동산 실거래가 월별 지수 예측')

    menu = ['Home', 'EDA', 'Prophet']

    choice = st.sidebar.selectbox('메뉴 선택', menu)

    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_eda()
    elif choice == menu[2]:
        run_prophet()

if __name__ == '__main__':
    main()