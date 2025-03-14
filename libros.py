import streamlit as st
import pandas as pd

# URL del CSV en GitHub
csv_url = "https://raw.githubusercontent.com/PitziPana/LIBRERIAWEB/main/libros_descargados.csv"

# Cargar el CSV
def cargar_datos():
    try:
        return pd.read_csv(csv_url)
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return pd.DataFrame(columns=["ID", "Título", "Autor", "Enlace"])

# Interfaz en Streamlit
st.title("📚 Librería Digital - Prueba de Enlaces")

df_libros = cargar_datos()

# Verificar si el CSV se cargó bien
if df_libros.empty:
    st.error("No se han encontrado datos en el CSV.")
else:
    st.success(f"📖 **Número de libros en el catálogo:** {len(df_libros)}")

    for index, row in df_libros.iterrows():
        with st.expander(f"📖 {row['Título']} - {row['Autor']}"):
            st.markdown(f"[📥 Descargar libro]({row['Enlace']})")
