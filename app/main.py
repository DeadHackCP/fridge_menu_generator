import streamlit as st
import google.generativeai as genai
import os
import json

# Configuración de Gemini
genai.configure(api_key="AIzaSyBeDEapDdHQN6OWRIuk5ufr-zarQru9XeU")

# Configuración del modelo
generation_config = {
    "temperature": 0.7,
    "top_p": 0.85,
    "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)


def generar_recetas_personalizadas(imagen, preferencias):
    """
    Genera recetas personalizadas basadas en imagen y preferencias
    """
    prompt = f"""
    Analiza esta imagen de alimentos y genera una respuesta en el siguiente formato JSON exacto:
    {{
        "recetas": [
            {{
                "nombre_receta": "Nombre de la receta",
                "ingredientes_necesarios": ["ingrediente1", "ingrediente2"],
                "ingredientes_disponibles": ["ingrediente1", "ingrediente2"],
                "instrucciones_paso_a_paso": ["paso1", "paso2"],
                "tiempo_preparacion": "XX minutos",
                "dificultad": "fácil/media/difícil"
            }}
        ]
    }}

    Consideraciones importantes:
    - Identifica todos los ingredientes visibles en la imagen
    - Crea 3 recetas saludables usando máximo 2 ingredientes adicionales
    - Ten en cuenta estas preferencias del usuario: {preferencias}
    - La respuesta DEBE ser un JSON válido con la estructura exacta mostrada arriba
    """

    try:
        response = model.generate_content([imagen, prompt])
        # Extraer el JSON de la respuesta
        response_text = response.text
        # Si la respuesta contiene bloques de código, extraer solo el JSON
        if "```json" in response_text:
            response_text = response_text.split("```json")[1].split("```")[0]
        elif "```" in response_text:
            response_text = response_text.split("```")[1].split("```")[0]

        # Limpiar el texto y convertir a JSON
        response_text = response_text.strip()
        return json.loads(response_text)
    except Exception as e:
        st.error(f"Error generando recetas: {str(e)}")
        return None


def lista_compras(recetas):
    """
    Genera lista de compras a partir de recetas
    """
    lista = {}
    for receta in recetas:
        for ingrediente in receta.get('ingredientes_necesarios', []):
            if ingrediente not in lista:
                lista[ingrediente] = 1
            else:
                lista[ingrediente] += 1
    return lista


def main():
    st.set_page_config(
        page_title="NutriAI - Tu Asistente Nutricional",
        page_icon="🥗",
        layout="wide"
    )

    st.title("🤖 NutriAI: Asistente Nutricional Inteligente")

    # Sidebar para preferencias
    st.sidebar.header("📋 Configuración Personal")
    ubicacion = st.sidebar.selectbox(
        "Tu ubicación",
        ["México", "Argentina", "España", "Colombia"]
    )

    dieta = st.sidebar.multiselect(
        "Restricciones alimenticias",
        [
            "Vegetariano",
            "Vegano",
            "Sin gluten",
            "Bajo en carbohidratos",
            "Ninguna"
        ]
    )

    # Carga de imagen
    uploaded_file = st.file_uploader(
        "Sube una foto de tus ingredientes 📸",
        type=['jpg', 'jpeg', 'png']
    )

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Imagen de ingredientes')

        if st.button('Generar Recetas 🍳'):
            with st.spinner('Analizando imagen...'):
                # Convertir imagen a formato compatible
                imagen = genai.upload_file(
                    uploaded_file,
                    mime_type=uploaded_file.type
                )

                preferencias = {
                    "ubicacion": ubicacion,
                    "dieta": dieta
                }

                resultado = generar_recetas_personalizadas(imagen, preferencias)

                if resultado and 'recetas' in resultado:
                    st.subheader("🥘 Recetas Personalizadas")
                    for receta in resultado['recetas']:
                        with st.expander(receta['nombre_receta']):
                            st.write(f"**Tiempo de preparación:** {receta['tiempo_preparacion']}")
                            st.write(f"**Dificultad:** {receta['dificultad']}")

                            st.markdown("### Ingredientes")
                            col1, col2 = st.columns(2)

                            with col1:
                                st.markdown("**Disponibles:**")
                                for ing in receta['ingredientes_disponibles']:
                                    st.write(f"✅ {ing}")

                            with col2:
                                st.markdown("**Necesarios:**")
                                for ing in receta['ingredientes_necesarios']:
                                    st.write(f"🛒 {ing}")

                            st.markdown("### Instrucciones")
                            for idx, paso in enumerate(receta['instrucciones_paso_a_paso'], 1):
                                st.write(f"{idx}. {paso}")

                    st.subheader("🛍️ Lista de Compras")
                    lista = lista_compras(resultado['recetas'])
                    for ingrediente, cantidad in lista.items():
                        st.write(f"- {ingrediente}: {cantidad}")
                else:
                    st.error("No se pudieron generar recetas. Por favor, intenta con otra imagen.")


if __name__ == "__main__":
    main()