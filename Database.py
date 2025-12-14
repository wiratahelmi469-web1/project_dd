import streamlit as st
import pandas as pd
import os

DATA_FILE = "data_penjualan.csv"

def load_data():
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        df["Tanggal"] = pd.to_datetime(df["Tanggal"])
    else:
        df = pd.DataFrame(
            columns=["Tanggal", "Produk", "Jumlah", "Harga", "Total"]
        )
    return df

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

def show(df):
    st.title("Database Penjualan")

    if df.empty:
        st.info("Belum ada data penjualan")
        return

    st.subheader("Proporsi Omzet per Produk")

    chart_data = df.groupby("Produk")["Total"].sum()

    st.bar_chart(chart_data)

    st.subheader("Tabel Database")
    st.dataframe(df, use_container_width=True)
