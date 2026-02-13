import streamlit as st
from streamlit.errors import Error
from abc import ABC, abstractmethod


class Layout_template(ABC):
    def __init__(self):
        super().__init__()
        self.st = st
    
    def render(self) -> None:
        try:
            self.body()
        
        except Error as e:
            self.st.error(f"Error in your code:{e}")
        
    def body(self) -> None:
        self.header()
        self.main()
        self.footer()
    
    @abstractmethod
    def header(self) -> None:
        pass
    
    @abstractmethod
    def main(self) -> None:
        pass
    
    @abstractmethod
    def footer(self) -> None:
        pass