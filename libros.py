import streamlit as st
import pandas as pd

# URL del CSV en GitHub
csv_url = "https://raw.githubusercontent.com/PitziPana/LIBRERIAWEB/main/libros_descargados.csv"

# Cargar datos desde el CSV
def cargar_datos():
    try:
        return pd.read_csv(csv_url)
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return pd.DataFrame(columns=["ID", "Título", "Autor", "Género", "Enlace", "Sinopsis"])

# Interfaz elegante en Streamlit
st.set_page_config(page_title="Librería Digital", layout="wide")

# Cargar datos
libros_df = cargar_datos()

# Mostrar avatar y título
st.image("https://raw.githubusercontent.com/PitziPana/LIBRERIAWEB/main/avatar.jpg", width=150)
st.title("📚 Librería Digital")
st.markdown("### *Tailored by PitziPana* 🛠️")

# Barra de búsqueda
busqueda = st.text_input("🔍 Buscar por título o autor", "")

# Filtrar resultados
if busqueda:
    libros_filtrados = libros_df[libros_df["Título"].str.contains(busqueda, case=False, na=False) | 
                                 libros_df["Autor"].str.contains(busqueda, case=False, na=False)]
else:
    libros_filtrados = libros_df

# Mostrar resultados
st.write(f"📚 Total de libros encontrados: {len(libros_filtrados)}")

if not libros_filtrados.empty:
    for index, row in libros_filtrados.iterrows():
        with st.expander(f"📖 {row['Título']} - {row['Autor']}"):
            st.write(f"**Género:** {row['Género']}")
            st.write(f"**Sinopsis:** {row['Sinopsis'] if pd.notna(row['Sinopsis']) else 'No disponible'}")
            st.markdown(f"[📥 Descargar]({row['Enlace']})")
