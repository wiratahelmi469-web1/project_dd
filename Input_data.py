import streamlit as st
import pandas as pd
from datetime import datetime
from Database import save_data

def show(df):
    st.title("Input Data Penjualan")

    with st.form("form_input"):
        tanggal = st.date_input("Tanggal", datetime.today())
        produk = st.text_input("Nama Produk")
        jumlah = st.number_input("Jumlah", min_value=1, step=1)
        harga = st.number_input("Harga", min_value=0, step=1000)

        submit = st.form_submit_button("Simpan")

        if submit:
            total = jumlah * harga
            data_baru = {
                "Tanggal": pd.to_datetime(tanggal),
                "Produk": produk,
                "Jumlah": jumlah,
                "Harga": harga,
                "Total": total
            }

            df = pd.concat(
                [df, pd.DataFrame([data_baru])],
                ignore_index=True
            )

            save_data(df)
            st.session_state.data = df
            st.success("Data berhasil disimpan")
