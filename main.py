import streamlit as st
from script.multipage import MultiPage
from script import homepage, model1

@st.cache(allow_output_mutation=True)
def init():
    app = MultiPage()
    
    app.add_page("Homepage", homepage.app)
    app.add_page("Model-1", model1.app)

    return app

st.title("Webiste for metabolic syndrome prediction[test ver.]")

#mainPage = Page("Main", main)
#secondPage = Page("Second", main)

app = init()
app.run()

#main()

