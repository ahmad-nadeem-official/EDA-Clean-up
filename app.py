import streamlit as st
import pandas as pd
from analysis.analyze import Analysis

data = pd.read_csv(r"/home/ahmad/workshop/EDA-Clean-up/res/Titanic-Dataset.csv")

pic = Analysis(data)

pic.columns
pic.describe
pic.head
pic.info
pic.shape