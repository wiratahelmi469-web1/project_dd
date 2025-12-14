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
h1,h2,h3{
    color:orange;
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
