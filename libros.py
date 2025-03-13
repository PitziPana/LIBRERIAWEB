mport streamlit as st
import pandas as pd
import requests
import io

# URL cruda del CSV en GitHub
csv_url = "https://raw.githubusercontent.com/PitziPana/LIBRERIAWEB/main/libros_descargados.csv"

# Cargar el CSV con los libros desde GitHub
def cargar_datos():
    try:
        return pd.read_csv(csv_url)
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return pd.DataFrame(columns=["ID", "Título", "Autor", "Género", "Enlace", "Sinopsis"])

# Función para descargar el archivo desde Google Drive
def descargar_archivo(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return io.BytesIO(response.content)  # Devuelve el contenido como un archivo en memoria
        else:
            return None
    except Exception as e:
        return None

# Interfaz en Streamlit
st.title("📚 Librería Digital")

df_libros = cargar_datos()

if not df_libros.empty:
    st.write("Listado de libros disponibles:")

    for index, row in df_libros.iterrows():
        with st.expander(f"📖 {row['Título']} - {row['Autor']}"):
            st.write(f"**Género:** {row['Género']}")
            st.write(f"**Sinopsis:** {row['Sinopsis'] if pd.notna(row['Sinopsis']) else 'No disponible'}")
            
            # 🔍 Mostrar el enlace en pantalla para verificarlo
            st.write(f"🔗 **Enlace directo:** [{row['Enlace']}]({row['Enlace']})")

            # Descargar el archivo desde Google Drive
            archivo = descargar_archivo(row['Enlace'])
            
            if archivo:
                # Botón de descarga correcto
                st.download_button(
                    label="📥 Descargar",
                    data=archivo,
                    file_name=row["Archivo"],
                    mime="application/epub+zip"
                )
            else:
                st.error("⚠️ Error al descargar el archivo.")
