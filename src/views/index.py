from src.utils import Layout_template

# :speaking_head:
class Index(Layout_template):
    def __init__(self):
        super().__init__()
        
    def header(self):
        self.st.title("🛑 Prevención del Bullying")
        self.st.subheader("Información y concientización escolar")
        self.st.divider()
    
    def main(self):
        self.st.header("¿Qué es el bullying?")

        self.st.markdown("""
                El bullying es una forma de violencia repetida en la que una persona
                intenta dañar física, emocional o socialmente a otra.

                Se caracteriza por un desequilibrio de poder.
                """)

        self.st.subheader("Características principales")

        self.st.markdown("""
- Es repetitivo
- Existe intención de dañar
- Hay desequilibrio de poder
- Puede ser físico, verbal o psicológico
        """)

        self.st.subheader("Tipos de bullying")

        self.st.markdown("""
- 👊 Físico
- 🗣 Verbal
- 🚫 Social
- 💻 Ciberbullying
        """)
    
    def footer(self):
        self.st.divider()
        self.st.caption("Proyecto escolar informativo sobre prevención del bullying")

if __name__ == "__main__":
    Index().render()