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


