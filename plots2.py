import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff

st.subheader('Altair Scatter Plot')
chart_data = pd.DataFrame(np.random.randn(500, 5), columns=['a', 'b', 'c', 'd', 'e'])
chart = alt.Chart(data=chart_data).mark_circle().encode(x='a', y='b', size='c', tooltip=['a', 'b', 'c', 'd', 'e'])
st.altair_chart(chart)

st.subheader("Interactive Chart")
df = pd.read_csv(r'C:\Users\surya\OneDrive\Desktop\data_science\streamlit_gfg\lang_data.csv')
lang_list = df.columns.to_list()
choose_lang = st.multiselect('Choose Your Programming Language: ', lang_list)
new_df = df[choose_lang]
st.subheader('Line Chart')
st.line_chart(new_df)

st.subheader('Area Chart')
st.area_chart(new_df)

st.subheader('Data Visualization With Plotly')
st.subheader('Pie Chart')
data = pd.read_csv(r'C:\Users\surya\OneDrive\Desktop\data_science\streamlit_gfg\tips.csv')
fig = px.pie(data, values='total_bill', names='day')
st.plotly_chart(fig)

st.subheader('Pie Chart with parameters')
data = pd.read_csv(r'C:\Users\surya\OneDrive\Desktop\data_science\streamlit_gfg\tips.csv')
fig = px.pie(data, values='total_bill', names='day', opacity=0.7, color_discrete_sequence=px.colors.sequential.Agsunset)
st.plotly_chart(fig)

st.subheader('Histogram Plots')
x1 = np.random.randn(200)
x2 = np.random.randn(200)
x3 = np.random.randn(200)

hist_dat = [x1, x2, x3]
group_label = ['Group-1', 'Group-2', 'Group-3']

fig2 = ff.create_distplot(hist_data=hist_dat, group_labels=group_label, bin_size=[.1, .25, .5])
st.plotly_chart(fig2)