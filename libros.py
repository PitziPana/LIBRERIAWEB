import streamlit as st

# 📂 Simulación de enlaces de libros desde Google Drive (debes conectar con tu fuente real)
libros = [
    {"titulo": "Libro 1", "enlace": "https://drive.google.com/uc?export=download&id=ID_DEL_ARCHIVO_1"},
    {"titulo": "Libro 2", "enlace": "https://drive.google.com/uc?export=download&id=ID_DEL_ARCHIVO_2"},
    {"titulo": "Libro 3", "enlace": "https://drive.google.com/uc?export=download&id=ID_DEL_ARCHIVO_3"},
]

# 🖥️ Mostrar cada libro con su enlace
st.title("📚 Biblioteca de libros")

for libro in libros:
    st.write(f"📖 **{libro['titulo']}**")
    
    # 🔍 Mostrar el enlace en pantalla para ver si es correcto
    st.write(f"🔗 **Enlace generado:** {libro['enlace']}")

    # 📥 Botón de descarga
    st.markdown(f"[📥 Descargar libro]({libro['enlace']})")

    st.write("---")  # Separador entre libros
