import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Load model dan encoder
try:
    model = joblib.load('model/stress_model.pkl')
    encoder = joblib.load('model/label_encoder.pkl')
except FileNotFoundError:
    st.error("Model atau label encoder tidak ditemukan. Pastikan file berada di folder 'model'.")

# Judul aplikasi
st.title("Prediksi Tingkat Stres Mahasiswa")

# Penjelasan aplikasi
st.markdown("""
    Aplikasi ini akan memprediksi tingkat stres mahasiswa berdasarkan beberapa faktor,
    seperti jam belajar, jam tidur, kegiatan ekstrakurikuler, dan lainnya.
    Silakan masukkan data pribadi Anda di bawah ini untuk melihat prediksi tingkat stres Anda.
""")

# Input data dari pengguna
study_hours = st.slider("Jam Belajar per Minggu", min_value=0, max_value=80, step=1, help="Jumlah jam yang Anda habiskan untuk belajar setiap minggu.")
extracurricular_hours = st.slider("Jam Kegiatan Ekstrakurikuler per Minggu", min_value=0, max_value=30, step=1, help="Jumlah jam untuk kegiatan ekstrakurikuler setiap minggu.")
sleep_hours = st.slider("Jam Tidur per Hari", min_value=0, max_value=24, step=1, help="Rata-rata jam tidur Anda per hari.")
social_hours = st.slider("Jam Kegiatan Sosial per Minggu", min_value=0, max_value=40, step=1, help="Jumlah jam kegiatan sosial per minggu.")
physical_activity_hours = st.slider("Jam Aktivitas Fisik per Minggu", min_value=0, max_value=20, step=1, help="Jumlah jam untuk aktivitas fisik setiap minggu.")
gpa = st.slider("IPK", min_value=0.0, max_value=4.0, step=0.1, help="Masukkan IPK Anda.")

# Menghitung jam kegiatan sosial dan fisik per hari
study_hours = study_hours / 7
physical_activity_hours_per_day = physical_activity_hours / 7

# Prediksi ketika tombol ditekan
if st.button("Prediksi"):
    if 'model' in globals() and 'encoder' in globals():
        # Logika untuk menentukan tingkat stres berdasarkan perbandingan jam kegiatan vs jam tidur
        if study_hours + physical_activity_hours_per_day > sleep_hours:
            stress_level = 'High'
        else:
            stress_level = 'Low'

        # Menampilkan hasil prediksi
        st.success(f"Tingkat Stres Anda: {stress_level}")

        # Visualisasi hasil prediksi
        fig, ax = plt.subplots()
        ax.barh([stress_level], [1], color="skyblue")
        ax.set_xlabel('Prediksi')
        ax.set_title('Tingkat Stres Prediksi')
        ax.set_xlim(0, 1)
        st.pyplot(fig)

        # Penjelasan tambahan
        st.markdown("""
        **Tips Mengurangi Stres:**
        - **Tidur yang cukup**: Minimal 7-8 jam per malam.
        - **Atur waktu belajar**: Jangan belajar terlalu lama tanpa istirahat.
        - **Kegiatan sosial**: Berinteraksi dengan teman dapat membantu mengurangi stres.
        - **Aktivitas fisik**: Berolahraga minimal 30 menit sehari.
        """)
    else:
        st.error("Model atau label encoder belum dimuat. Pastikan file yang diperlukan tersedia.")
