import streamlit as st

st.set_page_config(page_title="Simulador AMV", layout="centered")
st.title("🎓 Simulador de Examen AMV - 11 Componentes")
st.write("Responde 5 preguntas del componente seleccionado. Al final obtendrás tu puntaje y la explicación de cada respuesta.")

cuestionario = {
    "Regulación": [
        {"preg": "¿Qué entidad regula el mercado de valores en Colombia?", "opciones": ["Banco de la República", "Superfinanciera", "Ministerio de Hacienda", "DIAN"], "respuesta": "Superfinanciera", "explicacion": "La Superfinanciera regula y supervisa el mercado de valores colombiano."},
        {"preg": "¿Qué tipo de valores se negocian en el mercado público colombiano?", "opciones": ["Solo acciones", "Bonos y derivados", "Varios: acciones, bonos, etc.", "Solo TES"], "respuesta": "Varios: acciones, bonos, etc.", "explicacion": "El mercado público permite negociar distintos instrumentos como acciones, bonos, TES, entre otros."},
        {"preg": "¿Cuál es el objetivo del RNVE?", "opciones": ["Registrar fondos", "Registrar emisores y valores", "Registrar bancos", "Registrar clientes"], "respuesta": "Registrar emisores y valores", "explicacion": "El RNVE centraliza información relevante sobre emisores y los valores que colocan."},
        {"preg": "¿Qué operación es del mercado secundario?", "opciones": ["Emisión de bonos", "OPA inicial", "Compra-venta entre inversionistas", "Emisión TES"], "respuesta": "Compra-venta entre inversionistas", "explicacion": "En el mercado secundario se transan valores ya emitidos entre inversionistas."},
        {"preg": "¿Quién puede ser intermediario de valores?", "opciones": ["Cualquiera", "Solo bancos", "Entidades autorizadas por la Superfinanciera", "Personas naturales"], "respuesta": "Entidades autorizadas por la Superfinanciera", "explicacion": "Solo las entidades autorizadas pueden ejercer la intermediación de valores legalmente."}
    ],
    "Autorregulación": [
        {"preg": "¿Qué es la autorregulación?", "opciones": ["Obligación legal", "Mecanismo voluntario que complementa la regulación estatal", "Intervención estatal", "Impuesto al mercado"], "respuesta": "Mecanismo voluntario que complementa la regulación estatal", "explicacion": "Es un sistema en el cual los actores del mercado establecen normas adicionales a las oficiales para garantizar mejores prácticas."},
        {"preg": "¿Quién supervisa a los autorreguladores?", "opciones": ["La DIAN", "Superfinanciera", "La bolsa", "Los clientes"], "respuesta": "Superfinanciera", "explicacion": "Aunque la autorregulación es independiente, está sujeta a supervisión por la Superintendencia Financiera."},
        {"preg": "¿Qué función tiene un código de conducta?", "opciones": ["Norma jurídica", "Guía ética profesional", "Ley tributaria", "Manual de usuario"], "respuesta": "Guía ética profesional", "explicacion": "Un código de conducta establece principios y lineamientos éticos para los actores del mercado."},
        {"preg": "¿Qué promueve la autorregulación?", "opciones": ["Menos supervisión", "Mayor transparencia y confianza", "Menos regulación", "Exención tributaria"], "respuesta": "Mayor transparencia y confianza", "explicacion": "Uno de los principales objetivos de la autorregulación es mejorar la transparencia y la confianza del mercado."},
        {"preg": "¿Cuál es una entidad autorreguladora en Colombia?", "opciones": ["DIAN", "Banco de la República", "AMV", "MinHacienda"], "respuesta": "AMV", "explicacion": "La Autorreguladora del Mercado de Valores (AMV) es una entidad autorreguladora reconocida en Colombia."}
    ],
    "Ética e Integridad": [
        {"preg": "¿Qué es la ética profesional?", "opciones": ["Conjunto de leyes", "Reglas del empleador", "Principios que guían la conducta", "Normas de seguridad"], "respuesta": "Principios que guían la conducta", "explicacion": "La ética profesional se refiere a los principios morales que guían el comportamiento correcto en el ejercicio de una profesión."},
        {"preg": "¿Qué actitud debe tener un asesor financiero frente al conflicto de interés?", "opciones": ["Ocultarlo", "Rechazarlo y comunicarlo", "Aprovecharlo", "Negociarlo con el cliente"], "respuesta": "Rechazarlo y comunicarlo", "explicacion": "El asesor debe evitar y reportar cualquier conflicto de interés para proteger al cliente."},
        {"preg": "¿Qué conducta es contraria a la ética del mercado?", "opciones": ["Asesoría imparcial", "Uso de información privilegiada", "Divulgación de riesgos", "Cumplimiento normativo"], "respuesta": "Uso de información privilegiada", "explicacion": "Utilizar información privilegiada para obtener beneficios personales es antiético y sancionable."},
        {"preg": "¿Qué debe promover un asesor financiero ético?", "opciones": ["Mayor rentabilidad personal", "Confianza y transparencia", "Productos de su empresa", "Cierre de ventas"], "respuesta": "Confianza y transparencia", "explicacion": "La transparencia genera confianza y fortalece la relación con el cliente."},
        {"preg": "¿Qué debe hacer un asesor si no conoce un producto?", "opciones": ["Promoverlo igual", "Evitar hablar del tema", "Estudiarlo o referirlo", "Inventar una respuesta"], "respuesta": "Estudiarlo o referirlo", "explicacion": "Un asesor ético debe estar capacitado para asesorar o derivar al cliente a un experto."}
    ],
    "Análisis Económico": [
        {"preg": "¿Qué representa un aumento del PIB?", "opciones": ["Desaceleración", "Mayor producción de bienes y servicios", "Mayor inflación", "Caída del empleo"], "respuesta": "Mayor producción de bienes y servicios", "explicacion": "El PIB mide el total de bienes y servicios producidos, por lo que si sube, la economía crece."},
        {"preg": "¿Qué entidad calcula el IPC en Colombia?", "opciones": ["Banco de la República", "DANE", "Superfinanciera", "Ministerio de Hacienda"], "respuesta": "DANE", "explicacion": "El DANE es el encargado oficial de calcular el IPC."},
        {"preg": "¿Cuál es el efecto de una política monetaria expansiva?", "opciones": ["Sube tasas", "Reduce tasas", "Cierra mercados", "Aumenta déficit"], "respuesta": "Reduce tasas", "explicacion": "Busca estimular la economía al hacer el crédito más barato."},
        {"preg": "¿Qué mide el IPC?", "opciones": ["Riesgo país", "Inflación", "Tipo de cambio", "Desempleo"], "respuesta": "Inflación", "explicacion": "El IPC mide cómo cambian los precios de una canasta básica de bienes y servicios."},
        {"preg":"¿Qué es déficit fiscal?","opciones":["Más ingresos que gastos","Más gastos que ingresos","Superávit","Reducir impuestos"],"respuesta":"Más gastos que ingresos","explicacion":"Significa que el Estado gasta más de lo que recauda."}
    ],
    "Riesgos": [
        {"preg": "¿Qué riesgo representa una subida inesperada en tasas de interés?", "opciones": ["Crédito", "Mercado", "Operativo", "Reputacional"], "respuesta": "Mercado", "explicacion": "Este tipo de riesgo surge por cambios en tasas, precios o divisas."},
        {"preg": "¿Qué es riesgo de crédito?", "opciones": ["Error operativo", "Impago del cliente", "Variación de precios", "Problema legal"], "respuesta": "Impago del cliente", "explicacion": "Es el riesgo de que el deudor no cumpla con sus obligaciones."},
        {"preg": "¿Cómo reducir riesgo mediante diversificación?", "opciones": ["Concentrar inversiones", "Repositorio", "Portafolio diversificado", "Apalancarse"], "respuesta": "Portafolio diversificado", "explicacion": "Diversificar reduce la exposición a la falla de un solo activo."},
        {"preg": "¿Qué es riesgo operativo?", "opciones": ["Impago", "Hackeo", "Fraude o errores internos", "Cambio de tasas"], "respuesta": "Fraude o errores internos", "explicacion": "Incluye fallas tecnológicas, humanos o procesos internos."},
        {"preg": "¿Qué riesgo daña la imagen institucional?", "opciones": ["Mercado", "Liquidez", "Reputacional", "Legal"], "respuesta": "Reputacional", "explicacion": "Afecta cómo el público y clientes perciben a la entidad."}
    ]
}

