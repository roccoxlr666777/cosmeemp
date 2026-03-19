import streamlit as st
import pandas as pd

# ==========================================
# CONFIGURACIÓN Y ESTILOS UDAL
# ==========================================
st.set_page_config(page_title="Simulador: Empresa Estética", page_icon="🏢", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #f4f6f9; }
    h1, h2, h3 { color: #002b5e !important; font-family: 'Helvetica Neue', sans-serif; }
    .stButton>button { background-color: #f2a900; color: #ffffff; font-weight: bold; border-radius: 8px; border: none; }
    .stButton>button:hover { background-color: #d19200; color: white; }
    .header-box { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; }
    .card-foda { padding: 15px; border-radius: 8px; color: white; margin-bottom: 10px; }
    .bg-fortaleza { background-color: #27ae60; }
    .bg-debilidad { background-color: #e74c3c; }
    .bg-oportunidad { background-color: #2980b9; }
    .bg-amenaza { background-color: #8e44ad; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# PANTALLA DE ACCESO
# ==========================================
if 'acceso_empresa' not in st.session_state: st.session_state.acceso_empresa = False

if not st.session_state.acceso_empresa:
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div style='background-color: white; padding: 30px; border-radius: 15px; text-align: center;'><h2 style='color: #002b5e;'>Laboratorio de Negocios</h2><p>Creación de Empresa Estética</p></div>", unsafe_allow_html=True)
        pwd = st.text_input("Ingresa la clave del simulador:", type="password")
        if st.button("Ingresar al Simulador", use_container_width=True):
            if pwd == "Emprendedor2026":
                st.session_state.acceso_empresa = True
                st.rerun()
            else: st.error("Contraseña incorrecta.")
    st.stop()

# ==========================================
# INTERFAZ PRINCIPAL
# ==========================================
st.markdown("""
<div class='header-box'>
    <h1 style='margin: 0; font-size: 2.2rem;'>Simulador Empresarial Estético</h1>
    <p style='margin: 0; font-size: 1.1rem; color: #555;'>De la idea a la estructura operativa.</p>
</div>
""", unsafe_allow_html=True)

tab_plan, tab_finanzas, tab_org = st.tabs(["🎯 1. Planeación Estratégica", "💰 2. Costeo y Las 4 P's", "🏢 3. Organización y Estructura"])

# --- ETAPA 1: PLANEACIÓN ---
with tab_plan:
    st.markdown("### Identidad Corporativa")
    colA, colB = st.columns(2)
    with colA:
        nombre_empresa = st.text_input("Nombre de la Clínica / Marca Cosmética:")
        mision = st.text_area("Misión (¿Qué hacemos hoy?):", placeholder="Ej. Brindar tratamientos dermatológicos...")
    with colB:
        vision = st.text_area("Visión (¿Dónde estaremos en 5 años?):", placeholder="Ej. Ser la clínica líder en Puebla...")
        valores = st.text_input("Valores Principales:")

    st.markdown("---")
    st.markdown("### Análisis FODA")
    st.write("Identifica los factores internos y externos antes de lanzar el producto/servicio.")
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.markdown("<div class='card-foda bg-fortaleza'><b>Fortalezas (Interno)</b></div>", unsafe_allow_html=True)
        st.text_area("¿Qué ventajas competitivas o patentes tienes?", key="fort")
        st.markdown("<div class='card-foda bg-oportunidad'><b>Oportunidades (Externo)</b></div>", unsafe_allow_html=True)
        st.text_area("¿Qué tendencias del mercado (ej. cosmética vegana) puedes aprovechar?", key="opor")
    with col_f2:
        st.markdown("<div class='card-foda bg-debilidad'><b>Debilidades (Interno)</b></div>", unsafe_allow_html=True)
        st.text_area("¿Qué te falta? (ej. falta de capital, personal sin capacitar)", key="deb")
        st.markdown("<div class='card-foda bg-amenaza'><b>Amenazas (Externo)</b></div>", unsafe_allow_html=True)
        st.text_area("Nuevas leyes de COFEPRIS, competencia agresiva, inflación.", key="amen")

# --- ETAPA 2: FINANZAS Y MARKETING ---
with tab_finanzas:
    st.markdown("### Mix de Marketing (Las 4 P's)")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.text_area("📦 Producto", "Línea facial anti-edad con ácido hialurónico.")
    with c2: st.text_area("💵 Precio", "Estrategia de penetración: $450 MXN por unidad.")
    with c3: st.text_area("📍 Plaza", "Venta directa en clínica y e-commerce.")
    with c4: st.text_area("📣 Promoción", "Campañas en Meta Ads y PR con influencers locales.")

    st.markdown("---")
    st.markdown("### Simulador de Costeo y Punto de Equilibrio")
    st.info("¿Cuántos servicios/productos debes vender solo para no perder dinero?")
    
    col_costos1, col_costos2 = st.columns(2)
    with col_costos1:
        st.write("**Costos Fijos Mensuales (CF)**")
        renta = st.number_input("Renta del local ($):", value=15000)
        sueldos = st.number_input("Nómina base ($):", value=20000)
        servicios = st.number_input("Servicios e Internet ($):", value=3000)
        cf_total = renta + sueldos + servicios
        st.error(f"Total Costos Fijos: ${cf_total:,.2f}")
        
    with col_costos2:
        st.write("**Costos Variables por Unidad (CV)**")
        insumos = st.number_input("Insumos/Producto ($):", value=100)
        comision = st.number_input("Comisión de venta ($):", value=50)
        cv_total = insumos + comision
        precio_venta = st.number_input("Precio de Venta al Público ($):", value=500)
        
    if precio_venta > cv_total:
        punto_eq = cf_total / (precio_venta - cv_total)
        st.success(f"⚖️ **Punto de Equilibrio:** Necesitas vender **{int(punto_eq) + 1} unidades/servicios** al mes para no quebrar.")
    else:
        st.warning("⚠️ Tu costo variable es mayor al precio de venta. Estás perdiendo dinero en cada venta.")

# --- ETAPA 3: ORGANIZACIÓN (EL NUEVO TEMA) ---
with tab_org:
    st.markdown("### Estructura Organizacional y Jerárquica")
    st.write("Pasar del emprendedor 'todólogo' a una empresa estructurada requiere definir quién rinde cuentas a quién y qué hace exactamente.")
    
    st.markdown("#### 1. Arquitectura del Organigrama")
    tipo_org = st.selectbox("Selecciona el tipo de estructura para la clínica/empresa:", 
                            ["Estructura Funcional (Recomendada para clínicas medianas)", 
                             "Estructura Plana (Para startups o cabinas pequeñas)",
                             "Estructura Divisional (Si tienen sucursales o franquicias)"])
    
    if "Funcional" in tipo_org:
        st.info("🏢 **Funcional:** Agrupa a los empleados por su especialidad (Dirección, Clínica, Ventas, Administración). Garantiza que los especialistas sean dirigidos por expertos en su área.")
    elif "Plana" in tipo_org:
        st.info("➖ **Plana:** Se eliminan los mandos medios. Las cosmetólogas y vendedores reportan directamente al dueño. Da mucha velocidad, pero el dueño puede saturarse.")
    else:
        st.info("🗺️ **Divisional:** Dividido por sedes geográficas (ej. Sucursal Puebla Centro, Sucursal Cholula) o por tipo de negocio (Línea Cosmética vs Clínica de Servicios).")

    st.markdown("---")
    st.markdown("#### 2. Constructor del Manual de Puestos y Funciones")
    st.write("Selecciona un puesto clave para generar su perfil técnico y operativo.")
    
    puesto_sel = st.selectbox("Perfil a consultar:", 
                              ["Cosmetóloga / Cosmiatra Principal", 
                               "Director Médico (Responsable Sanitario)", 
                               "Gerente de Recepción y Ventas",
                               "Community Manager (Marketing)"])
    
    # Base de datos simulada de manuales de puestos
    manuales = {
        "Cosmetóloga / Cosmiatra Principal": {
            "objetivo": "Ejecutar con excelencia los protocolos estéticos faciales y corporales, garantizando la satisfacción del cliente y el cumplimiento de las normas de bioseguridad.",
            "reporta_a": "Director Médico / Gerente Operativo",
            "supervisa_a": "Auxiliares de cabina, practicantes.",
            "funciones": ["Realizar diagnósticos de piel.", "Aplicar tratamientos según aparatología y principios activos aprobados.", "Llenar expedientes clínicos y Consentimientos Informados.", "Venta cruzada de productos de apoyo en casa."],
            "requisitos": "Licenciatura en Cosmetología/Cosmiatría. Conocimiento profundo de INCI. Cursos en aparatología avanzada."
        },
        "Director Médico (Responsable Sanitario)": {
            "objetivo": "Garantizar el cumplimiento legal ante COFEPRIS y avalar los protocolos invasivos o aparatología médica tipo clase II y III.",
            "reporta_a": "Dirección General / Dueños",
            "supervisa_a": "Todo el personal clínico e instrumental.",
            "funciones": ["Firmar el aviso de funcionamiento.", "Aprobar manuales de procedimientos clínicos.", "Atender emergencias o reacciones adversas graves.", "Capacitar en bioseguridad."],
            "requisitos": "Título y Cédula de Médico Cirujano. Especialidad en Medicina Estética o Dermatología."
        },
        "Gerente de Recepción y Ventas": {
            "objetivo": "Maximizar la tasa de conversión de clientes, asegurar la rentabilidad diaria y brindar una excelente primera impresión en la clínica.",
            "reporta_a": "Dirección General",
            "supervisa_a": "Recepcionistas, personal de limpieza.",
            "funciones": ["Gestión de agenda y confirmación de citas.", "Cierre de ventas de paquetes y membresías.", "Corte de caja y facturación.", "Manejo de quejas y servicio al cliente."],
            "requisitos": "Lic. en Administración o afin. Excelente manejo de software de punto de venta y CRM. Habilidades de negociación."
        },
        "Community Manager (Marketing)": {
            "objetivo": "Posicionar la marca estética en el mercado digital y generar flujo constante de prospectos (leads) hacia la clínica.",
            "reporta_a": "Dirección General / Gerente de Ventas",
            "supervisa_a": "N/A",
            "funciones": ["Diseñar la parrilla de contenidos en redes sociales.", "Gestionar presupuesto de pauta (Meta Ads/Google).", "Responder mensajes y derivar prospectos a ventas.", "Vigilar el cumplimiento ético publicitario (evitar promesas engañosas)."],
            "requisitos": "Lic. en Comunicación o Mercadotecnia. Dominio de estrategias digitales y copywriting persuasivo."
        }
    }
    
    datos_puesto = manuales[puesto_sel]
    
    st.markdown(f"**Puesto:** {puesto_sel}")
    st.markdown(f"**📍 Objetivo del Puesto:** {datos_puesto['objetivo']}")
    
    c_jer1, c_jer2 = st.columns(2)
    with c_jer1: st.success(f"⬆️ **Le reporta a:** {datos_puesto['reporta_a']}")
    with c_jer2: st.info(f"⬇️ **Supervisa a:** {datos_puesto['supervisa_a']}")
    
    st.markdown("**📋 Funciones Específicas (Manual de Operaciones):**")
    for funcion in datos_puesto['funciones']:
        st.markdown(f"- {funcion}")
        
    st.markdown(f"**🎓 Perfil y Requisitos:** {datos_puesto['requisitos']}")