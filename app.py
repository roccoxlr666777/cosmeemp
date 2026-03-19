import streamlit as st
import pandas as pd
import html

# ==========================================
# 1. CONFIGURACIÓN Y CSS (Incluye formato para impresión a PDF)
# ==========================================
st.set_page_config(page_title="Simulador de Creación Cosmética", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    /* Estilos generales */
    .stApp { background-color: #f9fbfd; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    h1, h2, h3 { color: #2c3e50 !important; }
    
    /* Cajas de diseño */
    .brand-preview { padding: 30px; border-radius: 15px; text-align: center; margin-top: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); transition: all 0.3s ease; }
    .example-box { background-color: #e8f4f8; border-left: 4px solid #3498db; padding: 10px; font-size: 0.9em; margin-bottom: 15px; }
    .metric-card { background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center; border-top: 4px solid #f2a900; }
    
    /* Estilos para ocultar elementos al imprimir a PDF */
    @media print {
        header, .stSidebar, .stTabs [data-baseweb="tab-list"], button { display: none !important; }
        .stApp { background-color: white !important; }
        .brand-preview, .metric-card { box-shadow: none !important; border: 1px solid #ccc !important; }
        * { -webkit-print-color-adjust: exact !important; color-adjust: exact !important; }
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# ENCABEZADO Y BOTÓN DE PDF
# ==========================================
col_header, col_print = st.columns([4, 1])
with col_header:
    st.markdown("<h1>✨ Simulador Integral: Creación de Empresa Cosmética</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #7f8c8d; font-size: 1.2em;'>Desde la formulación INCI hasta el punto de equilibrio financiero.</p>", unsafe_allow_html=True)
with col_print:
    # Inyección de JavaScript para imprimir
    st.components.v1.html("""
        <button onclick="window.print()" style="background-color: #002b5e; color: white; border: none; padding: 10px 20px; border-radius: 5px; font-weight: bold; cursor: pointer; width: 100%;">🖨️ Imprimir Proyecto a PDF</button>
    """, height=50)

st.markdown("---")

# ==========================================
# TABS PRINCIPALES
# ==========================================
tab_identidad, tab_receta, tab_estrategia, tab_finanzas, tab_caso = st.tabs([
    "🎨 1. Marca e Identidad", 
    "🧪 2. Formulación", 
    "🎯 3. Estrategia 4P", 
    "📈 4. Costeo y Finanzas",
    "⚖️ 5. Caso Legal COFEPRIS"
])

# ------------------------------------------
# TAB 1: IDENTIDAD Y MARCA
# ------------------------------------------
with tab_identidad:
    st.markdown("### Identidad Filosófica y Visual")
    
    col_texto, col_visual = st.columns([3, 2])
    
    with col_texto:
        nombre = st.text_input("Nombre de la Marca:")
        
        st.markdown("<div class='example-box'><b>Ejemplo de Misión:</b> Potenciar la salud cutánea de nuestros clientes mediante cosmética natural, ofreciendo fórmulas libres de crueldad animal y de alta eficacia comprobada.</div>", unsafe_allow_html=True)
        mision = st.text_area("Misión:")
        
        st.markdown("<div class='example-box'><b>Ejemplo de Visión:</b> Posicionarnos para el 2030 como la marca líder en dermocosmética sustentable en el centro de México, expandiendo nuestra línea a tratamientos clínicos.</div>", unsafe_allow_html=True)
        vision = st.text_area("Visión:")
        
        st.markdown("<div class='example-box'><b>Ejemplo de Valores:</b> Transparencia científica, Ética profesional, Sustentabilidad, Innovación continua.</div>", unsafe_allow_html=True)
        valores = st.text_input("Valores:")

    with col_visual:
        st.markdown("#### Psicología del Color")
        color_primario = st.color_picker("Color Principal (Fondo):", "#002b5e")
        color_secundario = st.color_picker("Color Secundario (Texto/Acentos):", "#f2a900")
        
        # Previsualización dinámica de la marca
        st.markdown(f"""
        <div class='brand-preview' style='background-color: {color_primario};'>
            <h2 style='color: {color_secundario}; font-family: "Didot", serif; margin-bottom: 5px;'>{nombre if nombre else "TU MARCA AQUÍ"}</h2>
            <p style='color: white; font-size: 0.9em; font-style: italic;'>Dermocosmética Avanzada</p>
            <div style='background-color: {color_secundario}; height: 3px; width: 50%; margin: 0 auto; border-radius: 2px;'></div>
        </div>
        """, unsafe_allow_html=True)

# ------------------------------------------
# TAB 2: RECETA / FORMULACIÓN
# ------------------------------------------
with tab_receta:
    st.markdown("### Tabla de Formulación Cosmética (INCI)")
    st.write("Estructura la base, los activos y los aditivos de tu producto estrella.")
    
    # Tabla editable usando pandas y st.data_editor
    df_receta = pd.DataFrame(
        [
            {"Nomenclatura INCI": "Aqua", "Función": "Solvente (Fase Acuosa)", "Porcentaje (%)": 70.0},
            {"Nomenclatura INCI": "Glycerin", "Función": "Humectante", "Porcentaje (%)": 5.0},
            {"Nomenclatura INCI": "Niacinamide", "Función": "Principio Activo (Seborregulador)", "Porcentaje (%)": 4.0},
            {"Nomenclatura INCI": "Cetearyl Alcohol", "Función": "Emulsionante", "Porcentaje (%)": 6.0},
            {"Nomenclatura INCI": "Simmondsia Chinensis Seed Oil", "Función": "Emoliente", "Porcentaje (%)": 14.0},
            {"Nomenclatura INCI": "Phenoxyethanol", "Función": "Conservador", "Porcentaje (%)": 1.0},
        ]
    )
    
    receta_editada = st.data_editor(df_receta, num_rows="dynamic", use_container_width=True)
    
    total_pct = receta_editada["Porcentaje (%)"].sum()
    if total_pct == 100.0:
        st.success(f"✅ Fórmula estabilizada. Total: {total_pct}%")
    else:
        st.error(f"⚠️ Error de formulación: El porcentaje total debe ser 100%. Actual: {total_pct}%")

# ------------------------------------------
# TAB 3: ESTRATEGIA 4 P's
# ------------------------------------------
with tab_estrategia:
    st.markdown("### Estrategia de Marketing (Mix 4P)")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='example-box'><b>Ejemplo Producto:</b> Crema facial de textura ligera, envase airless de 50ml, aroma cítrico suave, empaque de cartón reciclado con sello Cruelty Free.</div>", unsafe_allow_html=True)
        producto = st.text_area("📦 Producto (Características físicas, empaque, beneficios):")
        
        st.markdown("<div class='example-box'><b>Ejemplo Plaza:</b> Venta directa en cabina estética (30%) y tienda online propia con envíos nacionales vía FedEx (70%).</div>", unsafe_allow_html=True)
        plaza = st.text_area("📍 Plaza (Canales de distribución y venta):")
        
    with c2:
        st.markdown("<div class='example-box'><b>Ejemplo Promoción:</b> Campañas de conversión en Meta Ads, micro-influencers de Skincare en TikTok, y masterclass gratuita de cuidado facial en la clínica.</div>", unsafe_allow_html=True)
        promocion = st.text_area("📣 Promoción (Publicidad, RRPP, redes sociales):")
        
        st.markdown("<div class='example-box'><b>Ejemplo Precio:</b> Estrategia de 'Prestige Pricing'. Precio alto para denotar calidad premium frente a marcas de supermercado.</div>", unsafe_allow_html=True)
        estrategia_precio = st.text_area("💵 Estrategia de Precio (Psicología detrás del cobro):")

# ------------------------------------------
# TAB 4: COSTEO Y FINANZAS
# ------------------------------------------
with tab_finanzas:
    st.markdown("### Estructura de Costos y Fijación de Precio")
    
    col_cf, col_cv = st.columns(2)
    
    # 6 Columnas/Campos para Costos Fijos
    with col_cf:
        st.markdown("#### Costos Fijos Mensuales (CF)")
        cf1 = st.number_input("1. Renta de local/cabina:", value=8000.0)
        cf2 = st.number_input("2. Sueldos base (dueño/empleados):", value=12000.0)
        cf3 = st.number_input("3. Servicios (Agua, Luz, Internet):", value=2500.0)
        cf4 = st.number_input("4. Publicidad fija mensual:", value=3000.0)
        cf5 = st.number_input("5. Suscripciones (Software/Punto de venta):", value=500.0)
        cf6 = st.number_input("6. Otros fijos (Seguros/Contador):", value=1500.0)
        total_cf = cf1 + cf2 + cf3 + cf4 + cf5 + cf6
        st.markdown(f"<h4 style='color: #c0392b;'>Total CF Mensual: ${total_cf:,.2f}</h4>", unsafe_allow_html=True)

    # 6 Columnas/Campos para Costos Variables (Por Unidad)
    with col_cv:
        st.markdown("#### Costos Variables por Producto (CVu)")
        cv1 = st.number_input("1. Materia prima (INCI total por unidad):", value=45.0)
        cv2 = st.number_input("2. Envase primario (Frasco/Tarro):", value=18.0)
        cv3 = st.number_input("3. Empaque secundario (Caja):", value=12.0)
        cv4 = st.number_input("4. Etiquetado (Frontal e INCI trasero):", value=5.0)
        cv5 = st.number_input("5. Envío / Logística por unidad:", value=0.0)
        cv6 = st.number_input("6. Comisión bancaria/pasarela por venta:", value=15.0)
        total_cv_unitario = cv1 + cv2 + cv3 + cv4 + cv5 + cv6
        st.markdown(f"<h4 style='color: #2980b9;'>Total CVu: ${total_cv_unitario:,.2f}</h4>", unsafe_allow_html=True)

    st.markdown("---")
    
    # Fijación de Precio y Proyecciones
    st.markdown("### Fijación de Precio y Proyección Financiera")
    
    col_proj1, col_proj2, col_proj3 = st.columns(3)
    
    with col_proj1:
        margen_deseado = st.number_input("Margen de Ganancia Deseado (%):", value=60.0, step=5.0)
        # Fórmula de fijación de precio por margen: Precio = Costo / (1 - Margen%) o Precio = Costo + (Costo * Margen%)
        # Usaremos el modelo de recargo (Markup) directo para facilitar a los alumnos
        precio_final = total_cv_unitario + (total_cv_unitario * (margen_deseado / 100))
        st.info(f"🏷️ **Precio de Venta Sugerido:** ${precio_final:,.2f}")
        
        # Override opcional del alumno
        precio_real = st.number_input("Precio Final de Venta (Tu decisión):", value=precio_final)

    with col_proj2:
        unidades_producidas = st.number_input("Unidades Producidas al Mes:", value=500, step=50)
        unidades_vendidas = st.number_input("Unidades Vendidas al Mes:", value=300, step=50)
        
        if unidades_vendidas > unidades_producidas:
            st.warning("⚠️ No puedes vender más de lo que produces.")

    with col_proj3:
        # Cálculos de rentabilidad
        ingresos_totales = unidades_vendidas * precio_real
        costo_produccion_total = unidades_producidas * total_cv_unitario # Se gasta en lo que se produce
        gastos_totales = total_cf + costo_produccion_total
        utilidad_neta = ingresos_totales - gastos_totales
        
        try:
            punto_equilibrio_unidades = total_cf / (precio_real - total_cv_unitario)
        except ZeroDivisionError:
            punto_equilibrio_unidades = 0
            
        st.markdown(f"<div class='metric-card'><h4>Ingresos Totales</h4><h2>${ingresos_totales:,.2f}</h2></div>", unsafe_allow_html=True)

    col_res1, col_res2 = st.columns(2)
    with col_res1:
        color_utilidad = "#27ae60" if utilidad_neta >= 0 else "#e74c3c"
        st.markdown(f"<div class='metric-card'><h4>Utilidad Neta (Ganancia)</h4><h2 style='color: {color_utilidad};'>${utilidad_neta:,.2f}</h2></div>", unsafe_allow_html=True)
    with col_res2:
        st.markdown(f"<div class='metric-card'><h4>Punto de Equilibrio</h4><h2>{int(punto_equilibrio_unidades) + 1} unidades</h2><p style='color: gray; font-size: 0.8em;'>Para cubrir fijos y variables sin perder dinero.</p></div>", unsafe_allow_html=True)

# ------------------------------------------
# TAB 5: CASO ÉTICO / COFEPRIS
# ------------------------------------------
with tab_caso:
    st.markdown("### Dilema de Negocios y Ética Regulatoria")
    
    st.markdown("""
    <div style="background-color: #f2f2f2; padding: 20px; border-radius: 10px; border-left: 5px solid #e67e22;">
    <h4>El Caso: "Aceite para Barba Detox Extremo"</h4>
    <p>Has lanzado al mercado un producto masculino llamado <i>Aceite para Barba Detox Extremo</i>. La formulación incluye aceites esenciales de menta y eucalipto en altas concentraciones. Tus ventas van increíblemente bien.</p>
    <p>Sin embargo, en tu estrategia de promoción (P de Promoción), tu equipo de marketing decidió poner en la etiqueta frontal y en la página web oficial la siguiente frase publicitaria:</p>
    <p style="font-size: 1.2em; font-weight: bold; font-style: italic; text-align: center;">"El único aceite terapéutico que cura la dermatitis facial, acelera el crecimiento del vello en 3 días y elimina toxinas de la sangre."</p>
    <p>A las dos semanas, recibes una notificación de visita de inspección por parte de COFEPRIS por sospecha de producto frontera (producto milagro).</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### Resolución del Conflicto:")
    q1 = st.text_area("1. Análisis INCI y Etiquetado: ¿Qué errores cometió la empresa en las afirmaciones de la etiqueta según el reglamento de productos cosméticos?")
    q2 = st.text_area("2. Estrategia Legal: ¿Qué plan de acción inmediato debes tomar para evitar la inmovilización del producto y las multas?")
    q3 = st.text_area("3. Bioética: Haciendo referencia al concepto de 'El Precio de la Perfección', ¿cómo afecta a la reputación de la marca jugar con la desesperación de los clientes mediante promesas falsas de crecimiento en 3 días?")