componente = st.selectbox("📘 Elige un componente:", list(cuestionario.keys()))

if "preguntas_mostradas" not in st.session_state or st.session_state["componente_activo"] != componente:
    st.session_state["preguntas_mostradas"] = cuestionario[componente][:5]
    st.session_state["componente_activo"] = componente

preguntas = st.session_state["preguntas_mostradas"]
respuestas_usuario = []

st.write("---")
for i, pregunta in enumerate(preguntas):
    st.subheader(f"Pregunta {i+1}")
    st.write(pregunta["preg"])
    respuestas_usuario.append(st.radio("Opciones:", pregunta["opciones"], key=f"{componente}_{i}"))

st.write("---")
if st.button("📊 Ver resultados"):
    aciertos = sum(1 for i, pregunta in enumerate(preguntas) if respuestas_usuario[i] == pregunta["respuesta"])
    st.success(f"Obtuviste {aciertos}/5 respuestas correctas. Puntaje: {(aciertos/5)*100:.0f}%")
    st.write("### 🧠 Explicaciones:")
    for i, pregunta in enumerate(preguntas):
        st.markdown(f"**{i+1}. {pregunta['preg']}**")
        st.markdown(f"- ✅ Respuesta correcta: {pregunta['respuesta']}")
        st.markdown(f"- 📘 Explicación: {pregunta['explicacion']}")
        st.write("")

