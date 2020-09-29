import streamlit as st
import pickle
import numpy as np


model=pickle.load(open('model.pkl','rb'))

def credit_default_predict(LIMIT_BAL,EDUCATION,MARRIAGE,AGE,PAY_1,BILL_AMT1,BILL_AMT2,
       BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,
       PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6):
        input=np.array([[LIMIT_BAL,EDUCATION,MARRIAGE,AGE,PAY_1,BILL_AMT1,BILL_AMT2,
       BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,
       PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6]]).astype(np.float64)
        prediction=model.predict(input)
        return prediction


def main():
    st.title("credit_default_prediction")
    html_temp="""
    <div style="background-color:#01DFD7 ;padding:10px">
    <h2 style="color:white;text-align:center;">credit_default_prediction App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    LIMIT_BAL = st.text_input("LIMIT_BAL","Type Here")
    EDUCATION= st.text_input("EDUCATION","Type Here")
    MARRIAGE= st.text_input("MARRIAGE","Type Here")
    AGE= st.text_input("AGE","Type Here")
    PAY_1= st.text_input("PAY_1","Type Here")
    BILL_AMT1= st.text_input("BILL_AMT1","Type Here")
    BILL_AMT2= st.text_input("BILL_AMT2","Type Here")
    BILL_AMT3= st.text_input("BILL_AMT3","Type Here")
    BILL_AMT4= st.text_input("BILL_AMT4","Type Here")
    BILL_AMT5= st.text_input("BILL_AMT5","Type Here")
    BILL_AMT6= st.text_input("BILL_AMT6","Type Here")
    PAY_AMT1= st.text_input("PAY_AMT1","Type Here")
    PAY_AMT2= st.text_input("PAY_AMT2","Type Here")
    PAY_AMT3= st.text_input("PAY_AMT3","Type Here")
    PAY_AMT4= st.text_input("PAY_AMT4","Type Here")
    PAY_AMT5= st.text_input("PAY_AMT5","Type Here")
    PAY_AMT6= st.text_input("PAY_AMT6","Type Here")
  
    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Low chances of defaulting account :Does not Require Counseling</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> High chances of defaulting account : Require Counseling</h2>
       </div>
    """
    if st.button("Predict"):
        output= credit_default_predict(LIMIT_BAL,EDUCATION,MARRIAGE,AGE,PAY_1,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6)
        if output>0.5:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)
if __name__=='__main__':
    main()
