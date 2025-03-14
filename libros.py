import streamlit as st
import pandas as pd

# Limpiar caché al inicio
st.cache_data.clear()

# URL del CSV en GitHub
CSV_URL = "https://raw.githubusercontent.com/PitziPana/LIBRERIAWEB/main/libros_descargados.csv"

@st.cache_data
def cargar_datos():
    try:
        df = pd.read_csv(CSV_URL)
        return df
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return pd.DataFrame(columns=["ID", "Título", "Autor", "Género", "Sinopsis", "Enlace"])

# Cargar datos
st.title("📚 Librería Digital")

# Avatar y título personalizado
st.image("https://avatars.githubusercontent.com/u/12345678?v=4", width=100)
st.markdown("### Tailored by Pitzipana")

df_libros = cargar_datos()

# Mostrar total de libros
st.markdown(f"📖 **Número de libros en el catálogo:** {len(df_libros)}")

# Cuadro de búsqueda
busqueda = st.text_input("🔍 Buscar libros por título o autor:")

# Filtrar libros
if busqueda:
    df_libros = df_libros[df_libros["Título"].str.contains(busqueda, case=False, na=False) |
                           df_libros["Autor"].str.contains(busqueda, case=False, na=False)]

# Mostrar libros
if not df_libros.empty:
    for _, row in df_libros.iterrows():
        with st.expander(f"📖 {row['Título']} - {row['Autor']}"):
            st.write(f"**Género:** {row['Género']}")
            st.write(f"**Sinopsis:** {row['Sinopsis'] if pd.notna(row['Sinopsis']) else 'No disponible'}")
            
            # Convertir enlace a descarga directa
            if "id=" in row["Enlace"]:
                id_archivo = row["Enlace"].split("id=")[-1].split("&")[0]
                enlace_descarga = f"https://drive.google.com/uc?export=download&id={id_archivo}"
            else:
                enlace_descarga = row["Enlace"]

            st.markdown(f"📥 [Descargar libro]({enlace_descarga})")
else:
    st.warning("No se encontraron libros con ese criterio de búsqueda.")
