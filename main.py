import streamlit as st

st.write("""
# Aplikasi Luas Segitiga
Sederhana Menggunakan Streamlit
""")
alas = st.number_input("Masukkan nilai alas",0)
tinggi = st.number_input("Masukkan nilai tinggi",0)
hitung = st.button ("Hitung Luas")

if hitung :
  luas = 0.5*alas*tinggi
  st.write("Luas Segitiga nya =",luas)
