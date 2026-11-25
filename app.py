from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Chapitre 3 : Concentration et solutions électrolytiques",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Masque l'interface Streamlit et fixe l'iframe exactement à l'écran (iOS, Android, Mac, Windows)
st.markdown(
    """
    <style>
        #MainMenu, header, footer,
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        [data-testid="stHeader"],
        [data-testid="collapsedControl"],
        section[data-testid="stSidebar"] {
            display: none !important;
            visibility: hidden !important;
        }
        html, body,
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"],
        [data-testid="stMainBlockContainer"],
        .main, .block-container {
            margin: 0 !important;
            padding: 0 !important;
            max-width: 100% !important;
            width: 100% !important;
            height: 100% !important;
            overflow: hidden !important;
            background: #eef2f6 !important;
        }
        [data-testid="stElementContainer"],
        [data-testid="stIFrame"],
        .element-container {
            margin: 0 !important;
            padding: 0 !important;
            width: 100% !important;
            height: 100% !important;
        }
        iframe {
            position: fixed !important;
            top: 0 !important;
            right: 0 !important;
            bottom: 0 !important;
            left: 0 !important;
            width: 100% !important;
            height: 100% !important;
            min-height: 100% !important;
            border: none !important;
            display: block !important;
            background: #eef2f6 !important;
            z-index: 9999 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "simulation.html"

if not html_path.exists():
    st.error("Fichier simulation.html introuvable dans le même dossier que app.py.")
else:
    html_content = html_path.read_text(encoding="utf-8")
    # scrolling=True garantit un repli tactile même sur les très anciens iOS/WebViews
    components.html(html_content, height=800, scrolling=True)
