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
        return pd.DataFrame(columns=["ID", "Título", "Autor", "Género", "Enlace", "Sinopsis"])

# Interfaz en Streamlit
st.title("📚 Librería Digital")

df_libros = cargar_datos()

if not df_libros.empty:
    st.write("Listado de libros disponibles:")

    for index, row in df_libros.iterrows():
        with st.expander(f"📖 {row['Título']} - {row['Autor']}"):
            st.write(f"**Género:** {row['Género']}")
            st.write(f"**Sinopsis:** {row['Sinopsis'] if pd.notna(row['Sinopsis']) else 'No disponible'}")
            st.download_button(
                label="📥 Descargar",
                data="",
                file_name=row["Archivo"],
                key=row["ID"],
                on_click=lambda link=row["Enlace"]: st.markdown(f"[Descargar aquí]({link})")
            )
else:
    st.warning("No se encontraron libros en la base de datos.")
