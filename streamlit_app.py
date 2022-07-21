import numpy as np
import pickle

import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

loaded_model = pickle.load(open('trainedfinalheartmodel1.sav', 'rb'))

def heart(input_data):

    input_data_as_numpy_array = np.asarray(input_data)
    input_reshape = input_data_as_numpy_array.reshape(1,-1)


    prediction = loaded_model.predict(input_reshape)
   
   


    if (prediction[0]==0):
        return st.success('This person has less chance of heart attack')
    else:
        return st.error('This person has more chance of heart attack')
        
        
def main():
    
   
    st.title('HEART DISEASE PREDICTION')
    
    name = st.text_input('Enter Your Name')
    st.write('Input:', name)

    age = st.text_input('AGE')
    st.write('You selected:', age)
    
    
    sex = st.radio("SELECT GENDER: (1 : MALE & 0 : FEMALE)", ('1', '0'))
    if (sex == '1'):
        st.info("Male")
    else:
        st.info("Female")
    st.write('You selected:', sex)

    st.write('<style>div.row-widget.stRadio>div{flex-direction:row;}</style>',unsafe_allow_html=True)
 
    st.write('CHEST PAIN TYPE (1 = TYPICAL ANGINA, 2 = ATYPICAL ANGINA, 3 : NON ANGINAL PAIN, 4 : ASYMPTOTIC')    
    chestpaintype = st.radio("CHEST PAIN RANGING FROM LEVELS OF PAIN",('1','2','3','4'))
    st.write('You selected:', chestpaintype)
    restingbps = st.text_input('RESTING BLOOD PRESSURE')
    st.write('You selected:', restingbps)
    cholestrol = st.text_input('CHOLESTROL')
    st.write('You selected:', cholestrol)
    
    fastingbloodsugar = st.radio("FASTING BLOOD SUGAR ( IF > 120mg/l YES : 1, NO : 0)", ('1','0'))
    st.write('You selected:', fastingbloodsugar)
    restingecg = st.radio("RESTING ECG(0 : NORMAL, 1 : ABNORMAL)",('0','1'))
    st.write('You selected:', restingecg)
    maxheartrate = st.text_input('MAXIMUM HEART RATE ACHIEVED') 
    st.write('You selected:', maxheartrate)
    exerciseangina = st.radio("EXERCISE INDUCED ANGINA (1 : YES, 0 : NO)", ('1','0'))
    st.write('You selected:', exerciseangina)
    oldpeak = st.text_input('ST DEPRESSION INDUCED BY EXERCISE REALTIVE TO REST / OLDPEAK')
    st.write('You selected:', oldpeak)
    STslope = st.selectbox(
     "PEAK EXERCISE ST SEGMENT (0 : UPSLOPPING, 1 : FLAT, 2 : DOWNSLOPPING)", ('0','1','2'))

    st.write('You selected:', STslope)


    st.write('PLEASE REVIEW YOUR FILLED DATA')
    data = {'Name' : name, 'Age ' : age , 'Sex' : sex, 'Chest Pain Type' : chestpaintype, 'Resting Blood Pressure' :  restingbps, 'Cholestrol' : cholestrol, 'Fasting Blood Sugar' : fastingbloodsugar, 'Resting ECG' : restingecg, 'Max Heart Rate' : maxheartrate, 'Exercise Induced Angina' : exerciseangina, 'Old Peak' : oldpeak, 'ST Slope' : STslope}
    
    df = pd.DataFrame(data, index = ['values'])
    

    st.dataframe(df)  # Same as st.write(df)

    
    submit = st.button('SUBMIT')

    diagnosis = ''
 
    
    if submit:
        diagnosis = heart([age,sex,chestpaintype,restingbps,cholestrol,fastingbloodsugar,restingecg,maxheartrate,exerciseangina,oldpeak,STslope])

   
    

if __name__ == '__main__':
    main()  
