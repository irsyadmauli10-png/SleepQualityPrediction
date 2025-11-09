import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# ==============================
# 1. Load Model & Scaler
# ==============================
logreg_model = joblib.load("model_logreg.joblib")
rf_model = joblib.load("model_rf.joblib")
scaler = joblib.load("scaler.joblib")

# ==============================
# 2. Konfigurasi Aplikasi
# ==============================
st.set_page_config(page_title="Prediksi Kualitas Tidur", layout="centered")
st.title("🛌 Prediksi Kualitas Tidur Menggunakan ML")
st.markdown("Model: **Logistic Regression** dan **Random Forest**")

# ==============================
# 3. Input Data dari User
# ==============================
st.header("Masukkan Data Pengguna")

age = st.number_input("Usia (tahun)", min_value=10, max_value=100, value=25)
sleep_duration = st.number_input("Durasi Tidur (jam)", min_value=0.0, max_value=12.0, value=7.0)
physical_activity = st.number_input("Tingkat Aktivitas Fisik (0-100)", min_value=0, max_value=100, value=50)
stress_level = st.slider("Tingkat Stres (1-10)", 1, 10, 5)
heart_rate = st.number_input("Detak Jantung (bpm)", min_value=40, max_value=120, value=75)
daily_steps = st.number_input("Langkah Harian", min_value=0, max_value=20000, value=5000)

# Buat DataFrame input user
input_data = pd.DataFrame({
    "Age": [age],
    "Sleep Duration": [sleep_duration],
    "Physical Activity Level": [physical_activity],
    "Stress Level": [stress_level],
    "Heart Rate": [heart_rate],
    "Daily Steps": [daily_steps]
})

# ==============================
# 4. Normalisasi Data
# ==============================
X_scaled = scaler.transform(input_data)

# ==============================
# 5. Pilih Model
# ==============================
st.subheader("Pilih Model untuk Prediksi")
model_choice = st.radio("Model yang digunakan:", ["Logistic Regression", "Random Forest"])

# ==============================
# 6. Prediksi
# ==============================
if st.button("Prediksi Kualitas Tidur"):
    if model_choice == "Logistic Regression":
        prediction = logreg_model.predict(X_scaled)
    else:
        prediction = rf_model.predict(X_scaled)
    
    hasil = int(prediction[0])

    # ==============================
    # 7. Tampilkan Hasil
    # ==============================
    st.success(f"🎯 Perkiraan Kualitas Tidur Anda: **{hasil} / 10**")

    # Interpretasi tambahan
    if hasil >= 8:
        st.info("💤 Tidur Anda sangat baik, pertahankan kebiasaan sehat ini!")
    elif hasil >= 6:
        st.warning("😴 Tidur Anda cukup, tapi bisa ditingkatkan lagi.")
    else:
        st.error("⚠️ Tidur Anda kurang baik. Coba perbaiki pola tidur dan gaya hidup.")
