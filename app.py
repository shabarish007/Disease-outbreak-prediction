import os 
import streamlit as st
import pickle 
from streamlit_option_menu import option_menu

st.set_page_config(page_title="prediction of disease outbreaks",layout="wide",page_icon=":doctor:")
wrk_dir=os.path.dirname(os.path.abspath(__file__))

diabetes_model=pickle.load(open(r"C:\\Users\\pshab\\Desktop\\aicte\\saved models\\diabetes_pred_model.sav",'rb'))

heart_disease_model=pickle.load(open(r"C:\\Users\\pshab\Desktop\\aicte\\saved models\\heart_disease_model.sav",'rb'))

parkinson_disease_model=pickle.load(open(r"C:\\Users\\pshab\Desktop\\aicte\\saved models\\parkinson_disease_model.sav",'rb'))

with st.sidebar:
    selected=option_menu('Prediction of Disease Outbreaks',
                         ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                         menu_icon='hospital-fill',
                         icons=['activity','heart','person'],
                         default_index=0)
    
if selected=='Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis=''
    if st.button('Test Result'):
        user_input=[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        user_input=[float(x) for x in user_input]
        diag_pred=diabetes_model.predict([user_input])
        if diag_pred[0]==1:
            diab_diagnosis='This person is diabetic'
        else:
            diab_diagnosis='This person is not diabetic'
    st.success(diab_diagnosis)

if selected == 'Parkinsons Prediction':
    st.title('Parkinson’s Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        MDVP_Fo_Hz = st.text_input('MDVP:Fo(Hz)')
        MDVP_Flo_Hz = st.text_input('MDVP:Flo(Hz)')
        MDVP_RAP = st.text_input('MDVP:RAP')
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
        NHR = st.text_input('NHR')
        RPDE = st.text_input('RPDE')
        spread1 = st.text_input('spread1')

    with col2:
        MDVP_Fhi_Hz = st.text_input('MDVP:Fhi(Hz)')
        MDVP_Jitter_percent = st.text_input('MDVP:Jitter(%)')
        MDVP_PPQ = st.text_input('MDVP:PPQ')
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
        HNR = st.text_input('HNR')
        DFA = st.text_input('DFA')
        spread2 = st.text_input('spread2')

    with col3:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        Jitter_DDP = st.text_input('Jitter:DDP')
        MDVP_APQ = st.text_input('MDVP:APQ')
        Shimmer_DDA = st.text_input('Shimmer:DDA')
        D2 = st.text_input('D2')
        PPE = st.text_input('PPE')

    parkinson_diagnosis = ''

    if st.button('Test Result'):
        # Gather user inputs
        user_input = [
            MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent, 
            MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, 
            MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, 
            Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE
        ]
        
        # Convert inputs to float
        user_input = [float(x) for x in user_input]

        # Use the Parkinson's disease model for prediction
        parkinson_pred = parkinson_disease_model.predict([user_input])
        
        if parkinson_pred[0] == 1:
            parkinson_diagnosis = 'This person may have Parkinson’s disease.'
        else:
            parkinson_diagnosis = 'This person does not have Parkinson’s disease.'

    st.success(parkinson_diagnosis)

if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
        cp = st.text_input('Chest Pain Type (cp)')
        chol = st.text_input('Cholesterol Level (chol)')
        restecg = st.text_input('Resting ECG results (restecg)')
        slope = st.text_input('Slope of peak exercise (slope)')

    with col2:
        sex = st.text_input('Sex (1 = Male, 0 = Female)')
        trestbps = st.text_input('Resting Blood Pressure (trestbps)')
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (fbs)')
        thalach = st.text_input('Maximum Heart Rate (thalach)')
        ca = st.text_input('Number of major vessels (ca)')

    with col3:
        exang = st.text_input('Exercise Induced Angina (exang)')
        oldpeak = st.text_input('ST Depression induced by exercise (oldpeak)')
        thal = st.text_input('Thalassemia (thal)')

    heart_diagnosis = ''

    if st.button('Test Result'):
        user_input = [
            age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, 
            oldpeak, slope, ca, thal
        ]
        
        user_input = [float(x) for x in user_input]

        heart_pred = heart_disease_model.predict([user_input])
        
        if heart_pred[0] == 1:
            heart_diagnosis = 'This person may have heart disease.'
        else:
            heart_diagnosis = 'This person does not have heart disease.'

    st.success(heart_diagnosis)
