import streamlit as st
import pandas as pd

# 📌 URL del CSV en GitHub
csv_url = "https://raw.githubusercontent.com/PitziPana/LIBRERIAWEB/main/libros_descargados.csv"
avatar_url = "https://raw.githubusercontent.com/PitziPana/LIBRERIAWEB/main/avatar_pitzipana.jpg"

# 📌 Cargar el CSV con los libros desde GitHub
@st.cache_data
def cargar_datos():
    try:
        return pd.read_csv(csv_url)
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return pd.DataFrame(columns=["ID", "Título", "Autor", "Género", "Enlace", "Sinopsis"])

# 📌 Interfaz en Streamlit
st.set_page_config(page_title="Librería Digital", layout="wide")

# 📌 Mostrar el avatar y el título
col1, col2 = st.columns([1, 5])
with col1:
    st.image(avatar_url, width=120)
with col2:
    st.title("📚 Librería Digital")
    st.markdown("*Tailored by PitziPana*")

# 📌 Cargar los libros
df_libros = cargar_datos()

# 📌 Barra de búsqueda
busqueda = st.text_input("🔎 Buscar por título o autor")

# 📌 Opciones de ordenamiento
orden_opcion = st.radio("📌 Ordenar por:", ["Ninguno", "Título (A-Z)", "Autor (A-Z)"], horizontal=True)

# 📌 Filtrar los libros según la búsqueda
if busqueda:
    df_libros = df_libros[df_libros.apply(lambda row: busqueda.lower() in str(row["Título"]).lower() 
                                                        or busqueda.lower() in str(row["Autor"]).lower(), axis=1)]

# 📌 Ordenar según la opción elegida
if orden_opcion == "Título (A-Z)":
    df_libros = df_libros.sort_values(by="Título")
elif orden_opcion == "Autor (A-Z)":
    df_libros = df_libros.sort_values(by="Autor")

# 📌 Mostrar el total de libros encontrados
st.markdown(f"📚 **Total de libros encontrados: {len(df_libros)}**")

# 📌 Mostrar la lista de libros con estilo mejorado
if not df_libros.empty:
    for _, row in df_libros.iterrows():
        with st.expander(f"📖 {row['Título']} - {row['Autor']}"):
            st.write(f"**📚 Género:** {row['Género']}")
            st.write(f"**📖 Sinopsis:** {row['Sinopsis'] if pd.notna(row['Sinopsis']) else 'No disponible'}")
            st.markdown(f"[📥 Descargar]({row['Enlace']})")
else:
    st.warning("No se encontraron libros con ese criterio de búsqueda.")
