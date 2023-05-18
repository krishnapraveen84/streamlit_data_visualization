import streamlit as st

st.title('HElllo')
st.header('HEllo')
st.subheader('HElllo')
st.text('hey')
st.markdown('# HEllo')
st.markdown('## HEllo')
st.markdown('### HEllo')
st.markdown('#### HEllo')
st.markdown('##### HEllo')

st.success('Data is Submitted!')
st.info('Got An Email...')
st.error("Error!")

exp = ZeroDivisionError('Division Not Possible With 0!')
st.exception(exp)
st.help(ZeroDivisionError)
st.write(f"Mathematical Operations : 8+1+2*1 =  {8 + 1 + 2 * 1}")

st.code('i = 10\n'
        'for i in range(i):\n'
        'print(i)')
st.checkbox('Male')
st.checkbox('Female')

if st.checkbox('Adult'):
    st.write("You're An Adult!..")

st.write('Select : ', ('Male', 'Female', 'Others'))
radioButton = st.radio('Select : ', ('Male', 'Female', 'Others'))
if radioButton == 'Male':
    st.write('Male')
elif radioButton == 'Female':
    st.write('Female')
else:
    st.write("Others")

st.subheader("Select Box")

selectBox = st.selectbox('Data Science : ', ['Data analysis', 'Web Scraping', 'Machine Learning', 'Deep Learning'])

st.write(f"You've Chosen : {selectBox}")

st.subheader(" Multi Select Box")

multiselectBox = st.multiselect('Data Science : ',
                                ['Data analysis', 'Web Scraping', 'Machine Learning', 'Deep Learning'])

st.write(f"You've Chosen :", len(multiselectBox), multiselectBox)

st.subheader("Button")
but = st.button("Click Me!")
if but:
    st.write('Thanks For Clicking..')

st.subheader('Slider')
volume = st.slider('Select Volume: ', 1, 100, step=1)
st.write("You're Volume: ", volume)

st.subheader("Input")
username = st.text_input("Enter UserName: ")
password = st.text_input('Enter Password: ', type='password')
st.write(username)
st.write(password)

st.subheader("Text Area")
text = st.text_area('Write something Here!..', )

st.write(text)

st.subheader("Input Number")
age = st.number_input('Select Your Age', 1, 20)
st.write('Your Age is : ', age)

st.subheader("Input Date")
date = st.date_input('Select Date')
st.write(date)
st.subheader("Input Time")
time = st.time_input('Select Time')
st.write(time)