import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Question 1
st.title('Streamlit App')

# Question 2
st.write('Hi there! My name is Jingyuan Yang.')
st.markdown("[Here](https://github.com/Jingyuan-Yang) is a link to my **GitHub**")

# Question 3: File uploader question
uploaded_file=st.file_uploader(label='Please upload a CSV file', type='CSV')

# Question 4:
# We want to convert the file to a pandas df
# But there will be an error if we don't have an uploaded file first.
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    # if x is an empty string, make it numpy's not-a-number, otherwise, leave x alone
    # Question 5
    df=df.applymap(lambda x: np.nan if x==' ' else x)
    # Question 6:
    # c is a column name, See week 3 Friday lecture
    def can_be_numeric(c):
        try:
            pd.to_numeric(df[c])
            return True
        except:
            return False
    # Now lets make a list of all the columns that can be made numeric
    good_cols=[c for c in df.columns if can_be_numeric(c)]

# Question 7
    df[good_cols]=df[good_cols].apply(pd.to_numeric,axis=0)

# Question 8
    x_axis = st.selectbox('Choose x-value', good_cols)
    y_axis = st.selectbox('Choose y-value', good_cols)

# Question 9
    values=st.slider('Select the range of rows you would like to plot',0,len(df.index)-1,(0,len(df.index)-1))

# Question 10
    st.write(f'Plotting ({x_axis},{y_axis}) for rows {values}.')

# Question 11
    my_chart=alt.Chart(df.loc[values[0]:values[1]]).mark_circle().encode(x=x_axis,y=y_axis)
    st.altair_chart(my_chart)

# Question 12
# Getting information from users
    name=st.text_input('Name')
    st.write(name)

    address=st.text_area('Enter your address')
    st.write(address)

    st.date_input('Enter a date')
    st.time_input('Enter a time')

    if st.checkbox('I accept T&C',value=False):
        st.write('Thank you!')

    if st.button('Subscribe'):
        st.write('successful subscription!')
