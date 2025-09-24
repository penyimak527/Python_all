import streamlit as st

st.write("""
         # Selamat Datang di Project 
         Ini adalah website untuk menghitung bunga tunggal
         """);
uang = st.number_input('Masukkan jumlah uang' , 0);
bunga = st.number_input('Masukkan bunga (%)' , 0);
persen = 100
akhir = st.button("hitung");

if(akhir):
    rumus = uang * (bunga / persen)
    total_formatted = f"{round(rumus):,}".replace(",", ".")
    st.success(f"Bunga tunggal berdasarkan 1 tahun adalah Rp {total_formatted}")
    st.balloons();


# audio start
audio_file = open('lemontree.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')

# audio end