from turtle import st
from src.utils import Layout_template

# :speaking_head:
class Victim(Layout_template):
    def __init__(self):
        super().__init__()
        
    def header(self):
        self.st.title("Información para la Víctima")
        self.st.divider()

    def main(self):
        self.st.header("Características de la víctima")

        self.st.markdown("""
Cualquier persona puede ser víctima.
No es su culpa.
""")

        self.st.subheader("Señales emocionales")

        self.st.markdown("""
- Tristeza
- Ansiedad
- Baja autoestima
- Miedo a la escuela
        """)

        self.st.subheader("Señales físicas o académicas")

        self.st.markdown("""
- Dolores frecuentes
- Bajo rendimiento escolar
- Aislamiento
        """)

        self.st.subheader("Cómo prevenir o detener la situación")

        self.st.markdown("""
- Hablar con un adulto
- No quedarse en silencio
- Buscar apoyo en amigos
- Reportar a la escuela
        """)

        self.st.success("Pedir ayuda es un acto de valentía.")

    def footer(self):
        self.st.divider()
        self.st.caption("No estás solo. Siempre hay ayuda disponible.")

Victim().render()