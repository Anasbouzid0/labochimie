from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Chapitre 3 : Concentration et solutions électrolytiques",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        #MainMenu, header, footer,
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        [data-testid="stHeader"],
        section[data-testid="stSidebar"] {
            display: none !important;
        }
        html, body, [data-testid="stAppViewContainer"], .main, .block-container {
            margin: 0 !important;
            padding: 0 !important;
            max-width: 100% !important;
            width: 100% !important;
            background: #eef2f6 !important;
        }
        iframe {
            width: 100% !important;
            height: 100dvh !important;
            min-height: 100vh !important;
            border: none !important;
            display: block !important;
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
    components.html(html_content, height=950, scrolling=True)
