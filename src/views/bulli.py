from src.utils import Layout_template

# :speaking_head:
class Bullying(Layout_template):
    def __init__(self):
        super().__init__()
        
    def header(self):
        self.st.title("Información para quien ejerce bullying")
        self.st.divider()
    
    def main(self):
        self.st.header("Características del agresor")

        self.st.markdown("""
La persona que hace bullying muchas veces
está manejando emociones no resueltas.
""")

        self.st.subheader("Posibles causas")

        self.st.markdown("""
- Inseguridad
- Necesidad de poder
- Problemas familiares
- Falta de empatía
        """)

        self.st.subheader("Consecuencias")

        self.st.markdown("""
- Problemas disciplinarios
- Aislamiento social
- Problemas futuros en relaciones
        """)

        self.st.subheader("Cómo evitar ser agresor")

        self.st.markdown("""
- Practicar empatía
- Controlar impulsos
- Hablar sobre emociones
- Buscar orientación psicológica
        """)

        self.st.success("Cambiar es posible. La empatía es fortaleza.")
    
    def footer(self):
        self.st.divider()
        self.st.caption("La prevención comienza con la educación.")
   
Bullying().render()     