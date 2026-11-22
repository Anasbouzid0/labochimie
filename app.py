from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

# Configuration plein écran de la page Streamlit
st.set_page_config(
    page_title="Chapitre 3 : Concentration et solutions électrolytiques",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Suppression complète de l'interface Streamlit et étirement de l'iframe sur tout l'écran
st.markdown(
    """
    <style>
        #MainMenu, header, footer, [data-testid="stToolbar"],
        [data-testid="stDecoration"], [data-testid="stStatusWidget"],
        [data-testid="stHeader"], section[data-testid="stSidebar"] {
            display: none !important;
            visibility: hidden !important;
        }
        html, body, [data-testid="stAppViewContainer"], .main, .block-container {
            margin: 0 !important;
            padding: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            max-width: 100vw !important;
            overflow: hidden !important;
            background: #f1f5f9 !important;
        }
        iframe {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            border: none !important;
            z-index: 99999 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Chargement et affichage du fichier HTML de simulation
html_path = Path(__file__).parent / "simulation.html"

if not html_path.exists():
    st.error(
        f"Fichier introuvable : `{html_path.name}`. "
        "Placez `simulation.html` dans le même dossier que `app.py`."
    )
else:
    html_content = html_path.read_text(encoding="utf-8")
    components.html(html_content, height=900, scrolling=False)
