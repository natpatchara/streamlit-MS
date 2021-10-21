import streamlit as st

@st.cache(suppress_st_warning=True)
def load_model(path):
    pass

@st.cache(suppress_st_warning=True)
def predict(model, X):
    return model.predict(X)

def app():

    path = ""
    st.title('ML sydrome prediction')

    with st.form(key='Model_form'):
        c11, c12 = st.columns(2)
        name = c11.text_input("Enter a name:")
        surname = c12.text_input("Enter a surname")
        c21, c22 = st.columns((1, 1))
        is_middlename = c21.checkbox("Do you have middlename")
        if (is_middlename):
            middlename = c22.text_input("Enter your middlename")
        else:
            middlename = ''
        c31, c32 = st.columns((1, 2))
        age = c31.number_input('Enter a age:')
        DOB = c32.date_input('Date of birth:')
        c41, c42 = st.columns(2)
        weight = st.number_input('Enter a weight(kg):')
        height = st.number_input('Enter a height(cm):', 120)
        submitted = st.form_submit_button('Submit')

    if (submitted):

        X = []
        model = load_model(path)
        res = predict(model, X)
        st.write("Prediction is {}".format(res))