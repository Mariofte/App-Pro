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
            self.st.navigation(
                self._build_pages(),
                position="sidebar",
                expanded=True
            ).run()
        
        except Error as e:
            self.st.warning(f"Error al cargar la aplicación: {e}")
    
    def path(self) -> str:
        return self.os.path.dirname(self.os.path.abspath(__file__))
    
    def _build_pages(self) -> dict[str, list[StreamlitPage]]:
        return {
            "Inicio": [
                self.st.Page(
                    page=self.path() + "\\views\\index.py",
                    title="Inicio",
                    icon="🏠",
                    url_path="/",
                    default=True
                )
            ]
        }
        