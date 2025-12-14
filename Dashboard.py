import streamlit as st

def show(df):
    st.title("Dashboard UMKM")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Transaksi", len(df))
    col2.metric("Jumlah Produk", df["Produk"].nunique())
    col3.metric("Total Omzet", f"Rp {df['Total'].sum():,.0f}")

    st.subheader("Data Terbaru")
    st.dataframe(df.tail(10), use_container_width=True)
