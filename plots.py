import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(20, 3), columns=['line-1', 'line-2', 'line-3'])
st.subheader("Random DataFrame")
st.table(df.head())

st.subheader('Line Chart')
st.line_chart(df)

st.subheader("Area Chart")
st.area_chart(df)

st.subheader("Bar Chart")
st.bar_chart(df)

st.subheader('Data Visualization with Matplotlib and Seaborn')
st.subheader("Loading Data Frame")
df = pd.read_csv('iris.csv')
st.table(df.head())

st.subheader('Distribution Plot')
fig = plt.figure(figsize=(15, 8))
df['species'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Distribution Plot with Seaborn')
fig = plt.figure(figsize=(15, 8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)

st.subheader('Multiple Graphs')
col1, col2 = st.columns(2)
with col1:
    fig1 = plt.figure()
    sns.set_style(style='darkgrid')
    sns.set_context(context='notebook')
    sns.distplot(df['sepal_length'], kde=False)
    st.pyplot(fig1)
with col2:
    fig2 = plt.figure()
    sns.set_theme(context='poster', style='darkgrid')
    sns.distplot(df['sepal_length'], hist=False)
    st.pyplot(fig2)

st.subheader('Scatter Plot')
fig, ax = plt.subplots(figsize=(15, 8))
ax.scatter(*np.random.random(size=(2, 100)))
st.pyplot(fig)

st.subheader('Count Plot')
fig = plt.figure(figsize=(15, 8))
sns.countplot(data=df, x='species')
st.pyplot(fig)

st.subheader('Box  Plot')
fig = plt.figure(figsize=(15, 8))
sns.boxplot(data=df, x='species', y='petal_length')
st.pyplot(fig)

st.subheader('Violin  Plot')
fig = plt.figure(figsize=(15, 8))
sns.violinplot(data=df, x='species', y='petal_length')
st.pyplot(fig)


