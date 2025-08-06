import streamlit as st

st.title("🎓 Simulador de Examen AMV - 11 Componentes")
st.write("Responde 5 preguntas del componente seleccionado. Al final obtendrás tu puntaje y la explicación de cada respuesta.")

cuestionario = {
    "Regulación": [ # ← Aquí empiezan los componentes con sus preguntas
        {"preg": "¿Qué entidad regula el mercado de valores en Colombia?", "opciones": ["Banco de la República", "Superfinanciera", "Ministerio de Hacienda", "DIAN"], "respuesta": "Superfinanciera", "explicacion": "La Superfinanciera regula y supervisa el mercado de valores colombiano."},
        ...
    ],
    "Autorregulación": [...],
    "Ética e Integridad": [...],
    "Análisis Económico": [...],
    "Riesgos": [...],
    "Matemáticas Financieras": [...],
    "Renta Fija": [...],
    "Renta Variable": [...],
    "Derivados": [...],
    "Fondos de Pensiones": [...],
    "Fondos de Inversión Colectiva": [...]
}

# ✅ AQUÍ ESTÁ EL CAMBIO IMPORTANTE
componente = st.selectbox("📘 Elige un componente:", list(cuestionario.keys()))
preguntas = cuestionario[componente][:5]  # ← Esta línea mantiene las preguntas fijas
respuestas_usuario = []

st.write("---")
for i, pregunta in enumerate(preguntas):
    st.subheader(f"Pregunta {i+1}")
    st.write(pregunta["preg"])
    respuesta = st.radio("Opciones:", pregunta["opciones"], key=f"{componente}_{i}")
    respuestas_usuario.append(respuesta)

st.write("---")
if st.button("📊 Ver resultados"):
    aciertos = 0
    for i, pregunta in enumerate(preguntas):
        if respuestas_usuario[i] == pregunta["respuesta"]:
            aciertos += 1
    st.success(f"Obtuviste {aciertos}/5 respuestas correctas. Puntaje: {(aciertos/5)*100:.0f}%")
    st.write("### 🧠 Explicaciones:")
    for i, pregunta in enumerate(preguntas):
        st.markdown(f"**{i+1}. {pregunta['preg']}**")
        st.markdown(f"- ✅ Respuesta correcta: {pregunta['respuesta']}")
        st.markdown(f"- 📘 Explicación: {pregunta['explicacion']}")
        st.write("")
