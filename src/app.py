import streamlit as st

from streamlit.navigation.page import StreamlitPage
from streamlit.errors import Error

class App:
    def __init__(self):
        self.st = st
    
    def load(self) -> None:
        try:
            self.st.navigation(
                self._build_pages(),
                position="sidebar",
                expanded=True
            ).run()
        
        except (Exception | Error) as e:
            self.st.error(f"Error al cargar la aplicación: {e}")
    
    def _build_pages(self) -> dict[str, list[StreamlitPage]]:
        return {
            "Inicio": [
                self.st.Page(
                    page="src\views\index.py",
                    title="Inicio",
                    icon="🏠",
                    url_path="/",
                    default=True
                )
            ]
        }
        