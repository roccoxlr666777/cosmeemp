import streamlit as st
import pandas as pd
import html
import random

# ==========================================
# 1. CONFIGURACIÓN Y ESTILOS (Súper Visual y para PDF)
# ==========================================
st.set_page_config(page_title="Simulador de Creación Cosmética", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    /* Estilos generales */
    .stApp { background-color: #f9fbfd; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    h1, h2, h3 { color: #002b5e !important; }
    
    /* Cajas de diseño */
    .brand-preview { padding: 30px; border-radius: 15px; text-align: center; margin-top: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); transition: all 0.3s ease; border: 2px solid transparent;}
    .example-box { background-color: #e8f4f8; border-left: 4px solid #3498db; padding: 10px; font-size: 0.9em; margin-bottom: 15px; border-radius: 4px; color: #555; }
    .card-foda { padding: 15px; border-radius: 8px; color: white; margin-bottom: 10px; font-weight: bold; text-align: center; }
    .metric-card { background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center; border-top: 4px solid #f2a900; margin-bottom: 10px;}
    .formula-box { font-size: 1.1rem; padding: 15px; background-color: #f1f8e9; border-radius: 8px; color: #1b5e20; font-family: monospace; font-weight: bold; text-align: center; border: 1px dashed #1b5e20; margin-bottom: 15px;}
    
    /* Colores FODA */
    .bg-fortaleza { background-color: #27ae60; }
    .bg-debilidad { background-color: #e74c3c; }
    .bg-oportunidad { background-color: #2980b9; }
    .bg-amenaza { background-color: #8e44ad; }

    /* Estilos para ocultar elementos al imprimir a PDF */
    @media print {
        header, .stSidebar, .stTabs [data-baseweb="tab-list"], button { display: none !important; }
        .stApp { background-color: white !important; padding: 0 !important; margin: 0 !important;}
        .brand-preview, .metric-card { box-shadow: none !important; border: 1px solid #ccc !important; }
        .stTabs [data-baseweb="tab-panel"] { border: none !important; padding: 0 !important; margin: 0 !important;}
        * { -webkit-print-color-adjust: exact !important; color-adjust: exact !important; }
        div[data-testid="stColorPicker"] { display: none !important; }
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. ENCABEZADO Y BOTÓN DE PDF (Inyección JS)
# ==========================================
col_header, col_print = st.columns([4, 1])
with col_header:
    st.markdown("<h1>✨ Simulador Integral: Creación de Empresa Cosmética</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #7f8c8d; font-size: 1.2em;'>De la Planeación FODA a la Estructura Organizacional y el Marco Legal.</p>", unsafe_allow_html=True)
with col_print:
    st.components.v1.html("""
        <button onclick="window.print()" style="background-color: #002b5e; color: white; border: none; padding: 12px 20px; border-radius: 8px; font-weight: bold; cursor: pointer; width: 100%; box-shadow: 0 4px 6px rgba(0,0,0,0.1); font-size: 1rem;">🖨️ Descargar Proyecto (PDF)</button>
    """, height=60)

st.markdown("---")

# ==========================================
# 3. DATOS MAESTROS (Ejemplos, Psicología de Color, Iconos)
# ==========================================
psicologia_color = {
    "🔵 Azul": "Confianza, Calma, Profesionalismo, Higiene. (Usado en dermocosmética clínica).",
    "🟢 Verde": "Naturaleza, Frescura, Orgánico, Sostenibilidad. (Usado en cosmética natural).",
    "⚪ Blanco": "Pureza, Limpieza, Minimalismo, Lujo. (Usado en marcas premium o minimalistas).",
    "🟡 Dorado/Amarillo": "Prestigio, Lujo, Energía, Innovación. (Usado en líneas anti-edad de alta gama).",
    "⚫ Negro": "Elegancia, Poder, Formalidad, Misterio. (Usado en líneas masculinas o premium de noche).",
    "🟣 Violeta": "Sabiduría, Creatividad, Espiritualidad, Lujo Alternativo.",
    "🟠 Naranja/Rosa": "Entusiasmo, Juventud, Creatividad, Diversión. (Usado en productos para piel joven o maquillaje)."
}

iconos_disponibles = {
    "Acción y Rapidez": "⚡🚀💨",
    "Naturaleza y Botánica": "🌿💧🍂🌸",
    "Medios y Comunicación": "📱📣🌐🎥",
    "Religión/Importancia": "🕯️🏛️✨",
    "Ciencia y Clínica": "🧪🔬🎓🩺",
    "Belleza y Cuidado": "🧖‍♀️🧴💖💎"
}

base_datos_manuales = {
    "Cosmetóloga / Cosmiatra Principal": {
        "reporta_a": "Director Médico / Gerente de Cabina", "supervisa_a": "Auxiliares, practicantes.",
        "funciones": ["Realizar diagnósticos faciales y corporales.", "Ejecutar tratamientos con aparatología avanzada.", "Mantener la bioseguridad en cabina.", "Registrar expedientes y Consentimientos Informados."]
    },
    "Director Médico (Responsable Sanitario)": {
        "reporta_a": "Dirección General / Dueños", "supervisa_a": "Todo el personal clínico e instrumental.",
        "funciones": ["Firmar y mantener actualizado el Aviso de Funcionamiento ante COFEPRIS.", "Avalar y aprobar protocolos invasivos o aparatología médica.", "Capacitar en bioseguridad y manejo de residuos peligrosos (RPBI).", "Atender reacciones adversas graves."]
    },
    "Gerente de Recepción y Ventas": {
        "reporta_a": "Dirección General", "supervisa_a": "Recepcionistas, asistentes.",
        "funciones": ["Gestionar la agenda y confirmación de citas.", "Cierre de ventas de paquetes y membresías.", "Manejo de CRM y cobros/facturación.", "Garantizar la excelente primera impresión de la clínica."]
    }
}

# ==========================================
# 4. TABS PRINCIPALES (RECONSTRUIDOS)
# ==========================================
tab_planeacion, tab_producto, tab_marketing, tab_finanzas, tab_organizacion, tab_legal = st.tabs([
    "🎯 1. Planeación Estratégica", 
    "🧪 2. El Producto (Receta y Etiqueta)", 
    "📊 3. Estrategia 4P", 
    "📈 4. Costeo y Finanzas Avanzadas", 
    "🏢 5. Organización y Estructura",
    "⚖️ 6. Marco Legal (COFEPRIS)"
])

# ------------------------------------------
# TAB 1: PLANEACIÓN ESTRATÉGICA (FODA y PESTEL restaurados)
# ------------------------------------------
with tab_planeacion:
    st.markdown("### Identidad Filosófica y Planeación")
    
    col_texto, col_visual = st.columns([3, 2])
    
    with col_texto:
        nombre_marca = st.text_input("Nombre de la Marca / Empresa:", placeholder="Tu Marca Estética Aquí")
        
        st.markdown("<div class='example-box'><b>Ejemplo Misión:</b> Potenciar la salud cutánea de nuestros clientes mediante dermocosmética de base científica, ofreciendo fórmulas de alta eficacia comprobada.</div>", unsafe_allow_html=True)
        mision = st.text_area("Misión:")
        
        st.markdown("<div class='example-box'><b>Ejemplo Visión:</b> Posicionarnos para el 2030 como la marca líder en dermatología sustentable en el centro de México, expandiendo nuestra línea a tratamientos clínicos.</div>", unsafe_allow_html=True)
        vision = st.text_area("Visión:")

    with col_visual:
        st.markdown("#### Psicología del Color y Marca")
        st.write("Selecciona los colores que definen la personalidad de tu marca (usa la guía).")
        color_primario = st.color_picker("Color Principal (Fondo):", "#002b5e")
        color_secundario = st.color_picker("Color Secundario (Acentos/Texto):", "#f2a900")
        
        guia_color = st.selectbox("📖 Guía Rápida de Psicología del Color:", list(psicologia_color.values()))
        
        # Previsualización dinámica de la marca
        st.markdown(f"""
        <div class='brand-preview' style='background-color: {color_primario}; border: 3px solid {color_secundario};'>
            <h1 style='color: {color_secundario}; font-family: "Didot", serif; margin: 0; padding-bottom: 5px;'>{nombre_marca if nombre_marca else "TU MARCA AQUÍ"}</h1>
            <p style='color: white; font-size: 0.9em; font-style: italic; margin-top: 5px;'>Dermocosmética Avanzada</p>
            <div style='background-color: white; height: 3px; width: 50%; margin: 0 auto; border-radius: 2px;'></div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # RESTAURACIÓN DEL FODA INTERACTIVO
    st.markdown("### 1.1 Análisis FODA")
    st.write("Identifica los factores internos y externos antes de lanzar el producto.")
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.markdown("<div class='card-foda bg-fortaleza'><b>Fortalezas (Interno)</b></div>", unsafe_allow_html=True)
        fortalezas = st.text_area("¿Qué ventajas competitivas, patentes o activos tienes?", height=100)
        
        st.markdown("<div class='card-foda bg-oportunidad'><b>Oportunidades (Externo)</b></div>", unsafe_allow_html=True)
        oportunidades = st.text_area("¿Qué tendencias de mercado (ej. cosmética vegana) puedes aprovechar?", height=100)
    with col_f2:
        st.markdown("<div class='card-foda bg-debilidad'><b>Debilidades (Interno)</b></div>", unsafe_allow_html=True)
        debilidades = st.text_area("¿Qué te falta? (ej. falta de capital, personal sin capacitar)", height=100)
        
        st.markdown("<div class='card-foda bg-amenaza'><b>Amenazas (Externo)</b></div>", unsafe_allow_html=True)
        amenazas = st.text_area("Inflación, nuevas leyes de COFEPRIS, competencia agresiva.", height=100)

    st.markdown("---")
    
    # RESTAURACIÓN DEL PESTEL (Estructurado)
    st.markdown("### 1.2 Análisis PESTEL")
    st.write("Evalúa los factores macroambientales externos.")
    
    c_p1, c_p2 = st.columns(2)
    with c_p1:
        politico = st.text_area("👮‍♂️ Político: Estabilidad del país, políticas comerciales.")
        economico = st.text_area("📉 Económico: Tasa de interés, inflación, poder adquisitivo.")
        social = st.text_area("👥 Social: Tendencias de cuidado facial, edad de la población.")
    with c_p2:
        tecnologico = st.text_area("⚙️ Tecnológico: Nuevos ingredientes activos, biotecnología.")
        ecologico = st.text_area("🌿 Ecológico (Sustentable): Regulaciones de empaque, Cruelty-Free.")
        legal = st.text_area("⚖️ Legal: Regulaciones generales, leyes de publicidad.")

# ------------------------------------------
# TAB 2: EL PRODUCTO (Explicación, Receta y Etiqueta)
# ------------------------------------------
with tab_producto:
    st.markdown("### 🧪 El Corazón Cosmético")
    
    # Explicación del Proceso
    st.markdown("""
    <div style='background-color: #f1f8e9; padding: 20px; border-radius: 10px; border-left: 5px solid #2e7d32; margin-bottom: 20px;'>
        <h4>¿Cómo funciona la creación de un cosmético?</h4>
        <p>Un cosmético no se "inventa", se **formula**. Este proceso combina química, dermatología y bioética para crear una emulsión estabilizada que entregue principios activos a la piel de forma segura. El proceso consta de:</p>
        <ol>
            <li><b>Investigación y Desarrollo (I+D):</b> Detección de una necesidad cutánea (ej. seborregulación en piel acnéica).</li>
            <li><b>Formulación INCI:</b> Creación de la "receta" usando nomenclatura internacional. El <b>70-90% suele ser la base</b> (agua/aceite), y el <b>1-5% son los Principios Activos</b> que hacen el trabajo real.</li>
            <li><b>Pruebas de Estabilidad y Bioseguridad:</b> Garantizar que el producto no se eche a perder y no cause reacciones alérgicas.</li>
            <li><b>Etiquetado INCI:</b> Listar los ingredientes de **mayor a menor** concentración.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

    # Tabla de Formulación Interactiva (INCI)
    st.markdown("#### 2.1 Tabla de Formulación (Receta)")
    st.write("Estructura la base, los activos y los aditivos de tu producto estrella.")
    
    df_inci = pd.DataFrame(
        [
            {"Nomenclatura INCI": "Aqua", "Función": "Solvente (Fase Acuosa)", "Porcentaje (%)": 70.0},
            {"Nomenclatura INCI": "Glycerin", "Función": "Humectante", "Porcentaje (%)": 5.0},
            {"Nomenclatura INCI": "Niacinamide", "Función": "Principio Activo (Dermocosmética)", "Porcentaje (%)": 4.0},
            {"Nomenclatura INCI": "Cetearyl Alcohol", "Función": "Emulsionante", "Porcentaje (%)": 6.0},
            {"Nomenclatura INCI": "Simmondsia Chinensis Seed Oil", "Función": "Emoliente (Fase Oleosa)", "Porcentaje (%)": 14.0},
            {"Nomenclatura INCI": "Phenoxyethanol", "Función": "Conservador", "Porcentaje (%)": 1.0},
        ]
    )
    receta_editada = st.data_editor(df_inci, num_rows="dynamic", use_container_width=True)
    
    total_pct = receta_editada["Porcentaje (%)"].sum()
    if total_pct == 100.0:
        st.success(f"✅ Fórmula estabilizada y balanceada. Total: {total_pct}%")
    else:
        st.error(f"⚠️ Error de formulación: El porcentaje total debe sumar exactamente 100%. Actual: {total_pct}%")

    st.markdown("---")
    
    # DISEÑADOR DE ETIQUETA INTERACTIVO
    st.markdown("### 🛠️ 2.2 Diseñador de Etiqueta Frontal")
    st.write("Selecciona los iconos visuales que comunican la acción de tu producto.")
    
    c_e1, c_e2 = st.columns([1, 1])
    with c_e1:
        # Selección de iconos/emojis (RESTAURO LO SOLICITADO)
        iconos_sel = st.multiselect("Selecciona los iconos que comunican el mensaje:", 
                                    list(iconos_disponibles.values()),
                                    format_func=lambda x: f"{[k for k, v in iconos_disponibles.items() if v == x][0]}: {x}")
        
        iconos_combinados = "".join(iconos_sel)
        volumen_neto = st.number_input("Volumen Neto (ml):", value=50)

    with c_e2:
        # Previsualización dinámica de la etiqueta (Integrando colores de marca e iconos)
        st.markdown(f"""
        <div style='background-color: white; color: {color_primario}; padding: 30px; border-radius: 5px; border: 2px solid {color_primario}; text-align: center; font-family: sans-serif;'>
            <h4 style='color: {color_primario}; font-family: Didot, serif; margin: 0;'>{nombre_marca if nombre_marca else "TU MARCA AQUÍ"}</h4>
            <div style='background-color: {color_primario}; height: 2px; width: 30%; margin: 5px auto;'></div>
            <p style='font-size: 1.1em; color: {color_primario}; margin-bottom: 5px;'>Sérum Regenerador</p>
            <h2 style='color: {color_secundario}; font-size: 2.5em; margin: 10px 0;'>{iconos_combinados if iconos_combinados else "🧩🧩"}</h2>
            <p style='color: gray; font-size: 0.8em; margin-top: 5px;'>Activos: Niacinamide 4%</p>
            <p style='font-weight: bold; margin-top: 15px;'>CONTENIDO NETO: {volumen_neto} ml</p>
        </div>
        """, unsafe_allow_html=True)

# ------------------------------------------
# TAB 3: MERCADOTECNIA 4P'S (Con ejemplos)
# ------------------------------------------
with tab_marketing:
    st.markdown("### Estrategia de Mix de Marketing (Mix 4P)")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown("<div class='example-box'><b>Ejemplo Producto:</b> Crema facial ligera en envase airless de 50ml, textura mate, libre de parabenos y con sello Cruelty-Free.</div>", unsafe_allow_html=True)
        producto_4p = st.text_area("📦 Producto (Atributos, empaque, beneficio):")
        
        st.markdown("<div class='example-box'><b>Ejemplo Plaza:</b> Venta directa en cabina (30%) y tienda online propia con envíos nacionales por FedEx (70%).</div>", unsafe_allow_html=True)
        plaza_4p = st.text_area("📍 Plaza (Canales de distribución y venta):")
        
    with col_p2:
        st.markdown("<div class='example-box'><b>Ejemplo Promoción:</b> Campañas de conversión en Meta Ads, micro-influencers de Skincare en TikTok y demostración gratuita en cabina.</div>", unsafe_allow_html=True)
        promocion_4p = st.text_area("📣 Promoción (Publicidad, RRPP, redes sociales):")
        
        st.markdown("<div class='example-box'><b>Ejemplo Estrategia Precio:</b> 'Prestige Pricing'. Precio alto para denotar calidad premium y diferenciación científica ante marcas de supermercado.</div>", unsafe_allow_html=True)
        estrategia_precio_4p = st.text_area("💵 Estrategia de Precio (Psicología detrás del cobro):")

# ------------------------------------------
# TAB 4: COSTEO Y FINANZAS AVANZADAS (RECONSTRUIDO CON 6 COLUMNAS)
# ------------------------------------------
with tab_finanzas:
    st.markdown("### Estructura Financiera Avanzada")
    
    # 4.1 Costos Fijos Mensuales (RESTAURADO CON 6 COLUMNAS SOLICITADAS)
    st.markdown("#### 4.1 Determinación de Costos Fijos Mensuales (CF)")
    
    # Uso un data_editor para permitir 6 líneas de costos fijos con nombre y monto
    df_cf = pd.DataFrame([
        {"Nombre del Costo Fijo": "Renta de Local / Cabina", "Monto ($)": 8000.0},
        {"Nombre del Costo Fijo": "Sueldos Base (Dueño/Personal)", "Monto ($)": 15000.0},
        {"Nombre del Costo Fijo": "Servicios (Luz, Agua, Internet)", "Monto ($)": 2500.0},
        {"Nombre del Costo Fijo": "Publicidad y Marketing Fijo", "Monto ($)": 4000.0},
        {"Nombre del Costo Fijo": "Suscipciones/Software/CRM", "Monto ($)": 800.0},
        {"Nombre del Costo Fijo": "Mantenimiento / Seguros", "Monto ($)": 1200.0}
    ])
    cf_editado = st.data_editor(df_cf, num_rows="dynamic", use_container_width=True, key="df_cf")
    total_cf = cf_editado["Monto ($)"].sum()
    st.markdown(f"<h4 style='color: #c0392b;'>Total CF Mensual: ${total_cf:,.2f}</h4>", unsafe_allow_html=True)

    st.markdown("---")
    
    # 4.2 Costos Variables (RESTAURADO CON 6 COLUMNAS SOLICITADAS)
    st.markdown("#### 4.2 Determinación de Costos Variables por Unidad (CVu)")
    st.write("Ingresa los costos variables específicos para fabricar UNA unidad del producto estrella.")
    
    # Uso un data_editor para permitir 6 líneas de costos variables con nombre y monto
    df_cv = pd.DataFrame([
        {"Nombre del Costo Variable": "Materia Prima INCI total", "Monto ($)": 65.0},
        {"Nombre del Costo Variable": "Envase Primario (Tarro/Frasco)", "Monto ($)": 22.0},
        {"Nombre del Costo Variable": "Empaque Secundario (Caja)", "Monto ($)": 14.0},
        {"Nombre del Costo Variable": "Etiqueta y Loteado", "Monto ($)": 5.0},
        {"Nombre del Costo Variable": "Logística/Envío por unidad", "Monto ($)": 0.0},
        {"Nombre del Costo Variable": "Comisión Pasarela de Venta/CRM", "Monto ($)": 18.0}
    ])
    cv_editado = st.data_editor(df_cv, num_rows="dynamic", use_container_width=True, key="df_cv")
    total_cv_unitario = cv_editado["Monto ($)"].sum()
    st.markdown(f"<h4 style='color: #2980b9;'>Total CVu por Unidad: ${total_cv_unitario:,.2f}</h4>", unsafe_allow_html=True)

    st.markdown("---")
    
    # 4.3 FIJACIÓN DE PRECIO Y PROYECCIÓN FINANCIERA (RECONSTRUIDO SOLICITADO)
    st.markdown("#### 4.3 Proyección de Rentabilidad")
    
    col_proj1, col_proj2, col_proj3 = st.columns(3)
    
    with col_proj1:
        # Fijar precio a partir del margen de ganancia (Markup) sobre el CVu
        margen_deseado = st.number_input("Margen de Ganancia sobre Costo Variable (%):", value=65.0, step=5.0)
        precio_sugerido = total_cv_unitario + (total_cv_unitario * (margen_deseado / 100))
        st.success(f"🏷️ **Precio de Venta Sugerido:** ${precio_sugerido:,.2f}")
        
        # Override opcional del alumno (su decisión final)
        precio_real = st.number_input("💵 Precio Final de Venta (Tu Decisión):", value=precio_sugerido)

    with col_proj2:
        # Controlar unidades producidas vs vendidas
        unidades_producidas = st.number_input("Unidades PRODUCIDAS al Mes:", value=600, step=50)
        unidades_vendidas = st.number_input("Unidades VENDIDAS al Mes:", value=400, step=50)
        
        if unidades_vendidas > unidades_producidas:
            st.warning("⚠️ No puedes vender más de lo que produces. Ajusta las cifras.")

    with col_proj3:
        # CÁLCULOS SOLICITADOS (Ingresos, Ganancias, Punto de Equilibrio)
        ingresos_totales = unidades_vendidas * precio_real
        
        # El costo de producción se basa en lo producido, no lo vendido
        costo_produccion_total = unidades_producidas * total_cv_unitario
        utilidad_bruta = (unidades_vendidas * precio_real) - (unidades_vendidas * total_cv_unitario)
        
        gastos_totales_reales = total_cf + costo_produccion_total
        utilidad_neta_mensual = ingresos_totales - gastos_totales_reales
        
        try:
            punto_equilibrio_unidades = total_cf / (precio_real - total_cv_unitario)
        except ZeroDivisionError: punto_equilibrio_unidades = 0
            
        st.markdown(f"<div class='metric-card'><h4>Ingresos Totales</h4><h2>${ingresos_totales:,.2f}</h2></div>", unsafe_allow_html=True)

    col_res1, col_res2 = st.columns(2)
    with col_res1:
        color_utilidad = "#27ae60" if utilidad_neta_mensual >= 0 else "#e74c3c"
        st.markdown(f"<div class='metric-card'><h4>Utilidad Neta (Ganancia Final)</h4><h2 style='color: {color_utilidad};'>${utilidad_neta_mensual:,.2f}</h2></div>", unsafe_allow_html=True)
    with col_res2:
        st.markdown(f"<div class='metric-card'><h4>Punto de Equilibrio</h4><h2>{int(punto_equilibrio_unidades) + 1} unidades</h2><p style='color: gray; font-size: 0.8em;'>Para cubrir fijos y variables sin perder dinero.</p></div>", unsafe_allow_html=True)

# ------------------------------------------
# TAB 5: ORGANIZACIÓN (Organigrama y Manuales RESTAURADOS)
# ------------------------------------------
with tab_organizacion:
    st.markdown("### Estructura Organizacional y Jerárquica")
    
    # Organigrama Dinámico (HTML/CSS)
    st.markdown("#### 5.1 Organigrama (Jerarquía Operativa)")
    st.write("Esta estructura garantiza que los especialistas sean dirigidos por expertos sanitarios.")
    
    st.components.v1.html(f"""
    <style>
        .tree ul {{ padding-top: 20px; position: relative; transition: all 0.5s; }}
        .tree li {{ float: left; text-align: center; list-style-type: none; position: relative; padding: 20px 5px 0 5px; transition: all 0.5s; }}
        .tree li::before, .tree li::after {{ content: ''; position: absolute; top: 0; right: 50%; border-top: 2px solid #002b5e; width: 50%; height: 20px; }}
        .tree li::after {{ right: auto; left: 50%; border-left: 2px solid #002b5e; }}
        .tree li:only-child::after, .tree li:only-child::before {{ display: none; }}
        .tree li:only-child {{ padding-top: 0; }}
        .tree li:first-child::before, .tree li:last-child::after {{ border: 0 none; }}
        .tree li:last-child::before {{ border-right: 2px solid #002b5e; border-radius: 0 5px 0 0; }}
        .tree li:first-child::after {{ border-radius: 5px 0 0 0; }}
        .tree ul ul::before {{ content: ''; position: absolute; top: 0; left: 50%; border-left: 2px solid #002b5e; width: 0; height: 20px; }}
        .tree li div {{ border: 2px solid #002b5e; padding: 10px; border-radius: 8px; color: #002b5e; font-weight: bold; background-color: white; }}
        .tree li .med {{ border: 2px solid #e74c3c; color: #e74c3c; }}
        .tree li .ven {{ border: 2px solid #27ae60; color: #27ae60; }}
    </style>
    <div class="tree" style="display: flex; justify-content: center;">
        <ul>
            <li>
                <div>Dirección General (Tú)</div>
                <ul>
                    <li>
                        <div class="med">Director Médico / Resp. Sanitario</div>
                        <ul>
                            <li><div>Cosmetóloga A</div></li>
                            <li><div>Cosmetóloga B</div></li>
                        </ul>
                    </li>
                    <li>
                        <div class="ven">Gerente Ventas / Recepción</div>
                        <ul>
                            <li><div>Recepcionista A</div></li>
                            <li><div>Recepcionista B</div></li>
                        </ul>
                    </li>
                </ul>
            </li>
        </ul>
    </div>
    """, height=350)

    st.markdown("---")
    
    # MANUALES DE PUESTOS (RESTAURADOS SOLICITADO)
    st.markdown("#### 5.2 Constructor de Manual de Puestos y Funciones")
    puesto_sel = st.selectbox("Selecciona un perfil para consultar su manual técnico:", list(base_datos_manuales.keys()))
    
    datos_puesto = base_datos_manuales[puesto_sel]
    st.markdown(f"<div class='metric-card' style='border-top: 4px solid #002b5e;'><h4>Puesto: {puesto_sel}</h4>", unsafe_allow_html=True)
    
    st.markdown(f"**⬅️ Le reporta a:** {datos_puesto['reporta_a']}")
    st.markdown(f"**➡️ Supervisa a:** {datos_puesto['supervisa_a']}")
    st.markdown("<br>**📋 Funciones Específicas (Manual de Operaciones):**", unsafe_allow_html=True)
    for func in datos_puesto['funciones']:
        st.markdown(f"- {func}")
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------------------
# TAB 6: MARCO LEGAL (COFEPRIS Redactable)
# ------------------------------------------
with tab_legal:
    st.markdown("### ⚖️ Marco Legal y Regulatorio (COFEPRIS)")
    st.write("Elabora la documentación crítica para la comercialización.")
    
    # ESPACIO PARA REDACTAR EL AVISO (RESTAURO SOLICITADO, QUITANDO PESTEL)
    st.markdown("#### 6.1 Aviso de Funcionamiento para la Comercialización")
    st.write("Redacta un borrador del Aviso de Funcionamiento según el formato oficial de COFEPRIS para la venta de productos cosméticos (Clave SCIAN 464112).")
    
    st.markdown("""
    <div class='example-box'>
    <b>Guía de Redacción:</b> El Aviso debe contener: Datos del propietario (RFC, domicilio), Datos del establecimiento (Nombre, clave SCIAN 464112 'Comercio al por menor de cosméticos y artículos de tocador'), Datos del Responsable Sanitario (si aplica por aparatología), y la fecha de inicio de operaciones.
    </div>
    """, unsafe_allow_html=True)
    
    borrador_aviso = st.text_area("✍️ Redacción del borrador del Aviso de Funcionamiento (COFEPRIS):", height=200)

    st.markdown("---")
    
    # CASO ÉTICO/LEGAL (RESTAURO SOLICITADO)
    st.markdown("#### 6.2 Dilema Ético / Regulatorio: 'Aceite para Barba Detox Extremo'")
    st.write("Análisis del caso COFEPRIS y producto milagro.")
    
    st.markdown("""
    <div style="background-color: #fcf3cf; padding: 20px; border-radius: 10px; border-left: 5px solid #f1c40f;">
    <h4 style="color: black; margin-top: 0;">El Conflicto:</h4>
    <p>Tu empresa lanzó el <i>"Aceite Terapéutico para Barba Detox Extremo"</i>. Contiene aceites de menta y eucalipto.</p>
    <p>La publicidad dice: <b>"El único aceite que cura la dermatitis facial, acelera el crecimiento en 3 días y elimina toxinas de la sangre."</b>.</p>
    <p>COFEPRIS inmoviliza el producto en la aduana por sospecha de 'Producto Frontera' (Producto Milagro).</p>
    </div>
    """, unsafe_allow_html=True)
    
    q_legal_1 = st.text_area("1. Análisis INCI y Etiqueta: ¿Qué afirmaciones de la publicidad están prohibidas para un cosmético según el reglamento y por qué?")
    q_legal_2 = st.text_area("2. Estrategia de Resolución Legal: ¿Cómo debes corregir la etiqueta y la estrategia de marketing para liberar el producto?")
