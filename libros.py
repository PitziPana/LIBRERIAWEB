import streamlit as st
import pandas as pd

# URL del CSV en GitHub (ruta correcta)
csv_url = "https://raw.githubusercontent.com/PitziPana/LIBRERIAWEB/main/libros_descargados.csv"

# Función para cargar el CSV desde GitHub
@st.cache_data
def cargar_datos():
    try:
        df = pd.read_csv(csv_url)
        return df
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return pd.DataFrame(columns=["ID", "Título", "Autor", "Género", "Enlace", "Sinopsis"])

# Título de la aplicación en Streamlit
st.title("📚 Librería Digital")

df_libros = cargar_datos()

# Mostrar el número total de libros
st.markdown(f"📖 **Número de libros en el catálogo:** {len(df_libros)}")

if not df_libros.empty:
    st.write("Listado de libros disponibles:")

    for index, row in df_libros.iterrows():
        titulo = row["Título"]
        autor = row["Autor"]
        genero = row["Género"]
        sinopsis = row["Sinopsis"] if pd.notna(row["Sinopsis"]) else "No disponible"
        enlace = row["Enlace"]
        portada = f"https://drive.google.com/thumbnail?id={enlace.split('id=')[-1]}&sz=w200"  # Miniatura del libro

        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(portada, caption=titulo, use_column_width=True)
            with col2:
                st.subheader(titulo)
                st.write(f"**Autor:** {autor}")
                st.write(f"**Género:** {genero}")
                st.write(f"**Sinopsis:** {sinopsis}")
                st.markdown(f"[📥 Descargar libro](https://drive.google.com/uc?export=download&id={enlace.split('id=')[-1]})")

st.success("✅ Aplicación cargada correctamente.")
