#======== Imports ========#

import streamlit as st # type: ignore

#======== Titles ========#

st.title('Material Analysis Database')
st.write('Web app for custom material selection & analysis. Define your own axes & criteria. Explore, analyze, discover.')

#======== Sidebar ========#

st.sidebar.header('Control Panel')
st.sidebar.write("")

with st.sidebar.expander('About this app'): 
     st.write("This is an open source analysis web app tool to further analyze material selection data, with the open-source code available [here](https://github.com/CizerSkizerBigger/MaterialAnalysisDatabase-MAD-)")

#======== Content ========#

st.header('Parameter Selection', divider=True)
st.write('In this section, select the relevent parameters to be determined for x and y axis')

col1, col2, col3 = st.columns(3)

X_coordinate_selection = ('Price', 'Performance', 'Ratio')
Y_coordinate_selection = None

with col1:
     X_coordinate = st.selectbox(
     'Select the X coordinate',
     X_coordinate_selection,
     index=None,
     placeholder='X coordinate'
     )

if X_coordinate != None:
    Remove = X_coordinate
    Y_coordinate_selection = tuple(item for item in X_coordinate_selection if item != Remove)

with col2:
    Y_coordinate = st.selectbox(
    'select the Y coordinate',
    Y_coordinate_selection,
    index=None,
    placeholder='Y coordinate'
    ) 

st.write('The material comparison would be: ', X_coordinate, 'vs', Y_coordinate)
