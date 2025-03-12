import streamlit as st
import pandas as pd

# URL cruda del CSV en GitHub
csv_url = "https://raw.githubusercontent.com/PitziPana/LIBRERIAWEB/main/libros_descargados.csv"

# Cargar el CSV con los libros desde GitHub
def cargar_datos():
    try:
        return pd.read_csv(csv_url)
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return pd.DataFrame(columns=["ID", "Título", "Autor", "Archivo", "Fecha", "Género", "Sinopsis", "Enlace"])

# Interfaz en Streamlit
st.title("📚 Librería Digital")

df_libros = cargar_datos()

if not df_libros.empty:
    st.write("Listado de libros disponibles:")
    st.dataframe(df_libros[["Título", "Autor", "Género", "Enlace"]])
else:
    st.warning("No se encontraron libros en la base de datos.")
