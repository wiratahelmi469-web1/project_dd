import streamlit as st
import Database
import Dashboard
import Input_data
import analisis_penjualan
import Dokumentasi

st.set_page_config(
    page_title="Manajemen UMKM",
    layout="wide"
)

# CSS
st.markdown("""
<style>
[data-testid="stSidebar"]{
    background-color:#ffcda5;
}
[data-testid="stHeader"]{
    background-color:#ffcda5;
}
h1,h2,h3{
    color: bold !important;
}
p{
    font-size: 20px !important;            
}
.card {
    background-color: #ffffff !important;
    padding: 20px !important;
    border-radius: 12px !important;
    box-shadow: 0 4px 8px rgba(0,0,0,0.08) !important;
    margin-bottom: 16px !important;
}
[data-testid="stAppViewContainer"] {
    background-color: #F9FAFB;
}

/* ===== SIDEBAR ===== */
[data-testid="stSidebar"] {
    background-color: #FFE1C4 !important;
    padding-top: 20px !important;
}

/* ===== CARD STYLE ===== */
.card {
    background-color: #FFFFFF !important;
    padding: 20px !important;
    border-radius: 14px !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08) !important;
    margin-bottom: 20px !important;
}

/* ===== METRIC ===== */
[data-testid="metric-container"] {
    background-color: #FFFFFF !important;
    border-radius: 14px !important;
    padding: 18px !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08) !important;
}

[data-testid="metric-container"] > div {
    font-size: 18px !important;
}

/* ===== BUTTON ===== */
button[kind="primary"] {
    background-color: #FF8C42 !important;
    border-radius: 10px !important;
    border: none !important;
}

button:hover {
    opacity: 0.9 !important;
}

/* ===== TABLE ===== */
[data-testid="stDataFrame"] {
    background-color: white !important;
    border-radius: 12px !important;
    padding: 10px !important;
}

/* ===== DIVIDER ===== */
hr {
    border-top: 2px solid #FFE1C4 !important;
}

/* ===== FOOTER SAFE SPACE ===== */
footer {
    visibility: hidden !important;
}
</style>
""", unsafe_allow_html=True)

# INIT DATA
if "data" not in st.session_state:
    st.session_state.data = Database.load_data()

menu = st.sidebar.radio(
    "Menu",
    ["Dashboard", "Input Data", "Database", "Analisis Penjualan", "Dokumentasi"]
)

df = st.session_state.data

def footer():
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #FFE8D7;
            color: #000;
            text-align: center;
            padding: 8px;
            font-size: 14px;
            z-index: 999;
        }
        </style>

        <div class="footer">
            © 2025 | Aplikasi Manajemen UMKM | UAS DDP
        </div>
        """,
        unsafe_allow_html=True
    )

with st.sidebar:
    st.divider()
    st.caption("© 2025 Manajemen UMKM")


if menu == "Dashboard":
    Dashboard.show(df)
elif menu == "Input Data":
    Input_data.show(df)
elif menu == "Database":
    Database.show(df)
elif menu == "Analisis Penjualan":
    analisis_penjualan.show(df)
elif menu == "Dokumentasi":
    Dokumentasi.show()
footer()
