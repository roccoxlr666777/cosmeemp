import streamlit as st
import pandas as pd

# ==========================================
# 1. CONFIGURACIÓN Y ESTILOS
# ==========================================
st.set_page_config(page_title="Simulador Cosmético", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #f9fbfd; font-family: 'Segoe UI', sans-serif; }
    h1, h2, h3 { color: #002b5e !important; }
    .brand-preview { padding: 30px; border-radius: 15px; text-align: center; margin-top: 20px; border: 2px solid transparent;}
    .metric-card { background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center; border-top: 4px solid #f2a900; margin-bottom: 10px;}
    .card-foda { padding: 15px; border-radius: 8px; color: white; margin-bottom: 10px; font-weight: bold; text-align: center; }
    .bg-fortaleza { background-color: #27ae60; } .bg-debilidad { background-color: #e74c3c; }
    .bg-oportunidad { background-color: #2980b9; } .bg-amenaza { background-color: #8e44ad; }
    
    @media print {
        header, .stSidebar, div[data-baseweb="tab-list"], button { display: none !important; }
        .stApp { background-color: white !important; padding: 0 !important; margin: 0 !important;}
        .brand-preview, .metric-card { box-shadow: none !important; border: 1px solid #ccc !important; }
        * { -webkit-print-color-adjust: exact !important; color-adjust: exact !important; }
        div[data-testid="stColorPicker"] { display: none !important; }
        div[data-baseweb="tab-panel"], div[role="tabpanel"] {
            display: block !important; visibility: visible !important; opacity: 1 !important;
            height: auto !important; overflow: visible !important; page-break-after: always;
        }
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. MEMORIA DEL SERVIDOR (Evita reseteos)
# ==========================================
if 'df_inci' not in st.session_state:
    st.session_state.df_inci = pd.DataFrame([
        {"Ingrediente INCI": "Aqua", "Función": "Solvente", "Porcentaje (%)": 70.0},
        {"Ingrediente INCI": "Glycerin", "Función": "Humectante", "Porcentaje (%)": 5.0},
        {"Ingrediente INCI": "Niacinamide", "Función": "Activo", "Porcentaje (%)": 4.0},
        {"Ingrediente INCI": "Cetearyl Alcohol", "Función": "Emulsionante", "Porcentaje (%)": 6.0},
        {"Ingrediente INCI": "Aceite de Jojoba", "Función": "Emoliente", "Porcentaje (%)": 14.0},
        {"Ingrediente INCI": "Phenoxyethanol", "Función": "Conservador", "Porcentaje (%)": 1.0},
    ])
if 'df_cf' not in st.session_state:
    st.session_state.df_cf = pd.DataFrame([
        {"Rubro": "Renta Cabina", "Monto ($)": 8000.0}, {"Rubro": "Sueldos", "Monto ($)": 15000.0},
        {"Rubro": "Servicios", "Monto ($)": 2500.0}, {"Rubro": "Marketing", "Monto ($)": 3000.0},
        {"Rubro": "Software CRM", "Monto ($)": 800.0}, {"Rubro": "Otros Fijos", "Monto ($)": 1200.0}
    ])
if 'df_cv' not in st.session_state:
    st.session_state.df_cv = pd.DataFrame([
        {"Rubro": "Materia Prima INCI", "Monto ($)": 45.0}, {"Rubro": "Envase Primario", "Monto ($)": 18.0},
        {"Rubro": "Empaque / Caja", "Monto ($)": 12.0}, {"Rubro": "Etiquetas", "Monto ($)": 5.0},
        {"Rubro": "Logística Envío", "Monto ($)": 0.0}, {"Rubro": "Comisión Venta", "Monto ($)": 15.0}
    ])

# ==========================================
# 3. ENCABEZADO Y BOTÓN PDF
# ==========================================
col_header, col_print = st.columns([4, 1])
with col_header:
    st.markdown("<h1>✨ Simulador Integral: Empresa Cosmética</h1>", unsafe_allow_html=True)
with col_print:
    st.components.v1.html("""<button onclick="window.parent.print()" style="background-color: #002b5e; color: white; border: none; padding: 12px; border-radius: 8px; font-weight: bold; cursor: pointer; width: 100%;">🖨️ Imprimir a PDF</button>""", height=60)

# ==========================================
# 4. TABS
# ==========================================
tabs = st.tabs(["🎯 1. Planeación", "🧪 2. Producto", "📊 3. Mix 4P", "📈 4. Finanzas", "⚖️ 5. Legal", "🏢 6. Organización"])

# --- TAB 1: PLANEACIÓN ---
with tabs[0]:
    col_t, col_v = st.columns([3, 2])
    with col_t:
        nombre_marca = st.text_input("Nombre de la Marca:", "DermaNova")
        st.text_area("Misión:")
        st.text_area("Visión:")
    with col_v:
        color_p = st.color_picker("Color Primario:", "#002b5e")
        color_s = st.color_picker("Color Secundario:", "#f2a900")
        st.markdown(f"<div class='brand-preview' style='background-color: {color_p}; border: 3px solid {color_s};'><h1 style='color: {color_s}; margin: 0;'>{nombre_marca}</h1><p style='color: white;'>Dermocosmética</p></div>", unsafe_allow_html=True)
    
    st.markdown("### Análisis FODA")
    c_f1, c_f2 = st.columns(2)
    with c_f1:
        st.markdown("<div class='card-foda bg-fortaleza'>Fortalezas</div>", unsafe_allow_html=True); st.text_area("Internas positivas:", key="f")
        st.markdown("<div class='card-foda bg-oportunidad'>Oportunidades</div>", unsafe_allow_html=True); st.text_area("Externas positivas:", key="o")
    with c_f2:
        st.markdown("<div class='card-foda bg-debilidad'>Debilidades</div>", unsafe_allow_html=True); st.text_area("Internas negativas:", key="d")
        st.markdown("<div class='card-foda bg-amenaza'>Amenazas</div>", unsafe_allow_html=True); st.text_area("Externas negativas:", key="a")
        
    st.markdown("### Análisis PESTEL")
    cp1, cp2 = st.columns(2)
    with cp1:
        st.text_input("👮‍♂️ Político:"); st.text_input("📉 Económico:"); st.text_input("👥 Social:")
    with cp2:
        st.text_input("⚙️ Tecnológico:"); st.text_input("🌿 Ecológico:"); st.text_input("⚖️ Legal:")

# --- TAB 2: PRODUCTO (RECETA) ---
with tabs[1]:
    st.markdown("### 🧪 Formulación y Cálculo (INCI)")
    volumen = st.number_input("Volumen a fabricar por envase (ml/g):", value=50)
    
    df_edit = st.data_editor(st.session_state.df_inci, num_rows="dynamic", use_container_width=True)
    total_pct = df_edit["Porcentaje (%)"].sum()
    
    if total_pct == 100.0:
        st.success(f"✅ Fórmula al 100%. Cantidades exactas para {volumen} ml/g:")
        df_calc = df_edit.copy()
        df_calc["Gramos / Mililitros Reales"] = (df_calc["Porcentaje (%)"] / 100) * volumen
        st.dataframe(df_calc[["Ingrediente INCI", "Porcentaje (%)", "Gramos / Mililitros Reales"]], use_container_width=True)
    else:
        st.error(f"⚠️ La fórmula debe sumar 100%. Actualmente suma: {total_pct}%")
        
    st.markdown("### 🛠️ Etiqueta Frontal")
    c_e1, c_e2 = st.columns(2)
    with c_e1:
        iconos = st.multiselect("Iconos:", ["🌿", "💧", "🔬", "⚡", "🌸", "✨"])
    with c_e2:
        st.markdown(f"<div style='border: 2px solid {color_p}; text-align: center; padding: 20px;'><h3 style='color: {color_p};'>{nombre_marca}</h3><h1 style='color: {color_s};'>{''.join(iconos)}</h1><p>CONTENIDO: {volumen} ml</p></div>", unsafe_allow_html=True)

# --- TAB 3: MARKETING 4P ---
with tabs[2]:
    st.markdown("### Estrategia de Marketing (Mix 4P)")
    c4p1, c4p2 = st.columns(2)
    with c4p1:
        st.text_area("📦 Producto:"); st.text_area("📍 Plaza:")
    with c4p2:
        st.text_area("📣 Promoción:"); st.text_area("💵 Precio (Estrategia):")

# --- TAB 4: FINANZAS (COSTOS Y PUNTO EQUILIBRIO) ---
with tabs[3]:
    st.markdown("### Costos y Fijación de Precio")
    col_cf, col_cv = st.columns(2)
    
    with col_cf:
        st.markdown("#### Costos Fijos Mensuales")
        cf_edit = st.data_editor(st.session_state.df_cf, use_container_width=True)
        total_cf = cf_edit["Monto ($)"].sum()
        st.markdown(f"<h4 style='color: #c0392b;'>Total CF: ${total_cf:,.2f}</h4>", unsafe_allow_html=True)

    with col_cv:
        st.markdown("#### Costos Variables Unitarios")
        cv_edit = st.data_editor(st.session_state.df_cv, use_container_width=True)
        total_cv = cv_edit["Monto ($)"].sum()
        st.markdown(f"<h4 style='color: #2980b9;'>Total CVu: ${total_cv:,.2f}</h4>", unsafe_allow_html=True)

    st.markdown("---")
    c_p1, c_p2, c_p3 = st.columns(3)
    
    with c_p1:
        margen = st.number_input("Margen Deseado (%):", value=65.0)
        p_sugerido = total_cv + (total_cv * (margen / 100))
        p_real = st.number_input("💵 Precio Final de Venta:", value=p_sugerido)
    with c_p2:
        u_prod = st.number_input("Unidades PRODUCIDAS:", value=500)
        u_vend = st.number_input("Unidades VENDIDAS:", value=300)
        if u_vend > u_prod: st.warning("⚠️ No puedes vender más de lo que produces.")
    with c_p3:
        ingresos = u_vend * p_real
        st.markdown(f"<div class='metric-card'><h4>Ingresos Totales</h4><h2>${ingresos:,.2f}</h2></div>", unsafe_allow_html=True)

    c_r1, c_r2 = st.columns(2)
    with c_r1:
        utilidad = ingresos - (total_cf + (u_prod * total_cv))
        color_u = "#27ae60" if utilidad >= 0 else "#e74c3c"
        st.markdown(f"<div class='metric-card'><h4>Utilidad Neta</h4><h2 style='color: {color_u};'>${utilidad:,.2f}</h2></div>", unsafe_allow_html=True)
    with c_r2:
        try: p_eq = total_cf / (p_real - total_cv)
        except ZeroDivisionError: p_eq = 0
        st.markdown(f"<div class='metric-card'><h4>Punto de Equilibrio</h4><h2>{int(p_eq) + 1} unidades</h2></div>", unsafe_allow_html=True)

# --- TAB 5: LEGAL ---
with tabs[4]:
    st.markdown("### ⚖️ Comercialización y COFEPRIS")
    st.write("**Reglas:** Aviso de funcionamiento obligatorio (SCIAN 464112). Prohibido atribuir propiedades curativas.")
    st.text_area("✍️ Redacta tu borrador de Aviso de Funcionamiento:", height=200)

# --- TAB 6: ORGANIZACIÓN ---
with tabs[5]:
    st.markdown("### 🏢 Jerarquía")
    st.components.v1.html("""
    <style>
        .tree ul { padding-top: 20px; position: relative; transition: all 0.5s; display: flex; justify-content: center; }
        .tree li { text-align: center; list-style-type: none; position: relative; padding: 20px 5px 0 5px; }
        .tree li::before, .tree li::after { content: ''; position: absolute; top: 0; right: 50%; border-top: 2px solid #002b5e; width: 50%; height: 20px; }
        .tree li::after { right: auto; left: 50%; border-left: 2px solid #002b5e; }
        .tree li:only-child::after, .tree li:only-child::before { display: none; }
        .tree li:only-child { padding-top: 0; }
        .tree li:first-child::before, .tree li:last-child::after { border: 0 none; }
        .tree li:last-child::before { border-right: 2px solid #002b5e; border-radius: 0 5px 0 0; }
        .tree li:first-child::after { border-radius: 5px 0 0 0; }
        .tree ul ul::before { content: ''; position: absolute; top: 0; left: 50%; border-left: 2px solid #002b5e; width: 0; height: 20px; }
        .tree li div { border: 2px solid #002b5e; padding: 10px; border-radius: 8px; font-weight: bold; background-color: white; }
    </style>
    <div class="tree"><ul><li><div>Dirección General</div><ul><li><div>Dir. Médico</div><ul><li><div>Cosmetólogas</div></li></ul></li><li><div>Gerente Ventas</div><ul><li><div>Recepción</div></li></ul></li></ul></li></ul></div>
    """, height=250)
    
    st.markdown("#### Manual de Puestos")
    p = st.selectbox("Perfil:", ["Cosmetóloga", "Director Médico", "Recepción"])
    if p == "Cosmetóloga": st.info("Reporta: Médico | Funciones: Diagnóstico facial, Aparatología.")
    elif p == "Director Médico": st.info("Reporta: Dirección | Funciones: Aviso COFEPRIS, Urgencias.")
    else: st.info("Reporta: Dirección | Funciones: Cobros, Agenda, Cierre Ventas.")
