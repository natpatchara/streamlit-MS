'''
    Base class for create multipage application base on article by Prakhar Rathi 
    [https://towardsdatascience.com/creating-multipage-applications-using-streamlit-efficiently-b58a58134030]
'''

import streamlit as st

class MultiPage():

    def __init__(self):

        self.pages = []

    def add_page(self, title, func):
        self.pages.append({'title': title, 'func': func})

    def run(self):
        page = st.sidebar.selectbox(
            'App Navigation', 
            self.pages, 
            format_func=lambda page: page["title"]
        )

        # render the app function 
        page["func"]()

'''
class Page():

    def __init__(self,title,func):
        self.title = title
        self.func = func

    def render(self):
        self.func()

class InferencePage(Page):

    def __init__(self,path):
        super.__init__()
        self.model = self.load_model(path)

    def load_model(self, path):
        pass

    def render(self):
        self.func()

'''