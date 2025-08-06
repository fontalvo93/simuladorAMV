import streamlit as st
import random

st.title("🎓 Simulador de Examen AMV - 11 Componentes")
st.write("Responde 5 preguntas del componente seleccionado. Al final obtendrás tu puntaje y la explicación de cada respuesta.")

cuestionario = {
    "Regulación": [
        {"preg": "¿Qué entidad regula el mercado de valores en Colombia?", "opciones": ["Banco de la República", "Superfinanciera", "Ministerio de Hacienda", "DIAN"], "respuesta": "Superfinanciera", "explicacion": "La Superfinanciera regula y supervisa el mercado de valores colombiano."},
        {"preg": "¿Qué tipo de valores se negocian en el mercado público colombiano?", "opciones": ["Solo acciones", "Bonos y derivados", "Varios: acciones, bonos, etc.", "Solo TES"], "respuesta": "Varios: acciones, bonos, etc.", "explicacion": "El mercado público permite negociar distintos instrumentos como acciones, bonos, TES, entre otros."},
        {"preg": "¿Cuál es el objetivo del RNVE?", "opciones": ["Registrar fondos", "Registrar emisores y valores", "Registrar bancos", "Registrar clientes"], "respuesta": "Registrar emisores y valores", "explicacion": "El RNVE centraliza información relevante sobre emisores y los valores que colocan."},
        {"preg": "¿Qué operación es del mercado secundario?", "opciones": ["Emisión de bonos", "OPA inicial", "Compra-venta entre inversionistas", "Emisión TES"], "respuesta": "Compra-venta entre inversionistas", "explicacion": "En el mercado secundario se transan valores ya emitidos entre inversionistas."},
        {"preg": "¿Quién puede ser intermediario de valores?", "opciones": ["Cualquiera", "Solo bancos", "Entidades autorizadas por la Superfinanciera", "Personas naturales"], "respuesta": "Entidades autorizadas por la Superfinanciera", "explicacion": "Solo las entidades autorizadas pueden ejercer la intermediación de valores legalmente."},
    ],
    "Autorregulación": [
        {"preg": "¿Qué significa la autorregulación en el mercado de valores?", "opciones": ["Control total del Estado", "Normas internas voluntarias", "Control por entidades autorizadas para asegurar transparencia", "Libre regulación"], "respuesta": "Control por entidades autorizadas para asegurar transparencia", "explicacion": "La autorregulación fortalece el control del mercado mediante normas adicionales a las legales, aplicadas por entidades autorizadas."},
        {"preg": "¿Cuál es la función del AMV?", "opciones": ["Emitir TES", "Supervisar la política monetaria", "Ejercer la autorregulación", "Otorgar créditos"], "respuesta": "Ejercer la autorregulación", "explicacion": "AMV es la entidad autorizada para autorregular el mercado de valores colombiano."},
        {"preg": "¿Qué ocurre si se incumplen normas de autorregulación?", "opciones": ["Nada", "Solo advertencia", "Sanciones del autorregulador", "Sanciones por la DIAN"], "respuesta": "Sanciones del autorregulador", "explicacion": "Las normas de autorregulación son obligatorias y su incumplimiento puede generar sanciones."},
        {"preg": "¿Quiénes deben cumplir las normas del AMV?", "opciones": ["Solo empleados", "Solo entidades públicas", "Todos los inscritos", "Solo directivos"], "respuesta": "Todos los inscritos", "explicacion": "Toda persona natural o jurídica registrada en AMV debe cumplir sus normas."},
        {"preg": "¿Cuál es un objetivo clave de la autorregulación?", "opciones": ["Reemplazar la ley", "Aumentar ganancias", "Proteger la integridad del mercado", "Evitar impuestos"], "respuesta": "Proteger la integridad del mercado", "explicacion": "La autorregulación complementa la ley para proteger a los inversionistas y al mercado."},
    ],
    "Ética e Integridad": [
        {"preg": "¿Qué representa un dilema ético?", "opciones": ["Una ley", "Un problema técnico", "Un conflicto entre opciones morales", "Un error contable"], "respuesta": "Un conflicto entre opciones morales", "explicacion": "Un dilema ético surge cuando se enfrentan dos opciones moralmente válidas."},
        {"preg": "¿Cuál es una conducta ética esencial?", "opciones": ["Buscar comisiones altas", "Actuar con honestidad", "Persuadir al cliente", "Ocultar riesgos"], "respuesta": "Actuar con honestidad", "explicacion": "La honestidad y transparencia son la base de la ética profesional financiera."},
        {"preg": "¿Qué hacer con la información del cliente?", "opciones": ["Venderla", "Compartirla", "Protegerla", "Ignorarla"], "respuesta": "Protegerla", "explicacion": "La protección de datos personales es una obligación ética y legal."},
        {"preg": "¿Qué acción va contra la ética?", "opciones": ["Escuchar al cliente", "Capacitarse", "Ocultar información", "Ofrecer productos adecuados"], "respuesta": "Ocultar información", "explicacion": "Omitir información relevante al cliente vulnera la transparencia."},
        {"preg": "Una práctica ética implica:", "opciones": ["Vender sin explicar", "Buscar solo beneficio personal", "Tomar decisiones justas", "Presionar al cliente"], "respuesta": "Tomar decisiones justas", "explicacion": "Las decisiones justas y responsables reflejan una actuación ética."},
    ],
    "Análisis Económico": [
        {"preg": "¿Qué es el PIB?", "opciones": ["Precio interno bruto", "Producto interno bruto", "Producto internacional bancario", "Pensión individual básica"], "respuesta": "Producto interno bruto", "explicacion": "El PIB es el valor total de los bienes y servicios producidos por una economía durante un periodo."},
        {"preg": "¿Qué indica una inflación alta?", "opciones": ["Reducción de empleo", "Estabilidad económica", "Aumento sostenido de precios", "Caída de exportaciones"], "respuesta": "Aumento sostenido de precios", "explicacion": "La inflación alta implica que los precios en general están subiendo continuamente."},
        {"preg": "¿Qué hace el Banco de la República para controlar la inflación?", "opciones": ["Imprime más dinero", "Sube la tasa de interés", "Reduce el IVA", "Disminuye el dólar"], "respuesta": "Sube la tasa de interés", "explicacion": "Al subir tasas, se desestimula el consumo y se reduce la inflación."},
        {"preg": "¿Qué significa una tasa de interés baja?", "opciones": ["Fomenta el ahorro", "Desestimula inversión", "Estimula consumo e inversión", "Cae el PIB"], "respuesta": "Estimula consumo e inversión", "explicacion": "Las tasas bajas hacen más baratos los créditos, estimulando el gasto y la inversión."},
        {"preg": "¿Qué afecta el tipo de cambio?", "opciones": ["El clima", "Los salarios mínimos", "La oferta y demanda de divisas", "La ley de pensiones"], "respuesta": "La oferta y demanda de divisas", "explicacion": "El valor de una moneda frente a otra depende de la oferta y demanda en el mercado."},
    ],
    "Riesgos": [
        {"preg": "¿Qué es el riesgo de mercado?", "opciones": ["Falta de liquidez", "Pérdida por variaciones en precios", "Fraude interno", "Falta de clientes"], "respuesta": "Pérdida por variaciones en precios", "explicacion": "El riesgo de mercado surge por cambios en tasas de interés, precios de acciones o divisas."},
        {"preg": "¿Qué es el riesgo de crédito?", "opciones": ["Fuga de datos", "Impago de obligaciones", "Cambios políticos", "Variación del dólar"], "respuesta": "Impago de obligaciones", "explicacion": "Es el riesgo de que un deudor no cumpla con el pago acordado."},
        {"preg": "¿Cuál es un ejemplo de riesgo operativo?", "opciones": ["Caída del mercado", "Errores humanos o tecnológicos", "Impago del cliente", "Subida del dólar"], "respuesta": "Errores humanos o tecnológicos", "explicacion": "El riesgo operativo incluye fallos de sistemas, errores humanos o fraudes internos."},
        {"preg": "¿Qué es riesgo legal?", "opciones": ["Fraude de empleados", "Problemas por cambios normativos o contratos", "Impago de bonos", "Hackeo bancario"], "respuesta": "Problemas por cambios normativos o contratos", "explicacion": "Involucra disputas legales, interpretación de contratos o regulación inesperada."},
        {"preg": "¿Qué herramienta se usa para medir riesgo?", "opciones": ["Tasa interna de retorno", "Valor en riesgo (VaR)", "PIB", "ROE"], "respuesta": "Valor en riesgo (VaR)", "explicacion": "El VaR mide la pérdida máxima esperada de una inversión bajo condiciones normales."},
    ],
    "Matemáticas Financieras": [
        {"preg": "Si inviertes $1.000.000 a una tasa del 10% anual durante 2 años, ¿cuánto obtienes al final (interés compuesto)?", "opciones": ["$1.100.000", "$1.200.000", "$1.210.000", "$1.300.000"], "respuesta": "$1.210.000", "explicacion": "Interés compuesto: VF = 1.000.000 x (1 + 0,10)^2 = 1.210.000"},
        {"preg": "¿Qué representa el valor presente?", "opciones": ["Valor actual de un flujo futuro", "Rendimiento de una acción", "Precio de mercado", "Ingreso neto"], "respuesta": "Valor actual de un flujo futuro", "explicacion": "Es cuánto vale hoy un monto que se recibirá en el futuro."},
        {"preg": "¿Qué es una anualidad?", "opciones": ["Un bono", "Pago único", "Serie de pagos iguales en el tiempo", "Tasa efectiva"], "respuesta": "Serie de pagos iguales en el tiempo", "explicacion": "Una anualidad es una secuencia de pagos iguales hechos a intervalos regulares."},
        {"preg": "¿Qué significa una tasa efectiva anual?", "opciones": ["Sin capitalización", "Incluye inflación", "Con capitalización compuesta", "Es menor que la nominal"], "respuesta": "Con capitalización compuesta", "explicacion": "La tasa efectiva incluye la capitalización de intereses durante el año."},
        {"preg": "¿Qué fórmula se usa para valor futuro con interés compuesto?", "opciones": ["VF = VP x (1 + i)^n", "VP = VF x i x n", "VF = VP + i", "VP = VF / (1 + i)^n"], "respuesta": "VF = VP x (1 + i)^n", "explicacion": "Es la fórmula base para calcular el valor futuro con interés compuesto."},
    ],
    "Renta Fija": [
        {"preg": "¿Qué es un bono?", "opciones": ["Acción de una empresa", "Instrumento de deuda", "Fondo de inversión", "Título de propiedad"], "respuesta": "Instrumento de deuda", "explicacion": "El bono representa una obligación de pagar intereses y capital en el futuro."},
        {"preg": "¿Qué es el cupón de un bono?", "opciones": ["El emisor", "El interés que paga", "Su valor nominal", "El precio de venta"], "respuesta": "El interés que paga", "explicacion": "El cupón es el interés periódico pagado al inversionista."},
        {"preg": "¿Qué pasa si suben las tasas de interés?", "opciones": ["Sube el precio del bono", "Baja el precio del bono", "Sube el cupón", "Baja el riesgo"], "respuesta": "Baja el precio del bono", "explicacion": "Existe una relación inversa entre tasas y precios de los bonos."},
        {"preg": "¿Qué es el vencimiento del bono?", "opciones": ["Fecha del cupón", "Plazo para redimir el capital", "Fecha de emisión", "Fecha de pago de dividendo"], "respuesta": "Plazo para redimir el capital", "explicacion": "Es la fecha en que se debe devolver el capital al inversionista."},
        {"preg": "¿Qué es el rendimiento al vencimiento?", "opciones": ["Valor presente neto", "Tasa interna de retorno del bono", "Fluctuación de precios", "Tasa fija del mercado"], "respuesta": "Tasa interna de retorno del bono", "explicacion": "Representa el retorno que el inversionista obtendrá si mantiene el bono hasta vencimiento."},
    ],
    "Renta Variable": [
        {"preg": "¿Qué representa una acción?", "opciones": ["Un préstamo", "Una obligación", "Una parte de propiedad", "Un bono del Estado"], "respuesta": "Una parte de propiedad", "explicacion": "Una acción representa una parte de propiedad en una empresa."},
        {"preg": "¿Qué es un dividendo?", "opciones": ["Interés de un bono", "Pago periódico a los socios", "Precio de una acción", "Un descuento"], "respuesta": "Pago periódico a los socios", "explicacion": "Los dividendos son pagos de utilidades a los accionistas."},
        {"preg": "¿Qué es el mercado primario de acciones?", "opciones": ["Compra-venta entre inversionistas", "Emisión inicial de acciones", "Mercado de derivados", "Intercambio de bonos"], "respuesta": "Emisión inicial de acciones", "explicacion": "Es donde se emiten por primera vez las acciones para conseguir recursos."},
        {"preg": "¿Qué es el mercado secundario?", "opciones": ["Oferta pública inicial", "Mercado donde se negocian acciones ya emitidas", "Mercado de deuda", "Bolsa internacional"], "respuesta": "Mercado donde se negocian acciones ya emitidas", "explicacion": "En el mercado secundario se negocian acciones entre inversionistas."},
        {"preg": "¿Qué es la valorización de una acción?", "opciones": ["Aumento en su precio", "Pago del dividendo", "Interés compuesto", "Pérdida del capital"], "respuesta": "Aumento en su precio", "explicacion": "La valorización ocurre cuando el precio de la acción sube respecto al momento de compra."},
    ],
    "Derivados": [
        {"preg": "¿Qué es un derivado financiero?", "opciones": ["Un bono", "Un tipo de acción", "Contrato cuyo valor depende de otro activo", "Fondo mutuo"], "respuesta": "Contrato cuyo valor depende de otro activo", "explicacion": "Un derivado toma su valor de un activo subyacente como una acción, bono o divisa."},
        {"preg": "¿Qué tipo de derivado es un forward?", "opciones": ["Contrato estandarizado en bolsa", "Contrato a futuro OTC", "Acción preferencial", "Obligación convertida"], "respuesta": "Contrato a futuro OTC", "explicacion": "El forward es un contrato privado negociado fuera de bolsa para comprar o vender un activo en el futuro."},
        {"preg": "¿Qué es una opción financiera?", "opciones": ["Un bono con derecho a voto", "Contrato que da el derecho pero no la obligación de comprar o vender", "Una acción común", "Fondo indexado"], "respuesta": "Contrato que da el derecho pero no la obligación de comprar o vender", "explicacion": "Las opciones otorgan derechos, no obligaciones, sobre activos."},
        {"preg": "¿Cuál es un riesgo de los derivados?", "opciones": ["Pérdida del dividendo", "Mayor liquidez", "Alto apalancamiento", "Interés fijo"], "respuesta": "Alto apalancamiento", "explicacion": "El uso de apalancamiento puede aumentar las ganancias, pero también las pérdidas."},
        {"preg": "¿Qué función tienen los derivados?", "opciones": ["Pagar dividendos", "Cubrir riesgos", "Generar inflación", "Emitir bonos"], "respuesta": "Cubrir riesgos", "explicacion": "Los derivados permiten gestionar el riesgo de mercado mediante cobertura (hedging)."},
    ],
    "Fondos de Pensiones": [
        {"preg": "¿Qué es un fondo de pensiones obligatorias?", "opciones": ["Ahorro voluntario", "Seguro de vida", "Sistema de ahorro para la jubilación", "Préstamo a largo plazo"], "respuesta": "Sistema de ahorro para la jubilación", "explicacion": "Son mecanismos obligatorios de ahorro para la vejez bajo el sistema pensional colombiano."},
        {"preg": "¿Quién regula los fondos de pensiones?", "opciones": ["Ministerio de Salud", "DIAN", "Superfinanciera", "Bancolombia"], "respuesta": "Superfinanciera", "explicacion": "La Superfinanciera supervisa a las administradoras de fondos de pensiones en Colombia."},
        {"preg": "¿Qué es multifondos en pensiones?", "opciones": ["Un único fondo con múltiples usos", "Múltiples fondos con distintos perfiles de riesgo", "Fondo sin riesgo", "Fondo para niños"], "respuesta": "Múltiples fondos con distintos perfiles de riesgo", "explicacion": "Permite asignar los aportes según el perfil de riesgo del afiliado y su edad."},
        {"preg": "¿Qué fondo pensional tiene mayor riesgo?", "opciones": ["Fondo conservador", "Fondo moderado", "Fondo de retiro programado", "Fondo de mayor riesgo"], "respuesta": "Fondo de mayor riesgo", "explicacion": "Este fondo invierte en activos más volátiles y busca mayor rentabilidad."},
        {"preg": "¿Quién administra los aportes pensionales?", "opciones": ["El empleador", "El afiliado", "La AFP", "La Superintendencia"], "respuesta": "La AFP", "explicacion": "Las Administradoras de Fondos de Pensiones gestionan los recursos obligatorios y voluntarios del sistema."},
    ],
    "Fondos de Inversión Colectiva": [
        {"preg": "¿Qué es un FIC?", "opciones": ["Crédito bancario", "Fondo que reúne aportes de varios inversionistas", "Seguro financiero", "Inversión estatal"], "respuesta": "Fondo que reúne aportes de varios inversionistas", "explicacion": "Un FIC agrupa recursos de muchas personas para invertirlos colectivamente."},
        {"preg": "¿Quién administra un FIC?", "opciones": ["Superintendencia", "El Banco Central", "Sociedad administradora autorizada", "Inversionista líder"], "respuesta": "Sociedad administradora autorizada", "explicacion": "Una entidad autorizada por la Superfinanciera gestiona profesionalmente los recursos del fondo."},
        {"preg": "¿Cuál es una ventaja del FIC?", "opciones": ["Alta concentración", "Bajo riesgo siempre", "Diversificación y acceso profesional", "Garantía de rentabilidad"], "respuesta": "Diversificación y acceso profesional", "explicacion": "Los FIC permiten diversificar riesgos y contar con expertos que administran el portafolio."},
        {"preg": "¿Qué documento describe los objetivos y condiciones de un FIC?", "opciones": ["Manual del cliente", "Prospecto de inversión", "Factura", "Acta de asamblea"], "respuesta": "Prospecto de inversión", "explicacion": "El prospecto explica las políticas, comisiones y riesgos del fondo."},
        {"preg": "¿Qué son las unidades de participación?", "opciones": ["Tipo de acción", "Instrumento de deuda", "Fracción del valor del fondo que posee un inversionista", "Cuota de crédito"], "respuesta": "Fracción del valor del fondo que posee un inversionista", "explicacion": "Representan la porción que cada inversionista tiene del total del FIC."},
    ]
}

componente = st.selectbox("📘 Elige un componente:", list(cuestionario.keys()))
preguntas = random.sample(cuestionario[componente], 5)
respuestas_usuario = []

st.write("---")
for i, pregunta in enumerate(preguntas):
    st.subheader(f"Pregunta {i+1}")
    st.write(pregunta["preg"])
    respuesta = st.radio("Opciones:", pregunta["opciones"], key=f"preg_{i}")
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
