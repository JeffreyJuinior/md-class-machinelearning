import streamlit as st

def main():

  st.title('Machine Learning App')
  st.info('This app for dhermatology classification')

  erythema = st.slider('erythema', min_value = 0, max_value = 3, value = 2)
  
  


if __name__=="__main__":
  main()
