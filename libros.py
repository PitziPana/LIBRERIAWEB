import streamlit as st
import pandas as pd

# URL cruda del CSV en GitHub
csv_url = "https://raw.githubusercontent.com/PitziPana/LIBRERIAWEB/main/libros_descargados.csv"

# 🔄 Forzar la recarga sin caché
@st.cache_data(ttl=0)  # Esto hace que se recargue cada vez que se ejecuta la app
def cargar_datos():
    return pd.read_csv(csv_url)

# Interfaz en Streamlit
st.title("📚 Librería Digital")

df_libros = cargar_datos()

# 📌 Mostrar la fuente y el número de libros cargados
st.write(f"📂 Cargando desde: {csv_url}")
st.write(f"🔢 Número de libros en el CSV: {len(df_libros)}")

if not df_libros.empty:
    st.write("Listado de libros disponibles:")

    for index, row in df_libros.iterrows():
        with st.expander(f"📖 {row['Título']} - {row['Autor']}"):
            st.write(f"**Género:** {row['Género']}")
            st.write(f"**Sinopsis:** {row['Sinopsis'] if pd.notna(row['Sinopsis']) else 'No disponible'}")
            st.markdown(f"[📥 Descargar]({row['Enlace']})")
