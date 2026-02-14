import streamlit as st
import os

from streamlit.navigation.page import StreamlitPage
from streamlit.errors import Error

class App:
    def __init__(self):
        self.st = st
        self.os = os
    
    def load(self) -> None:
        try:
            self.st.set_page_config(
                page_title="Web App",
                page_icon="🚀",
                layout="wide",
                initial_sidebar_state="expanded",
                
            )
                
            self.st.navigation(
                self._build_pages(),
                position="sidebar",
                expanded=True
            ).run()
        
        except Error as e:
            self.st.warning(f"Error al cargar la aplicación: {e}")
    
    def _build_pages(self) -> dict[str, list[StreamlitPage]]:
        return {
            "Inicio": [
                self.st.Page(
                    page=os.path.join("src", "views", "index.py"),
                    title="Inicio",
                    icon="🏠",
                    url_path="/",
                    default=True
                )
            ],
            
            "Paginas": [
                # src\views\victim.py
                self.st.Page(
                    page=os.path.join("src", "views", "victim.py"),
                    title="Victima",
                    url_path="/victima"
                ),
                self.st.Page(
                    page=os.path.join("src", "views", "bulli.py"),
                    title="Bullying",
                    url_path="/bullying"
                )
            ]
        }
        