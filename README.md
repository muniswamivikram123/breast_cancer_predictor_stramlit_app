##### This project was built following a YouTube tutorial to learn and implement a machine learning model for breast cancer prediction.

Alejandro AO - Software & Ai


# breast_cancer_predictor_stramlit_app

### step1:
#### install streamlit
> pip install streamlit

#### import the required libraries and try it 

```python
import streamlit as st
import pickle5 as pickle
import pandas as pd

def main():
    st.set_page_config(
        page_title = "breast cancer predictor",
        page_icon = ":female-doctor:"
    )
    st.write("hello world!")

if __name__ == '__main__':
    main()
```
#### output for this:
![image](https://github.com/user-attachments/assets/129e680a-61c0-49a6-9b6a-f61981155dc4)


### step2:

```python
import streamlit as st
import pickle5 as pickle
import pandas as pd
def main():
    st.set_page_config(
        page_title = "breast cancer predictor",
        page_icon = ":female-doctor:",
        layout = "wide",
        initial_sidebar_state = "expanded"
    )
    with st.container():
        st.title("Breast canser predictor")
        st.write("write anything like a paragraph")
    

if __name__ == '__main__':
    main()
```

### output :
![image](https://github.com/user-attachments/assets/c1b35a84-06e1-44ff-8b33-16a573ddb41a)

### step3:
## Creating columns

```python
import streamlit as st
import pickle5 as pickle
import pandas as pd
def main():
    st.set_page_config(
        page_title = "breast cancer predictor",
        page_icon = ":female-doctor:",
        layout = "wide",
        initial_sidebar_state = "expanded"
    )
    with st.container():
        st.title("Breast cancer predictor")
        st.write("write anything like a paragraph")

    col1,col2 = st.columns([4,1])
    with col1:
        st.write("this is column 1")
    
    with col2:
        st.write("this is column 2")
    

if __name__ == '__main__':
    main()
```

#### output :
![image](https://github.com/user-attachments/assets/34f8225e-95b9-4fdc-8458-829caf4d8208)

### step4:
#### adding sidebar

```python
import streamlit as st
import pickle5 as pickle
import pandas as pd

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
        st.sidebar.slider(
            label,
            min_value =0,
            max_value = 100
        )


     

def main():
    st.set_page_config(
        page_title = "breast cancer predictor",
        page_icon = ":female-doctor:",
        layout = "wide",
        initial_sidebar_state = "expanded"
    )

    add_sidebar()
    with st.container():
        st.title("Breast cancer predictor")
        st.write("write anything like a paragraph")

    col1,col2 = st.columns([4,1])
    with col1:
        st.write("this is column 1")
    
    with col2:
        st.write("this is column 2")
    

if __name__ == '__main__':
    main()

```

output:
![image](https://github.com/user-attachments/assets/0033efa9-5219-4bd5-a265-0a1b25919921)

### step4:

#### maximum value
##### instead of keeping 100 as a maximum keep actual value in the dataset 
```python
for label,key in slider_labels:
        st.sidebar.slider(
            label,
            min_value =float(0),
            max_value =float(data[key].max())
        )
```

#### output :
![image](https://github.com/user-attachments/assets/0cdd4860-d16f-4f55-94e6-bbd72b638cfb)

### for average

```python
for label,key in slider_labels:
        st.sidebar.slider(
            label,
            min_value =float(0),
            max_value =float(data[key].max()),
            value =float(data[key].mean())
        )
```

### output:
![image](https://github.com/user-attachments/assets/78f20beb-b4c1-4a93-aefb-8cc404c8db76)

## creating the chart

#### visit this site and copy the code and paste it
> https://plotly.com/python/radar-chart/

```python
import plotly.graph_objects as go

categories = ['processing cost','mechanical properties','chemical stability',
              'thermal stability', 'device integration']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[1, 5, 2, 2, 3],
      theta=categories,
      fill='toself',
      name='Product A'
))
fig.add_trace(go.Scatterpolar(
      r=[4, 3, 2.5, 1, 2],
      theta=categories,
      fill='toself',
      name='Product B'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5]
    )),
  showlegend=False
)

fig.show()
```

```python
import streamlit as st
import pickle5 as pickle
import pandas as pd
import plotly.graph_objects as go


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

def get_radar_chart():
    categories = ['processing cost','mechanical properties','chemical stability',
              'thermal stability', 'device integration']

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[1, 5, 2, 2, 3],
        theta=categories,
        fill='toself',
        name='Product A'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[4, 3, 2.5, 1, 2],
        theta=categories,
        fill='toself',
        name='Product B'
    ))

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 5]
        )),
    showlegend=False
    )

    fig.show()
     

def main():
    st.set_page_config(
        page_title = "breast cancer predictor",
        page_icon = ":female-doctor:",
        layout = "wide",
        initial_sidebar_state = "expanded"
    )


    input_data = add_sidebar()
   



    with st.container():
        st.title("Breast cancer predictor")
        st.write("write anything like a paragraph")

    col1,col2 = st.columns([4,1])
    with col1:
        get_radar_chart(input_data)
    
    with col2:
        st.write("this is column 2")
    

if __name__ == '__main__':
    main()
```


## the final output 
### for **benign**

![image](https://github.com/user-attachments/assets/11130f7d-7fac-49cc-8187-967eb836a283)

### for **malicious**
![image](https://github.com/user-attachments/assets/b92ff35b-265b-4633-a54e-f1dd45597827)


## the final code

```python
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
```







