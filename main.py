import streamlit as st
from embajadores import embajadores

st.set_page_config(page_title="Socio Solidario · Virreyes Rugby Club", layout="centered")

# Obtener el embajador desde la URL
query_params = st.query_params
embajador_key = query_params.get("embajador", "general")
data = embajadores.get(embajador_key, embajadores["general"])

# Estilo CSS mínimo para botones horizontales uniformes
st.markdown("""
    <style>
        .montos-container {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-top: 2rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }
        .boton-donacion {
            background-color: #237d33;
            color: white;
            padding: 0.8rem 1.6rem;
            font-size: 1.1rem;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            text-decoration: none;
        }
        .boton-donacion:hover {
            background-color: #1b6226;
        }
        .footer {
            font-size: 0.9rem;
            color: #555;
            text-align: center;
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Logo superior
st.image("logovrc.png", width=100)

# Título central
st.markdown("<h1 style='text-align: center;'>SOCIO SOLIDARIO</h1>", unsafe_allow_html=True)

# Mensaje principal
st.markdown(
    """
    <p style='text-align: center; font-size: 1.1rem; margin-top: 1.5rem;'>
    Hacé posible que un joven siga disfrutando del rugby.<br>
    Con tu aporte ayudás a cubrir parte de la cuota de quien hoy no puede afrontarla<br>
    y promovés su formación deportiva y personal.
    </p>
    """,
    unsafe_allow_html=True
)

# Imagen emotiva
st.image(data["imagen"], use_container_width=True)

# Botones de donación
st.markdown("<div class='montos-container'>", unsafe_allow_html=True)
st.markdown(f"<a class='boton-donacion' href='{data['links']['20000']}' target='_blank'>$20.000</a>", unsafe_allow_html=True)
st.markdown(f"<a class='boton-donacion' href='{data['links']['40000']}' target='_blank'>$40.000</a>", unsafe_allow_html=True)
st.markdown(f"<a class='boton-donacion' href='{data['links']['60000']}' target='_blank'>$60.000</a>", unsafe_allow_html=True)
st.markdown(f"<a class='boton-donacion' href='{data['links']['libre']}' target='_blank'>Otro monto</a>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    El link redirige al sitio de donación segura a través de Mercado Pago.<br>
    Podés cancelarla cuando quieras.
</div>
""", unsafe_allow_html=True)

# Gracias
st.caption("Gracias por confiar en lo que hacemos ❤️")
