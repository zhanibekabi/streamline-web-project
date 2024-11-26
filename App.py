import streamlit as st
from Pages import Home, DataFrame, Videos, Project3
from streamlit_navigation_bar import st_navbar
import os
from PIL import Image

# Safely load images
try:
    image = Image.open('img/volleyball.png')
    st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)
except FileNotFoundError:
    st.warning("Icon image not found. Using default configuration.")
    st.set_page_config(initial_sidebar_state="collapsed")

# Logo Path
logo_path = os.path.join(os.path.dirname(__file__), "img", "volleyball.svg")
if not os.path.exists(logo_path):
    logo_path = None  # Handle missing logo gracefully

# Pages and Navbar Configuration
pages = ["Home", "DataFrame", "Videos", "Project3"]
styles = {
    "nav": {
        "background": "black",  # Gradient color
        "display": "flex",
        "justify-content": "center",
        "padding": "0px 0",
        "border-radius": "8px",
        "height": "80px",
    },
    "img": {
        "position": "absolute",
        "left": "20px",
        "top": "4px",
        "width": "100px",
        "height": "70px",
    },
    "span": {
        "display": "block",
        "color": "#FFFFFF",
        "padding": "0.5rem 1rem",
        "font-size": "16px",
        "transition": "background 0.3s ease, color 0.3s ease",
    },
    "active": {
        "background-color": "#FFFFFF",
        "color": "black",
        "font-weight": "bold",
        "padding": "14px",
        "border-radius": "4px",
    }
}

options = {
    "show_menu": False,
    "show_sidebar": True,
}

# Navbar Rendering
page = st_navbar(pages, styles=styles, logo_path=logo_path, options=options)

# Page Routing
if page == "Home":
    Home.Home().app()
elif page == "DataFrame":
    DataFrame.DataFrame().app()
elif page == "Videos":
    Videos.Videos().app()
elif page == "Project3":
    Project3.Project3().app()
else:
    st.error("Page not found. Redirecting to Home.")
    Home.Home().app()