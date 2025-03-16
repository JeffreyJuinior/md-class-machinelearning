import streamlit as st

def main():

  st.title('Machine Learning App')
  st.info('This app for dhermatology classification')

  erythema = st.slider('Erythema', min_value = 0, max_value = 3, value = 2)
  scaling = st.slider('Scaling', min_value = 0, max_value = 3, value = 2)
  definite_borders = st.slider('Definite Borders', min_value = 0, max_value = 3, value = 2)
  


if __name__=="__main__":
  main()
