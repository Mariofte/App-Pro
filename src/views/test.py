from src.utils import Layout


PREGUNTAS = [
    # (pregunta, categoria)  V=victima, A=agresor, T=testigo
    ("¿Alguna vez alguien en tu escuela se ha burlado de ti repetidamente?",        "V"),
    ("¿Sientes miedo o ansiedad cuando tienes que ir a la escuela?",                "V"),
    ("¿Te han excluido a propósito de grupos o actividades sociales?",              "V"),
    ("¿Alguien te ha quitado o dañado tus cosas sin tu permiso?",                  "V"),
    ("¿Has recibido mensajes hirientes o humillantes por internet o celular?",      "V"),

    ("¿Has insultado o te has burlado de algún compañero para sentirte superior?",  "A"),
    ("¿Has excluido a alguien del grupo para que se sienta mal?",                   "A"),
    ("¿Has amenazado a alguien para conseguir lo que quieres?",                     "A"),
    ("¿Has golpeado, empujado o lastimado físicamente a un compañero?",             "A"),
    ("¿Has publicado algo en redes para avergonzar a alguien?",                     "A"),

    ("¿Has visto cómo alguien maltrata a un compañero y no hiciste nada?",          "T"),
    ("¿Te da miedo defender a alguien que es víctima de bullying?",                 "T"),
    ("¿Conoces a alguien en tu escuela que esté sufriendo bullying?",               "T"),
    ("¿Has compartido o reenviado mensajes que humillan a un compañero?",           "T"),
    ("¿Ríes o sigues la corriente cuando alguien molesta a otro?",                  "T"),
]

RESULTADOS = {
    "V": {
        "titulo":  "🟣 Posible Víctima",
        "color":   "violet",
        "mensaje": (
            "Las respuestas indican que podrías estar viviendo una situación de bullying. "
            "Recuerda: **no es tu culpa**. Habla con un adulto de confianza, "
            "un maestro o familiar. Pedir ayuda es un acto de valentía."
        ),
    },
    "A": {
        "titulo":  "🔴 Posible Agresor",
        "color":   "red",
        "mensaje": (
            "Algunas respuestas sugieren conductas de agresión hacia otros. "
            "Reflexiona sobre cómo tus acciones afectan a los demás. "
            "Hablar con un orientador o psicólogo puede ayudarte a manejar "
            "tus emociones de forma positiva. **Cambiar siempre es posible.**"
        ),
    },
    "T": {
        "titulo":  "🟡 Posible Testigo",
        "color":   "orange",
        "mensaje": (
            "Pareces ser testigo de situaciones de bullying. "
            "Los testigos tienen un papel clave: **tu voz puede marcar la diferencia**. "
            "Reporta lo que ves a un adulto y apoya a quien lo necesita. "
            "No actuar también es una forma de permitir el bullying."
        ),
    },
    "N": {
        "titulo":  "🟢 Sin indicadores claros",
        "color":   "green",
        "mensaje": (
            "No se detectaron indicadores fuertes de ningún rol. "
            "Sigue promoviendo un ambiente escolar seguro y respetuoso."
        ),
    },
}


class Test(Layout):
    def __init__(self):
        super().__init__()

    # ------------------------------------------------------------------ #
    def header(self):
        self.st.title("🧪 Test: ¿Cuál es tu rol?")
        self.st.markdown(
            "Responde con honestidad. Este test es **confidencial** y solo busca orientarte."
        )
        self.st.divider()

    # ------------------------------------------------------------------ #
    def main(self):
        st = self.st

        # Inicializar estado
        if "test_respuestas" not in st.session_state:
            st.session_state.test_respuestas = {}
        if "test_enviado" not in st.session_state:
            st.session_state.test_enviado = False

        # ---------- Formulario ----------
        if not st.session_state.test_enviado:
            st.markdown("### Responde cada pregunta:")

            for i, (pregunta, _) in enumerate(PREGUNTAS):
                col1, col2 = st.columns([0.75, 0.25])
                with col1:
                    st.markdown(f"**{i+1}.** {pregunta}")
                with col2:
                    respuesta = st.radio(
                        label=f"p{i}",
                        options=["Sí", "No"],
                        horizontal=True,
                        label_visibility="collapsed",
                        key=f"q_{i}",
                    )
                    st.session_state.test_respuestas[i] = respuesta
                st.write("")   # espacio visual

            st.divider()

            if st.button("Ver mi resultado →", type="primary", use_container_width=True):
                st.session_state.test_enviado = True
                st.rerun()

        # ---------- Resultado ----------
        else:
            self._mostrar_resultado()

            if st.button("🔄 Volver a hacer el test", use_container_width=True):
                st.session_state.test_respuestas = {}
                st.session_state.test_enviado = False
                st.rerun()

    # ------------------------------------------------------------------ #
    def _mostrar_resultado(self):
        st = self.st
        respuestas = st.session_state.test_respuestas

        # Contar "Sí" por categoría
        conteo = {"V": 0, "A": 0, "T": 0}
        for i, (_, categoria) in enumerate(PREGUNTAS):
            if respuestas.get(i) == "Sí":
                conteo[categoria] += 1

        total_por_cat = 5   # 5 preguntas por categoría

        st.markdown("## 📊 Tu resultado")

        # Barras de progreso
        cols = st.columns(3)
        etiquetas = {"V": "Víctima", "A": "Agresor", "T": "Testigo"}
        for col, (cat, etiqueta) in zip(cols, etiquetas.items()):
            pct = int((conteo[cat] / total_por_cat) * 100)
            with col:
                st.metric(etiqueta, f"{pct}%")
                st.progress(pct / 100)

        st.divider()

        # Determinar rol principal (mínimo 2 "Sí" para considerar)
        UMBRAL = 2
        rol = max(conteo, key=conteo.get)

        if conteo[rol] < UMBRAL:
            rol = "N"

        info = RESULTADOS[rol]
        getattr(st, info["color"] if info["color"] in
                ("success", "warning", "error", "info") else "info")(
            f"### {info['titulo']}\n\n{info['mensaje']}"
        )

        # Mostrar tarjeta de color correcta
        color_fn = {
            "violet": st.info,
            "red":    st.error,
            "orange": st.warning,
            "green":  st.success,
        }
        color_fn.get(info["color"], st.info)(
            f"### {info['titulo']}\n\n{info['mensaje']}"
        )

    # ------------------------------------------------------------------ #
    def footer(self):
        self.st.divider()
        self.st.caption(
            "Este test es orientativo, no un diagnóstico clínico. "
            "Ante cualquier situación de riesgo, acude a un adulto de confianza."
        )


Test().render()