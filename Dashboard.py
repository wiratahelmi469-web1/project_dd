import streamlit as st

def show(df):
    st.title("Dashboard UMKM")

    
    total_transaksi = len(df)
    jumlah_produk = df["Produk"].nunique()
    total_omzet = df['Total'].sum() if 'Total' in df.columns else 0

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Transaksi", total_transaksi)
    col2.metric("Jumlah Produk", jumlah_produk)
    col3.metric("Total Omzet", f"Rp {total_omzet:,.0f}")

    st.subheader("Data Terbaru")
    st.dataframe(df.tail(10), use_container_width=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    # reuse the computed total_omzet instead of undefined variable 'a'
    st.metric("Total Omzet (Ringkasan)", f"Rp {total_omzet:,.0f}")
    st.markdown('</div>', unsafe_allow_html=True)
