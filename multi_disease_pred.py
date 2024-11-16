import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('./notebook/models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('./notebook/models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('./notebook/models/parkinson_model.sav', 'rb'))

lung_cancer_model = pickle.load(open('./notebook/models/lung_cancer_model.sav','rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Lung Cancer'],
                          icons=['activity','heart','person','lungs'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
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
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)

if (selected == 'Lung Cancer'):

    st.title('Lung Cancer Prediction Using ML')

    col1, col2, col3 = st.columns(3)  

    
        
    with col1 :
        Age = st.text_input('AGE')
    
    with col2:
        Smoking = st.text_input('Smoking (YES=2/NO=1)')
        
    
    with col3:
        Yellow_Fingers = st.text_input('Yellow_Fingers (YES=2/NO=1)')
       
    with col1:
        Anxiety = st.text_input('Anxiety (YES=2/NO=1)')
        
    with col2:
        Peer_Pressure = st.text_input('Peer_Pressure (YES=2/NO=1)')
        

    with col3:
        Chronic_Disease = st.text_input('Chronic_Disease (YES=2/NO=1)')
        
    with col1:
        Fatigue = st.text_input('Fatigue (YES=2/NO=1)')
        
    with col2:
        Allergy = st.text_input('Allergy (YES=2/NO=1)')
        

    with col3:
        Wheezing = st.text_input('Wheezing (YES=2/NO=1)')
        
    with col1:
        Alcohol = st.text_input('Alcohol (YES=2/NO=1)')
        
    with col2:
        Couching = st.text_input('Couching (YES=2/NO=1)')
       

    with col3:
        Shortness_of_Breath = st.text_input('Shortness_of_Breath (YES=2/NO=1)')
        
    with col1:
        Swallowing_Difficulty = st.text_input('Swallowing_Difficulty (YES=2/NO=1)')
        
    with col2:
        Chest_Pain = st.text_input('Chest_Pain (YES=2/NO=1)')
    
    #inputs = [ Age,Smoking,Yellow_Fingers,Anxiety,Peer_Pressure,Chronic_Disease,Fatigue,Allergy,Wheezing,Alcohol,Couching,Shortness_of_Breath,Swallowing_Difficulty,Chest_Pain]
    #inputs = np.array([float(i) for i in inputs]).reshape(1, -1)

    lung_cancer = ''
    if st.button('Lung Cancer Prediction'):
        inputs = [ Age,Smoking,Yellow_Fingers,Anxiety,Peer_Pressure,Chronic_Disease,Fatigue,Allergy,Wheezing,Alcohol,Couching,Shortness_of_Breath,Swallowing_Difficulty,Chest_Pain]
        inputs = np.array([float(i) for i in inputs]).reshape(1, -1)
        lung_cancer_prediction = lung_cancer_model.predict(inputs)
        
        if lung_cancer_prediction[0] == 0 :
            lung_cancer = "The person is healthy"
        else :
            lung_cancer = "The person have lung cancer"

    st.success(lung_cancer)



    














