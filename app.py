import streamlit as st
import urllib.parse
from embajadores import embajadores

# Configuración general
st.set_page_config(page_title="Sumate como socio aportante", layout="wide")

# Leer parámetro de la URL
query_params = st.query_params
embajador_key = query_params.get("embajador", "general")
data = embajadores.get(embajador_key, embajadores["general"])

# Estilos CSS personalizados
st.markdown(f"""
    <style>
        body {{
            background-color: #237d33;
        }}
        .main-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 2rem;
            color: white;
        }}
        .mensaje-central {{
            font-size: 1.6rem;
            font-weight: bold;
            margin: 2rem 0;
            color: white;
        }}
        .img-container {{
            position: relative;
            width: 100%;
            max-width: 600px;
            margin: 0 auto 2rem auto;
        }}
        .img-container img {{
            width: 100%;
            border-radius: 12px;
            filter: brightness(0.6);
        }}
        .botones-container {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 1rem;
            margin: 2rem 0;
        }}
        .donar-btn {{
            background-color: #fbca0c;
            color: black;
            border: none;
            padding: 1rem 2rem;
            font-size: 1.2rem;
            border-radius: 8px;
            text-decoration: none;
            display: inline-block;
            width: 150px;
            font-weight: bold;
        }}
        .donar-btn:hover {{
            background-color: #f8ba00;
        }}
        .testimonio {{
            font-style: italic;
            margin: 1.5rem 0;
            color: white;
            font-size: 1.1rem;
        }}
        .footer {{
            margin-top: 3rem;
            text-align: center;
            color: white;
            font-size: 0.9rem;
        }}
        .logo {{
            width: 120px;
            margin-bottom: 1rem;
        }}
        @media (max-width: 768px) {{
            .botones-container {{
                flex-direction: column;
                align-items: center;
            }}
            .donar-btn {{
                width: 80%;
            }}
        }}
    </style>
""", unsafe_allow_html=True)

# --- CONTENIDO ---

st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Logo superior
st.image("logovrc.png", width=120)

# Mensaje central
st.markdown('<div class="mensaje-central">Cada chico que está en el club es gracias a alguien que apostó por este sueño. Vos podés ser ese alguien.</div>', unsafe_allow_html=True)

# Imagen principal con filtro oscuro
st.markdown(f"""
    <div class="img-container">
        <img src="{data['imagen']}" alt="Imagen de campaña">
    </div>
""", unsafe_allow_html=True)

# Botones de donación
st.markdown('<div class="botones-container">', unsafe_allow_html=True)
st.markdown(f'<a class="donar-btn" href="{data["links"]["20000"]}" target="_blank">$20.000</a>', unsafe_allow_html=True)
st.markdown(f'<a class="donar-btn" href="{data["links"]["40000"]}" target="_blank">$40.000</a>', unsafe_allow_html=True)
st.markdown(f'<a class="donar-btn" href="{data["links"]["60000"]}" target="_blank">$60.000</a>', unsafe_allow_html=True)
st.markdown(f'<a class="donar-btn" href="{data["links"]["libre"]}" target="_blank">Monto libre</a>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Testimonio
st.markdown('<div class="testimonio">“Más de 600 chicos entrenan y estudian en el club gracias al aporte de personas como vos.”</div>', unsafe_allow_html=True)

# Logo inferior
st.image("logovrc.png", width=120)

# Footer
st.markdown('<div class="footer">El link redirige al sitio de donación segura a través de Mercado Pago. Podés cancelarla cuando quieras.</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
