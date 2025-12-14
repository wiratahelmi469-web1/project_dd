import streamlit as st
import pandas as pd

def show(df):
    st.title("Analisis Penjualan")

    if df.empty:
        st.info("Belum ada data untuk dianalisis")
        return

    # =====================
    # METRIC
    # =====================
    total_omzet = df["Total"].sum()
    rata_transaksi = df["Total"].mean()

    col1, col2 = st.columns(2)
    col1.metric("Total Omzet", f"Rp {total_omzet:,.0f}")
    col2.metric("Rata-rata Transaksi", f"Rp {rata_transaksi:,.0f}")

    # =====================
    # BAR CHART - PRODUK
    # =====================
    st.subheader("Omzet per Produk")

    omzet_produk = (
        df.groupby("Produk")["Total"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(omzet_produk)

    # =====================
    # LINE CHART - TREN WAKTU
    # =====================
    st.subheader("Tren Penjualan Berdasarkan Waktu")

    tren_waktu = (
        df.groupby("Tanggal")["Total"]
        .sum()
        .sort_index()
    )

    st.line_chart(tren_waktu)

    # =====================
    # KESIMPULAN
    # =====================
    produk_terlaris = omzet_produk.idxmax()

    st.subheader("Kesimpulan")
    st.success(
        f"Produk dengan performa penjualan terbaik adalah **{produk_terlaris}**. "
        "Disarankan untuk memprioritaskan stok dan promosi pada produk ini."
    )
