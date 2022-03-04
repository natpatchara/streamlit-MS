#Model 3 importance factor
import streamlit as st

st.title('ML sydrome prediction(model3)')

with st.form(key='Model_form'):
    c11, c12 = st.columns(2)
    age = c11.number_input('Enter a age:')
    wc = c12.number_input("Enter a waist circumference")
    c21, c22 = st.columns((1, 2))
    weight = c21.number_input('Enter a weight(kg):', value=0)
    height = c22.number_input('Enter a height(cm):',value=120)
    c31, c32 = st.columns((1, 1))
    is_BMI = c31.checkbox("Do you have calculated BMI")
    bmi = c32.number_input("Enter your bmi")
    if (is_BMI):
        pass
    else:
        bmi = weight / (height / 100) / (height / 100)
    c41, c42 = st.columns((1, 1))
    sbp = c41.number_input('Enter a systolic blood pressure:')
    dbp = c42.number_input('Enter a diastolic blood pressure:')
    c51, c52= st.columns(2)
    fbs = c51.number_input('Enter a fasting blood glucose:')
    tg = c52.number_input('Enter a triglyceride level:')
    c61, c62= st.columns(2)
    hdl = c61.number_input('Enter a HDL level:')
    ldl = c62.number_input('Enter a LDL level:')
    c71, c72= st.columns((1,1))
    nafld = c71.checkbox('Have you ever have NAFLD/MAFLD')
    ast = c72.number_input('Enter a AST level:')
    
    submitted = st.form_submit_button('Submit')

def model(**arg):
    return 0

if (submitted):
    #res = model()
    st.write("Your input")
    st.write("Age: {}".format(age))
    st.write("Waist circumference: {}".format(wc))
    st.write("BMI: {}".format(bmi))
    st.write("DBP: {}".format(dbp))
    st.write("SBP: {}".format(sbp))
    st.write("FBS: {}".format(fbs))
    st.write("TG: {}".format(tg))
    st.write("HDL: {}".format(hdl))