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
        body, .stApp {
            background-color: #237d33 !important;
            color: white !important;
        }

        h1, p, div, span {
            color: white !important;
        }

        .montos-container {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-top: 2rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }

        .boton-donacion {
            background-color: #fbca0c;
            color: black !important;
            padding: 0.8rem 1.6rem;
            font-size: 1.1rem;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            text-align: center;
            text-decoration: none !important;
            display: inline-block;
        }

        .boton-donacion:hover {
            background-color: #f1b200;
            color: black !important;
        }

        .footer {
            font-size: 0.9rem;
            color: white;
            text-align: center;
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)



col = st.columns(3)[1]
with col:
    st.image("logovrc.png", width=220)


st.markdown("<h1 style='text-align: center; margin-top: -80px;'>SOCIO SOLIDARIO</h1>", unsafe_allow_html=True)


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

# Mensaje antes de los botones
st.markdown(
    """
    <p style='text-align: center; font-size: 1.1rem; margin-top: 1.5rem;'>
    Quiero ser socio y contribuir mensualmente con la cantidad de:
    </p>
    """,
    unsafe_allow_html=True
)

# Botones de donación
st.markdown(f"""
    <div class='montos-container'>
        <a class='boton-donacion' href='{data["links"]["20000"]}' target='_blank'>$20.000</a>
        <a class='boton-donacion' href='{data["links"]["40000"]}' target='_blank'>$40.000</a>
        <a class='boton-donacion' href='{data["links"]["60000"]}' target='_blank'>$60.000</a>
        <a class='boton-donacion' href='{data["links"]["libre"]}' target='_blank'>Otro monto</a>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    El link redirige al sitio de donación segura a través de Mercado Pago.<br>
    Podés cancelarla cuando quieras.
</div>
""", unsafe_allow_html=True)

# Gracias
st.caption("Gracias por confiar en lo que hacemos")
