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
