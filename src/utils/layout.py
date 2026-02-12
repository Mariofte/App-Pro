import streamlit as st
from streamlit.errors import Error
from streamlit.commands.page_config import PageIcon, Layout, InitialSideBarState, MenuItems
from abc import ABC, abstractmethod


class Layout_template(ABC):
    def __init__(self, title:str, icon:PageIcon, layout:Layout, sidebar:InitialSideBarState, menu:MenuItems):
        super().__init__()
        self.st = st
        self.title:str = title
        self.icon:PageIcon = PageIcon
        self.layout:Layout = layout
        self.sidebar:InitialSideBarState = sidebar
        self.menu:MenuItems = menu
    
    def render(self) -> None:
        try:
            self.head()
            self.body()
        
        except (Exception, Error) as e:
            self.st.error(f"Error in your code:{e}")
    
    def head(self) -> None:
        self.st.set_page_config(
            page_title=self.menu,
            page_icon=self.icon,
            layout=self.layout,
            initial_sidebar_state=self.sidebar,
            menu_items=self.menu
        )
        
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