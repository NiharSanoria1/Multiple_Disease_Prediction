## v-AI-dya - Diagnosis Website

This repository contains the code for the Diagnosis Website component of the VAIDIYA project. The diagnosis website allows users to input their medical test results and receive a potential diagnosis based on trained machine learning models.

## Features

User- friendly interface to input medical test results.
Real-time disease prediction based on machine learning algorithms.
Visual representation of input data and prediction outcomes using charts and graphs.

## Technologies Used

Python 3.12: Core programming language for development.
Streamlit: Framework used to create the interactive web application.
Streamlit Option Menu: For creating a structured and navigable sidebar.
Sklearn: Machine learning library for model development and evaluation.
Seaborn: For creating attractive and informative statistical graphics.
Matplotlib: For basic plotting and data visualization.
Pandas: For efficient data manipulation and analysis.
NumPy: For numerical computations and data handling.

## Setup and Installation

# Clone this repository:

git clone https://github.com/your-repo/Multiple_Disease_Prediction.git  
cd Multiple_Disease_Prediction

# Install the required dependencies:

pip install -r requirements.txt  

# Run the Streamlit app:

streamlit run app.py  

## How It Works

Input Medical Data:
Users enter their test results into a form on the website.

Model Prediction:
The app processes the input data and uses a pre-trained machine learning model to predict potential diseases.

File Structure

multi_disease_pred.py : Main application file for Streamlit.
model.sav: Pre-trained machine learning model used for predictions.
requirements.txt: List of dependencies required to run the application.
notebook/data/: Folder containing sample datasets.
notebook/model : Folder containing trained model.

The website is deployed on Streamlit .

website link :

https://multidiseaseprediction.streamlit.app/
