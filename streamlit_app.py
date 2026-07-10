import streamlit as st

# ---- CONFIGURATION & STYLING ----
st.set_page_config(page_title="BurgerThing E-Kiosk", page_icon="🍔", layout="wide")

# Custom CSS to mimic a sleek touch-screen kiosk
st.markdown("""
    <style>
    .kiosk-header {
        text-align: center; 
        color: #FF5A00; 
        font-family: 'Arial Black', sans-serif;
        margin-bottom: 20px;
    }
    .price-tag {
        color: #2E7D32;
        font-weight: bold;
        font-size: 1.1rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF5A00;
        color: white;
        font-weight: bold;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #CC4800;
        color: white;
    }
    </style>
""", unsafe_with_html=True)
