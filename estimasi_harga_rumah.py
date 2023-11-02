import pickle
import streamlit as st

model = pickle.load(open('estimasi_harga_rumah.sav','rb'))

st.title('Estimasi Harga Rumah')
house_age = st.number_input ('Masukkan Umur Rumah')
distance_to_MRT = st.number_input ('Masukkan Jarak ke Stasiun Terdekat')
number_cs = st.slider('Masukkan Jumlah Toko',0,10)
latitude = st.number_input ('Masukkan Latitude Lokasi')
longitude = st.number_input ('Masukkan Longitude Lokasi')

predict = ''

if st.button('Hitung Prediksi Harga Rumah'):
    predict = model.predict(
        [[house_age, distance_to_MRT, number_cs, latitude, longitude]]
    )
    st.write('Prediksi Harga Rumah = ',predict)