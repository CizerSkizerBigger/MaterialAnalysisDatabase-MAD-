import streamlit as st # type: ignore

st.title('Select box Example')

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)

#=========

st.header('st.selectbox')

X_coordinate_selection = ('Price', 'Performance', 'Ratio')
Y_coordinate_selection = None

X_coordinate = st.selectbox(
     'Select the X coordinate',
     X_coordinate_selection,
     index=None,
     placeholder='Select the X coordinate'
     )

if X_coordinate != None:
    Remove = X_coordinate
    Y_coordinate_selection = tuple(item for item in X_coordinate_selection if item != Remove)

Y_coordinate = st.selectbox(
    'select the Y coordinate',
    Y_coordinate_selection,
    index=None,
    placeholder='Select the Y coordinate'
)



st.write('The material comparison would be: ', X_coordinate, 'vs', Y_coordinate)