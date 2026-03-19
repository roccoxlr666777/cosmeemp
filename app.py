import streamlit as st
import pandas as pd

# ==========================================
# 1. CONFIGURACIÓN Y ESTILOS (Para PDF y UI)
# ==========================================
st.set_page_config(page_title="Simulador de Creación Cosmética", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #f9fbfd; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    h1, h2, h3 { color: #002b5e !important; }
    .brand-preview { padding: 30px; border-radius: 15px; text-align: center; margin-top: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); border: 2px solid transparent;}
    .example-box { background-color: #e8f4f8; border-left: 4px solid #3498db; padding: 10px; font-size: 0.9em; margin-bottom: 15px; border-radius: 4px; color: #555; }
    .card-foda { padding: 15px; border-radius: 8px; color: white; margin-bottom: 10px; font-weight: bold; text-align: center; }
    .metric-card { background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center; border-top: 4px solid #f2a900; margin-bottom: 10px;}
    .bg-fortaleza { background-color: #27ae60; }
    .bg-debilidad { background-color: #e74c3c; }
    .bg-oportunidad { background-color: #2980b9; }
    .bg-amenaza { background-color: #8e44ad; }

    @media print {
        header, .stSidebar, .stTabs [data-baseweb="tab-list"], button { display: none !important; }
        .stApp { background-color: white !important; padding: 0 !important; margin: 0 !important;}
        .brand-preview, .metric-card { box-shadow: none !important; border: 1px solid #ccc !important; }
        * { -webkit-print-color-adjust: exact !important; color-adjust: exact !important; }
        div[data-testid="stColorPicker"] { display: none !important; }
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. ENCABEZADO Y BOTÓN DE PDF
# ==========================================
col_header, col_print = st.columns([4, 1])
with col_header:
    st.markdown("<h1>✨ Simulador Integral: Empresa Cosmética</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #7f8c8d; font-size: 1.2em;'>De la Planeación a la Organización.</p>", unsafe_allow_html=True)
with col_print:
    st.components.v1.html("""
        <button onclick="window.parent.print()" style="background-color: #002b5e; color: white; border: none; padding: 12px 20px; border-radius: 8px; font-weight: bold; cursor: pointer; width: 100%; font-size: 1rem;">🖨️ Descargar Proyecto (PDF)</button>
    """, height=60)
    
st.markdown("---")

# ==========================================
# 3. DATOS MAESTROS
# ==========================================
psicologia_color = {
    "🔵 Azul": "Confianza, Calma, Profesionalismo. (Dermocosmética clínica).",
    "🟢 Verde": "Naturaleza, Orgánico, Sustentable. (Cosmética natural).",
    "⚪ Blanco": "Pureza, Minimalismo, Lujo. (Marcas premium).",
    "🟡 Dorado": "Prestigio, Lujo, Innovación. (Anti-edad).",
    "⚫ Negro": "Elegancia, Formalidad. (Líneas masculinas/noche).",
    "🟠 Naranja/Rosa": "Juventud, Creatividad. (Piel joven)."
}

iconos_disponibles = {
    "Acción y Rapidez": "⚡🚀💨", "Naturaleza y Botánica": "🌿💧🍂🌸",
    "Medios y Comunicación": "📱📣🌐🎥", "Religión/Importancia": "🕯️🏛️✨",
    "Ciencia y Clínica": "🧪🔬🎓🩺", "Belleza y Cuidado": "🧖‍♀️🧴💖💎"
}

# ==========================================
# 4. TABS PRINCIPALES (NUEVO ORDEN)
# ==========================================
tab_planeacion, tab_producto, tab_marketing, tab_finanzas, tab_legal, tab_organizacion = st.tabs([
    "🎯 1. Planeación", 
    "🧪 2. Producto y Receta", 
    "📊 3. Estrategia 4P", 
    "📈 4. Finanzas", 
    "⚖️ 5. Legal (COFEPRIS)",
    "🏢 6. Organización"
])

# ------------------------------------------
# TAB 1: PLANEACIÓN ESTRATÉGICA (FODA/PESTEL)
# ------------------------------------------
with tab_planeacion:
    st.markdown("### Identidad y Planeación")
    col_texto, col_visual = st.columns([3, 2])
    
    with col_texto:
        nombre_marca = st.text_input("Nombre de la Marca:", placeholder="Tu Marca")
        mision = st.text_area("Misión:")
        vision = st.text_area("Visión:")

    with col_visual:
        st.markdown("#### Diseño de Marca")
        color_primario = st.color_picker("Color Principal (Fondo):", "#002b5e")
        color_secundario = st.color_picker("Color Secundario (Acentos/Texto):", "#f2a900")
        st.selectbox("📖 Psicología del Color:", list(psicologia_color.values()))
        
        st.markdown(f"""
        <div class='brand-preview' style='background-color: {color_primario}; border: 3px solid {color_secundario};'>
            <h1 style='color: {color_secundario}; font-family: "Didot", serif; margin: 0;'>{nombre_marca if nombre_marca else "TU MARCA AQUÍ"}</h1>
            <p style='color: white; font-style: italic;'>Dermocosmética Avanzada</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Análisis FODA")
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.markdown("<div class='card-foda bg-fortaleza'>Fortalezas (Interno)</div>", unsafe_allow_html=True)
        st.text_area("Ventajas competitivas:", height=80, key="f")
        st.markdown("<div class='card-foda bg-oportunidad'>Oportunidades (Externo)</div>", unsafe_allow_html=True)
        st.text_area("Tendencias a aprovechar:", height=80, key="o")
    with col_f2:
        st.markdown("<div class='card-foda bg-debilidad'>Debilidades (Interno)</div>", unsafe_allow_html=True)
        st.text_area("Carencias o riesgos internos:", height=80, key="d")
        st.markdown("<div class='card-foda bg-amenaza'>Amenazas (Externo)</div>", unsafe_allow_html=True)
        st.text_area("Factores externos de riesgo:", height=80, key="a")

    st.markdown("---")
    st.markdown("### Análisis PESTEL")
    c_p1, c_p2 = st.columns(2)
    with c_p1:
        st.text_area("👮‍♂️ Político:")
        st.text_area("📉 Económico:")
        st.text_area("👥 Social:")
    with c_p2:
        st.text_area("⚙️ Tecnológico:")
        st.text_area("🌿 Ecológico:")
        st.text_area("⚖️ Legal General:")

# ------------------------------------------
# TAB 2: EL PRODUCTO (CALCULADORA DE RECETA)
# ------------------------------------------
with tab_producto:
    st.markdown("### 🧪 Formulación Cosmética y Cálculo de Producción")
    
    st.info("💡 Define los porcentajes de tu fórmula. Luego ingresa el volumen de tu envase para calcular exactamente cuántos mililitros/gramos necesitas llevar al laboratorio de cada ingrediente.")
    
    # 1. Ingreso del volumen total
    volumen_total = st.number_input("Volumen a fabricar por envase (ml/g):", value=50, step=10)
    
    st.write("**Edita los ingredientes y su porcentaje (%)**")
    
    # 2. Editor de tabla base
    df_inci_base = pd.DataFrame([
        {"Ingrediente INCI": "Aqua (Agua)", "Función": "Solvente", "Porcentaje (%)": 70.0},
        {"Ingrediente INCI": "Glycerin", "Función": "Humectante", "Porcentaje (%)": 5.0},
        {"Ingrediente INCI": "Niacinamide", "Función": "Activo", "Porcentaje (%)": 4.0},
        {"Ingrediente INCI": "Cetearyl Alcohol", "Función": "Emulsionante", "Porcentaje (%)": 6.0},
        {"Ingrediente INCI": "Aceite de Jojoba", "Función": "Emoliente", "Porcentaje (%)": 14.0},
        {"Ingrediente INCI": "Phenoxyethanol", "Función": "Conservador", "Porcentaje (%)": 1.0},
    ])
    
    # El usuario edita la tabla
    receta_editada = st.data_editor(df_inci_base, num_rows="dynamic", use_container_width=True)
    
    total_pct = receta_editada["Porcentaje (%)"].sum()
    
    # 3. Lógica de cálculo interactivo
    if total_pct == 100.0:
        st.success(f"✅ Fórmula estabilizada al 100%. Aquí está tu receta de laboratorio para un envase de {volumen_total} ml/g:")
        
        # Calcular los ml o gramos reales
        receta_editada["Cantidad Requerida (ml o g)"] = (receta_editada["Porcentaje (%)"] / 100) * volumen_total
        
        # Mostrar la tabla final no editable con los resultados
        st.dataframe(receta_editada[["Ingrediente INCI", "Porcentaje (%)", "Cantidad Requerida (ml o g)"]], use_container_width=True)
    else:
        st.error(f"⚠️ La fórmula debe sumar exactamente 100%. Actualmente suma: {total_pct}%")

    st.markdown("---")
    st.markdown("### 🛠️ Diseñador de Etiqueta Frontal")
    c_e1, c_e2 = st.columns(2)
    with c_e1:
        iconos_sel = st.multiselect("Selecciona los iconos del producto:", list(iconos_disponibles.values()))
        iconos_combinados = "".join(iconos_sel)
        
    with c_e2:
        st.markdown(f"""
        <div style='background-color: white; color: {color_primario}; padding: 30px; border: 2px solid {color_primario}; text-align: center;'>
            <h4 style='color: {color_primario}; margin: 0;'>{nombre_marca if nombre_marca else "MARCA"}</h4>
            <div style='background-color: {color_primario}; height: 2px; width: 30%; margin: 5px auto;'></div>
            <h2 style='color: {color_secundario}; margin: 10px 0;'>{iconos_combinados if iconos_combinados else "🧩🧩"}</h2>
            <p style='font-weight: bold;'>CONTENIDO NETO: {volumen_total} ml/g</p>
        </div>
        """, unsafe_allow_html=True)

# ------------------------------------------
# TAB 3: ESTRATEGIA 4P
# ------------------------------------------
with tab_marketing:
    st.markdown("### Estrategia de Marketing (Mix 4P)")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.text_area("📦 Producto (Atributos, empaque, beneficio):")
        st.text_area("📍 Plaza (Canales de distribución):")
    with col_p2:
        st.text_area("📣 Promoción (Publicidad, redes):")
        st.text_area("💵 Estrategia de Precio (Psicología de cobro):")

# ------------------------------------------
# TAB 4: FINANZAS (COSTOS Y PUNTO DE EQUILIBRIO)
# ------------------------------------------
with tab_finanzas:
    st.markdown("### Costos y Fijación de Precio")
    col_cf, col_cv = st.columns(2)
    
    with col_cf:
        st.markdown("#### Costos Fijos Mensuales (CF)")
        df_cf = pd.DataFrame([{"Costo Fijo": f"Rubro {i+1}", "Monto ($)": 0.0} for i in range(6)])
        cf_editado = st.data_editor(df_cf, use_container_width=True, key="d_cf")
        total_cf = cf_editado["Monto ($)"].sum()
        st.markdown(f"<h4 style='color: #c0392b;'>Total CF: ${total_cf:,.2f}</h4>", unsafe_allow_html=True)

    with col_cv:
        st.markdown("#### Costos Variables por Unidad (CVu)")
        df_cv = pd.DataFrame([{"Costo Variable": f"Rubro {i+1}", "Monto ($)": 0.0} for i in range(6)])
        cv_editado = st.data_editor(df_cv, use_container_width=True, key="d_cv")
        total_cv_unitario = cv_editado["Monto ($)"].sum()
        st.markdown(f"<h4 style='color: #2980b9;'>Total CVu: ${total_cv_unitario:,.2f}</h4>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Proyección y Punto de Equilibrio")
    col_proj1, col_proj2, col_proj3 = st.columns(3)
    
    with col_proj1:
        margen = st.number_input("Margen Deseado sobre Costo (%):", value=60.0)
        precio_sugerido = total_cv_unitario + (total_cv_unitario * (margen / 100))
        precio_real = st.number_input("💵 Precio Final de Venta:", value=precio_sugerido)

    with col_proj2:
        u_producidas = st.number_input("Unidades PRODUCIDAS al Mes:", value=500)
        u_vendidas = st.number_input("Unidades VENDIDAS al Mes:", value=300)
        if u_vendidas > u_producidas: st.warning("⚠️ No puedes vender más de lo que produces.")

    with col_proj3:
        ingresos = u_vendidas * precio_real
        costo_produccion = u_producidas * total_cv_unitario
        utilidad_neta = ingresos - (total_cf + costo_produccion)
        try: p_equilibrio = total_cf / (precio_real - total_cv_unitario)
        except ZeroDivisionError: p_equilibrio = 0
            
        st.markdown(f"<div class='metric-card'><h4>Ingresos Totales</h4><h2>${ingresos:,.2f}</h2></div>", unsafe_allow_html=True)

    col_res1, col_res2 = st.columns(2)
    with col_res1:
        c_util = "#27ae60" if utilidad_neta >= 0 else "#e74c3c"
        st.markdown(f"<div class='metric-card'><h4>Utilidad Neta (Ganancia)</h4><h2 style='color: {c_util};'>${utilidad_neta:,.2f}</h2></div>", unsafe_allow_html=True)
    with col_res2:
        st.markdown(f"<div class='metric-card'><h4>Punto de Equilibrio</h4><h2>{int(p_equilibrio) + 1} unidades</h2></div>", unsafe_allow_html=True)

# ------------------------------------------
# TAB 5: LEGAL (COFEPRIS ANTES DE ORGANIZACIÓN)
# ------------------------------------------
with tab_legal:
    st.markdown("### ⚖️ Marco Legal y Regulatorio (COFEPRIS)")
    
    st.markdown("""
    <div style='background-color: #fff3e0; padding: 20px; border-left: 5px solid #ff9800; border-radius: 5px; margin-bottom: 20px;'>
        <h4 style='margin-top:0;'>Reglas Generales para la Comercialización Cosmética</h4>
        <ul>
            <li><b>Aviso de Funcionamiento:</b> Requisito obligatorio para la comercialización o fabricación. Se ingresa ante COFEPRIS o secretarías de salud estatales.</li>
            <li><b>Clave SCIAN:</b> Para comercialización al por menor de cosméticos, se usa generalmente la clave <b>464112</b>.</li>
            <li><b>Publicidad:</b> Está estrictamente prohibido atribuir propiedades terapéuticas, curativas o preventivas a un cosmético (ej. "cura el acné"). Solo se permiten fines de embellecimiento o limpieza.</li>
            <li><b>Etiquetado (NOM-141):</b> Debe incluir denominación, contenido neto, instrucciones de uso, precauciones y lote.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Redacción del Aviso de Funcionamiento")
    st.write("Elabora el borrador de tu aviso incluyendo: Datos del propietario (RFC), domicilio de la clínica/tienda, representante legal y la clave SCIAN elegida.")
    
    aviso_cofepris = st.text_area("✍️ Redacta aquí el borrador de tu Aviso de Funcionamiento:", height=250)

# ------------------------------------------
# TAB 6: ORGANIZACIÓN (AL FINAL)
# ------------------------------------------
with tab_organizacion:
    st.markdown("### Estructura Organizacional y Jerárquica")
    
    st.markdown("#### 6.1 Organigrama Funcional")
    st.components.v1.html(f"""
    <style>
        .tree ul {{ padding-top: 20px; position: relative; transition: all 0.5s; }}
        .tree li {{ float: left; text-align: center; list-style-type: none; position: relative; padding: 20px 5px 0 5px; }}
        .tree li::before, .tree li::after {{ content: ''; position: absolute; top: 0; right: 50%; border-top: 2px solid #002b5e; width: 50%; height: 20px; }}
        .tree li::after {{ right: auto; left: 50%; border-left: 2px solid #002b5e; }}
        .tree li:only-child::after, .tree li:only-child::before {{ display: none; }}
        .tree li:only-child {{ padding-top: 0; }}
        .tree li:first-child::before, .tree li:last-child::after {{ border: 0 none; }}
        .tree li:last-child::before {{ border-right: 2px solid #002b5e; border-radius: 0 5px 0 0; }}
        .tree li:first-child::after {{ border-radius: 5px 0 0 0; }}
        .tree ul ul::before {{ content: ''; position: absolute; top: 0; left: 50%; border-left: 2px solid #002b5e; width: 0; height: 20px; }}
        .tree li div {{ border: 2px solid #002b5e; padding: 10px; border-radius: 8px; color: #002b5e; font-weight: bold; background-color: white; }}
    </style>
    <div class="tree" style="display: flex; justify-content: center;">
        <ul>
            <li>
                <div>Dirección General (Tú)</div>
                <ul>
                    <li><div>Director Médico / Sanitario</div><ul><li><div>Cosmetólogas</div></li></ul></li>
                    <li><div>Gerente Ventas / Mkt</div><ul><li><div>Recepción</div></li></ul></li>
                </ul>
            </li>
        </ul>
    </div>
    """, height=300)

    st.markdown("---")
    st.markdown("#### 6.2 Manual de Puestos y Funciones")
    puestos = {
        "Cosmetóloga Principal": {"Reporta": "Dir. Médico", "Supervisa": "Auxiliares", "Funciones": ["Diagnóstico facial", "Aparatología", "Bioseguridad"]},
        "Director Médico": {"Reporta": "Dir. General", "Supervisa": "Cabina", "Funciones": ["Aviso COFEPRIS", "Aval de tratamientos", "Emergencias"]},
        "Gerente de Ventas": {"Reporta": "Dir. General", "Supervisa": "Recepción", "Funciones": ["Agenda", "Cierre de ventas", "Facturación"]}
    }
    
    puesto_sel = st.selectbox("Selecciona perfil:", list(puestos.keys()))
    info_p = puestos[puesto_sel]
    
    st.markdown(f"<div class='metric-card' style='border-top: 4px solid #002b5e; text-align: left;'>", unsafe_allow_html=True)
    st.markdown(f"**Puesto:** {puesto_sel}")
    st.markdown(f"**⬅️ Reporta a:** {info_p['Reporta']} | **➡️ Supervisa a:** {info_p['Supervisa']}")
    st.markdown("**📋 Funciones:**")
    for func in info_p['Funciones']: st.markdown(f"- {func}")
    st.markdown("</div>", unsafe_allow_html=True)
