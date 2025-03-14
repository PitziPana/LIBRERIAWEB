import streamlit as st
import pandas as pd

# Cargar datos desde el CSV (ajusta la ruta correcta)
CSV_PATH = "ruta_a_tu_csv/libros_descargados.csv"
df = pd.read_csv(CSV_PATH)

# Título de la aplicación
st.title("📚 Biblioteca Digital")

for index, row in df.iterrows():
    titulo = row["Título"]
    autor = row["Autor"]
    enlace = row["Enlace"]

    # Extraer el ID del archivo de Google Drive de manera más segura
    if "id=" in enlace:
        archivo_id = enlace.split("id=")[-1].split("&")[0]
        enlace_descarga = f"https://drive.google.com/uc?export=download&id={archivo_id}"
        portada = f"https://drive.google.com/thumbnail?id={archivo_id}&sz=w200"
    else:
        archivo_id = None
        enlace_descarga = None
        portada = None

    # Mostrar en Streamlit
    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            if portada:
                st.image(portada, caption=titulo, use_column_width=True)
        with col2:
            st.subheader(titulo)
            st.write(f"**Autor:** {autor}")
            if enlace_descarga:
                st.markdown(f"[📥 Descargar libro]({enlace_descarga})")
            else:
                st.write("⚠️ Enlace no válido")
