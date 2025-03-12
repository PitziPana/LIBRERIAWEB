import streamlit as st
import pandas as pd

# Cargar el CSV con los libros
def cargar_datos():
    csv_path = "/content/gdrive/MyDrive/libreria_streamlite/CSV_Libros/libros_descargados.csv"
    try:
        return pd.read_csv(csv_path)
    except FileNotFoundError:
        return pd.DataFrame(columns=["ID", "Título", "Autor", "Archivo", "Fecha", "Género", "Sinopsis", "Enlace"])

# Interfaz en Streamlit
st.title("📚 Librería Digital")

df_libros = cargar_datos()

if not df_libros.empty:
    st.write("Listado de libros disponibles:")
    st.dataframe(df_libros[["Título", "Autor", "Género", "Enlace"]])
else:
    st.warning("No se encontraron libros en la base de datos.")
