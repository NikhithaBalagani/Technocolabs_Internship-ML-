import streamlit as st
import pickle
import numpy as np


# In[12]:


model=pickle.load(open('model.pk1','rb'))


# In[20]:


def predict_parkinsons(Fo_Hz,Fhi_Hz,Flo_Hz,Jitter_p,Jitter_Abs,RAP,PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE):
        input=np.array([[Fo_Hz,Fhi_Hz,Flo_Hz,Jitter_p,Jitter_Abs,RAP,PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]]).astype(np.float64)
        prediction=model.predict(input)
        return prediction


# In[ ]:





# In[17]:





# In[ ]:





# In[22]:


def main():
    st.title("parkinsos_disease_prediction")
    html_temp="""
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">parkinsons diease prediction App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Fo_Hz = st.text_input("Fo_Hz","Type Here")
    Fhi_Hz= st.text_input("Fhi_Hz","Type Here")
    Flo_Hz= st.text_input("Flo_Hz","Type Here")
    Jitter_p= st.text_input("Jitter_p","Type Here")
    Jitter_Abs= st.text_input("Jitter_Abs","Type Here")
    RAP= st.text_input("RAP","Type Here")
    PPQ= st.text_input("PPQ","Type Here")
    DDP= st.text_input("DDP","Type Here")
    Shimmer= st.text_input("Shimmer","Type Here")
    Shimmer_dB= st.text_input("Shimmer_dB","Type Here")
    APQ3= st.text_input("APQ3","Type Here")
    APQ5= st.text_input("APQ5","Type Here")
    APQ= st.text_input("APQ","Type Here")
    DDA= st.text_input("DDA","Type Here")
    NHR= st.text_input("NHR","Type Here")
    HNR= st.text_input("HNR","Type Here")
    RPDE= st.text_input("RPDE","Type Here")
    DFA= st.text_input("DFA","Type Here")
    spread1= st.text_input("spread1","Type Here")
    spread2= st.text_input("spread2","Type Here")
    D2= st.text_input("D2","Type Here")
    PPE= st.text_input("PPE","Type Here")
    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> You do not have parkinsons disease</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> You have parkinsons disease: consult doctor</h2>
       </div>
    """
    if st.button("Predict"):
        output=predict_parkinsons(Fo_Hz,Fhi_Hz,Flo_Hz,Jitter_p,Jitter_Abs,RAP,PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE)

        if output ==1:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)
if __name__=='__main__':
    main()


