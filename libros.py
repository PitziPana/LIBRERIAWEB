import streamlit as st
import pandas as pd

# URL del CSV en GitHub
CSV_URL = "https://raw.githubusercontent.com/PitziPana/LIBRERIAWEB/main/libros_descargados.csv"

# Función para cargar datos
@st.cache_data
def cargar_datos():
    try:
        df = pd.read_csv(CSV_URL)
        return df
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return pd.DataFrame(columns=["ID", "Título", "Autor", "Género", "Enlace", "Sinopsis"])

# Cargar datos
df_libros = cargar_datos()

# Título de la aplicación
st.title("📚 Librería Digital")

# Mostrar número de libros
st.markdown(f"📖 **Número de libros en el catálogo:** {len(df_libros)}")

if not df_libros.empty:
    st.write("Listado de libros disponibles:")

    for index, row in df_libros.iterrows():
        with st.expander(f"📖 {row['Título']} - {row['Autor']}"):
            st.write(f"**Género:** {row['Género']}")
            st.write(f"**Sinopsis:** {row['Sinopsis'] if pd.notna(row['Sinopsis']) else 'No disponible'}")
            st.markdown(f"[📥 Descargar libro](https://drive.google.com/uc?export=download&id={row['Enlace'].split('id=')[-1]})")
