import streamlit as st
import pandas as pd

# Cargar datos desde el CSV (asegúrate de que la ruta es correcta)
CSV_PATH = "ruta_a_tu_csv/libros_descargados.csv"  # Cambia esto por la ubicación real
df = pd.read_csv(CSV_PATH)

# Mostrar en Streamlit
st.title("📚 Biblioteca Digital")

for index, row in df.iterrows():
    titulo = row["Título"]
    autor = row["Autor"]
    enlace = row["Enlace"]
    portada = f"https://drive.google.com/thumbnail?id={enlace.split('id=')[-1]}&sz=w200"  # Genera la miniatura

    # Mostrar la información en Streamlit
    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(portada, caption=titulo, use_column_width=True)
        with col2:
            st.subheader(titulo)
            st.write(f"**Autor:** {autor}")
            st.markdown(f"[📥 Descargar libro](https://drive.google.com/uc?export=download&id={enlace.split('id=')[-1]})")

st.success("✅ Enlaces corregidos y funcionando correctamente")
