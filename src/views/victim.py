from src.utils.layout import Layout_template

# :speaking_head:
class Victim(Layout_template):
    def __init__(self):
        super().__init__(
            "victim",
            icon=":busts_in_silhouette:",
            layout="centered",
            sidebar="auto",
            menu={
                "Get Help" : "marioftetriana@gmail.com",
                "Escuela": "https://cervantestorreon.edu.mx"
            }
        )
        
    def header(self):
        self.st.title("Victim")
    
    def main(self):
        self.st.write("Hola marioftetriana@gmail.com")
    
    def footer(self):
        self.st.write("footer")
        