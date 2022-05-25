import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import random
import seaborn as sns
from fbprophet import Prophet
import streamlit as st

def run_home():
    st.text('프로핏 라이브러리')
    st.text('앞으로의 부동산 가격의 동향을 예측해보자')
    