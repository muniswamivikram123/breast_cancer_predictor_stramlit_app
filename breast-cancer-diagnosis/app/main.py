import streamlit as st
import pickle5 as pickle
import pandas as pd
import plotly.graph_objects as go
import numpy as np


def get_clean_data():
    data = pd.read_csv("data\data.csv")
    #print(data.head())
    # droping the Unnamed and id because unnamed have Nan value and id is not required
    data = data.drop(['Unnamed: 32','id'], axis=1)
    # now we have to encode the data of diagnosis
    data['diagnosis'] = data['diagnosis'].map({'M':1,'B':0})
    #print(data)
    #print(data)
    return data

def add_sidebar():
    st.sidebar.header("Cell Nuclei Measurements")

    data = get_clean_data()

    slider_labels = [
        ("Radius (mean)", "radius_mean"),
        ("Texture (mean)", "texture_mean"),
        ("Perimeter (mean)", "perimeter_mean"),
        ("Area (mean)", "area_mean"),
        ("Smoothness (mean)", "smoothness_mean"),
        ("Compactness (mean)", "compactness_mean"),
        ("Concavity (mean)", "concavity_mean"),
        ("Concave points (mean)", "concave points_mean"),
        ("Symmetry (mean)", "symmetry_mean"),
        ("Fractal dimension (mean)", "fractal_dimension_mean"),
        ("Radius (se)", "radius_se"),
        ("Texture (se)", "texture_se"),
        ("Perimeter (se)", "perimeter_se"),
        ("Area (se)", "area_se"),
        ("Smoothness (se)", "smoothness_se"),
        ("Compactness (se)", "compactness_se"),
        ("Concavity (se)", "concavity_se"),
        ("Concave points (se)", "concave points_se"),
        ("Symmetry (se)", "symmetry_se"),
        ("Fractal dimension (se)", "fractal_dimension_se"),
        ("Radius (worst)", "radius_worst"),
        ("Texture (worst)", "texture_worst"),
        ("Perimeter (worst)", "perimeter_worst"),
        ("Area (worst)", "area_worst"),
        ("Smoothness (worst)", "smoothness_worst"),
        ("Compactness (worst)", "compactness_worst"),
        ("Concavity (worst)", "concavity_worst"),
        ("Concave points (worst)", "concave points_worst"),
        ("Symmetry (worst)", "symmetry_worst"),
        ("Fractal dimension (worst)", "fractal_dimension_worst"),
    ]


  

    input_dict = {}


    for label,key in slider_labels:
        input_dict[key] = st.sidebar.slider(
            label,
            min_value =float(0),
            max_value =float(data[key].max()),
            value =float(data[key].mean())
        )
    
    return input_dict


def add_predictions(input_data):
  model = pickle.load(open("model/model.pkl", "rb"))
  scaler = pickle.load(open("model/scaler.pkl", "rb"))
  
  input_array = np.array(list(input_data.values())).reshape(1, -1)
  
  input_array_scaled = scaler.transform(input_array)
  
  prediction = model.predict(input_array_scaled)
  
  st.subheader("Cell cluster prediction")
  st.write("The cell cluster is:")
  
  if prediction[0] == 0:
    st.write("<span class='diagnosis benign'>**Benign**</span>", unsafe_allow_html=True)
  else:
    st.write("<span class='diagnosis malicious'>**Malicious**</span>", unsafe_allow_html=True)
    
  
  st.write("Probability of being benign: ", model.predict_proba(input_array_scaled)[0][0])
  st.write("Probability of being malicious: ", model.predict_proba(input_array_scaled)[0][1])
  
  st.write("This app can assist medical professionals in making a diagnosis, but should not be used as a substitute for a professional diagnosis.")

def main():
    st.set_page_config(
        page_title = "breast cancer predictor",
        page_icon = ":female-doctor:",
        layout = "wide",
        initial_sidebar_state = "expanded"
    )

    st.markdown("""
    <style>
    .diagnosis.benign {
        background-color: #00FFFF; /* Green background for Benign */
        color: white; /* White text for contrast */
        padding: 10px 20px; /* Padding for button-like appearance */
        border-radius: 5px; /* Rounded corners */
        font-weight: bold; /* Bold text */
        display: inline-block; /* Inline block for button appearance */
    }

    .diagnosis.malicious {
        background-color: #dc3545; /* Red background for Malicious */
        color: white; /* White text for contrast */
        padding: 10px 20px; /* Padding for button-like appearance */
        border-radius: 5px; /* Rounded corners */
        font-weight: bold; /* Bold text */
        display: inline-block; /* Inline block for button appearance */
    }
</style>

    """, unsafe_allow_html=True)


    input_data = add_sidebar()
   



    with st.container():
        st.title("Breast cancer predictor")
        

        add_predictions(input_data)

    

if __name__ == '__main__':
    main()