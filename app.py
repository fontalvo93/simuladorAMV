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
    ],
    "Matemáticas Financieras": [
    {"preg": "¿Qué representa la tasa de interés?", "opciones": ["Costo del dinero en el tiempo", "Costo del producto", "Costo del impuesto", "Valor presente neto"], "respuesta": "Costo del dinero en el tiempo", "explicacion": "La tasa de interés mide cuánto se paga o gana por usar dinero en un periodo."},
    {"preg": "¿Qué es el valor presente?", "opciones": ["Valor que tendrá en el futuro", "Valor actual de un flujo futuro", "Valor acumulado con interés", "Costo del activo"], "respuesta": "Valor actual de un flujo futuro", "explicacion": "El valor presente permite conocer cuánto vale hoy un dinero que se recibirá después."},
    {"preg": "¿Qué es un interés compuesto?", "opciones": ["Interés sobre capital inicial", "Interés sobre interés generado", "Interés sobre cuota fija", "Sin capitalización"], "respuesta": "Interés sobre interés generado", "explicacion": "El interés compuesto acumula intereses generados en periodos anteriores."},
    {"preg": "¿Cuál fórmula se usa para valor futuro con interés compuesto?", "opciones": ["VF = VP(1+it)", "VF = VP(1+i)^n", "VP = VF/(1+i)", "VF = i/n"], "respuesta": "VF = VP(1+i)^n", "explicacion": "Esa es la fórmula clásica del valor futuro compuesto."},
    {"preg": "¿Qué ocurre si la tasa nominal es 12% y capitaliza mensualmente?", "opciones": ["Tasa efectiva anual es 12%", "Tasa efectiva anual es mayor", "Tasa baja", "No cambia nada"], "respuesta": "Tasa efectiva anual es mayor", "explicacion": "La capitalización aumenta el valor efectivo de la tasa nominal."}
],
    "Renta Fija": [
    {"preg": "¿Qué es un bono?", "opciones": ["Acción de empresa", "Derecho a voto", "Instrumento de deuda", "Título sin valor"], "respuesta": "Instrumento de deuda", "explicacion": "Es un título que representa una deuda que será pagada en el futuro con intereses."},
    {"preg": "¿Qué es la tasa cupón?", "opciones": ["Rentabilidad anual de una acción", "Pago periódico del bono", "Costo del bono", "Valor residual"], "respuesta": "Pago periódico del bono", "explicacion": "La tasa cupón es el interés que paga un bono periódicamente."},
    {"preg": "¿Qué afecta el precio de un bono en el mercado secundario?", "opciones": ["Tasa de inflación", "Tasa de mercado", "PIB", "Emisión de acciones"], "respuesta": "Tasa de mercado", "explicacion": "Si sube la tasa del mercado, el precio del bono suele bajar, y viceversa."},
    {"preg": "¿Qué es la duración de un bono?", "opciones": ["Vida útil", "Tiempo hasta el pago de cupón", "Promedio ponderado del plazo de los flujos", "Tasa fija"], "respuesta": "Promedio ponderado del plazo de los flujos", "explicacion": "La duración mide la sensibilidad del precio del bono ante cambios en tasas."},
    {"preg": "¿Qué riesgo tiene la renta fija?", "opciones": ["Ninguno", "Riesgo de crédito y tasa de interés", "Solo riesgo de mercado", "Riesgo operacional"], "respuesta": "Riesgo de crédito y tasa de interés", "explicacion": "Existe riesgo de impago y de que las tasas afecten el precio del bono."}
],
    "Renta Variable": [
    {"preg": "¿Qué instrumento representa la renta variable?", "opciones": ["Bono", "Acción", "CDT", "TES"], "respuesta": "Acción", "explicacion": "Las acciones no tienen una rentabilidad fija, por eso son renta variable."},
    {"preg": "¿Qué derecho otorgan las acciones ordinarias?", "opciones": ["Pago fijo", "Participar en utilidades y voto", "Redención garantizada", "Tasa de interés fija"], "respuesta": "Participar en utilidades y voto", "explicacion": "El accionista tiene derecho a recibir dividendos y a votar en asambleas."},
    {"preg": "¿Qué es el dividendo?", "opciones": ["Interés por deuda", "Ganancia de capital", "Distribución de utilidades", "Precio de venta"], "respuesta": "Distribución de utilidades", "explicacion": "Es el pago que hace la empresa a los accionistas con sus utilidades."},
    {"preg": "¿Qué riesgo predomina en renta variable?", "opciones": ["Riesgo tasa", "Riesgo mercado", "Riesgo operativo", "Riesgo legal"], "respuesta": "Riesgo mercado", "explicacion": "Las acciones fluctúan mucho por cambios de mercado, confianza, noticias, etc."},
    {"preg": "¿Qué es la valorización de una acción?", "opciones": ["Caída en el precio", "Pago de intereses", "Aumento en su precio de mercado", "Reducción de tasa"], "respuesta": "Aumento en su precio de mercado", "explicacion": "Valorización significa que la acción vale más que cuando se compró."}
],
    "Derivados": [
    {"preg": "¿Qué es un derivado financiero?", "opciones": ["Título de deuda", "Acción preferencial", "Instrumento cuyo valor depende de otro", "Crédito bancario"], "respuesta": "Instrumento cuyo valor depende de otro", "explicacion": "Su valor deriva del precio de otro activo (subyacente)."},
    {"preg": "¿Cuál es un tipo de derivado?", "opciones": ["Bonos", "Forward", "Certificado de depósito", "TES"], "respuesta": "Forward", "explicacion": "Los Forward son contratos que fijan precio futuro de compra/venta."},
    {"preg": "¿Para qué se usan los derivados?", "opciones": ["Evadir impuestos", "Asegurar precios o especular", "Reducir liquidez", "Comprar bonos"], "respuesta": "Asegurar precios o especular", "explicacion": "Pueden ser usados para cubrir riesgos o buscar rentabilidad."},
    {"preg": "¿Qué riesgo manejan los derivados?", "opciones": ["Riesgo climático", "Riesgo operacional", "Riesgo de contraparte y mercado", "Riesgo logístico"], "respuesta": "Riesgo de contraparte y mercado", "explicacion": "Puede que la contraparte no cumpla o el mercado varíe."},
    {"preg": "¿Cuál es un mercado donde se negocian derivados en Colombia?", "opciones": ["Bolsa Nacional de Derivados", "BVC (Bolsa de Valores de Colombia)", "SIC", "RNVE"], "respuesta": "BVC (Bolsa de Valores de Colombia)", "explicacion": "La BVC tiene un sistema de negociación de derivados estandarizados."}
],
    "Fondos de Pensiones": [
    {"preg": "¿Qué función tienen los fondos de pensiones?", "opciones": ["Financiar EPS", "Administrar ahorro para retiro", "Pagar impuestos", "Intermediar valores"], "respuesta": "Administrar ahorro para retiro", "explicacion": "Su propósito principal es garantizar un ingreso al momento del retiro laboral."},
    {"preg": "¿Qué régimen existe en Colombia?", "opciones": ["Solidario", "Privado", "Público y privado", "Gratuito"], "respuesta": "Público y privado", "explicacion": "Colombia tiene régimen público (Colpensiones) y privado (fondos AFP)."},
    {"preg": "¿Qué es la doble asesoría?", "opciones": ["Dos pensiones", "Asesoría para migrar entre regímenes", "Asesoría del empleador", "Dos asesores del mismo fondo"], "respuesta": "Asesoría para migrar entre regímenes", "explicacion": "Se debe dar asesoría completa si alguien quiere cambiar entre fondo privado y público."},
    {"preg": "¿Cuál es un objetivo del multifondos?", "opciones": ["Unificar rentabilidad", "Ofrecer diferentes perfiles de riesgo", "Eliminar aportes", "Limitar retiros"], "respuesta": "Ofrecer diferentes perfiles de riesgo", "explicacion": "Permite al afiliado elegir el fondo según su edad y tolerancia al riesgo."},
    {"preg": "¿Qué entidad pública administra el fondo pensional?", "opciones": ["Bancolombia", "Superfinanciera", "Colpensiones", "MinHacienda"], "respuesta": "Colpensiones", "explicacion": "Colpensiones es el administrador público del sistema pensional colombiano."}
],
    "Fondos de Inversión Colectiva": [
    {"preg": "¿Qué es un FIC?", "opciones": ["Cuenta de ahorros", "Portafolio colectivo administrado", "Acción preferente", "Bonos garantizados"], "respuesta": "Portafolio colectivo administrado", "explicacion": "Son vehículos de inversión donde varios inversionistas aportan recursos gestionados profesionalmente."},
    {"preg": "¿Quién administra los FIC?", "opciones": ["Superfinanciera", "Administradoras autorizadas", "Empresas", "Usuarios"], "respuesta": "Administradoras autorizadas", "explicacion": "Deben ser administradoras vigiladas por la Superfinanciera."},
    {"preg": "¿Qué documento describe el FIC?", "opciones": ["Pagaré", "Reglamento del fondo", "Factura", "Acta de constitución"], "respuesta": "Reglamento del fondo", "explicacion": "Allí se especifica el tipo de inversiones, riesgos, comisiones, etc."},
    {"preg": "¿Qué ventaja tiene un FIC?", "opciones": ["Menor control", "Inversión especulativa", "Diversificación y administración profesional", "Riesgo ilimitado"], "respuesta": "Diversificación y administración profesional", "explicacion": "El inversionista accede a una cartera gestionada por expertos y con bajo riesgo individual."},
    {"preg": "¿Qué tipo de FIC puede existir?", "opciones": ["Solo renta fija", "Renta fija y variable", "Solo acciones", "Crédito corporativo"], "respuesta": "Renta fija y variable", "explicacion": "Pueden invertir en distintos tipos de activos dependiendo del objetivo del fondo."}
],






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


