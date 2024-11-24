# 🥗 Fridge Menu Generator

## 📝 Descripción
Fridge Menu Generator es una aplicación web inteligente que utiliza la API de Google Gemini para analizar imágenes de ingredientes y generar recetas personalizadas. La aplicación considera las preferencias dietéticas del usuario y su ubicación para proporcionar recomendaciones relevantes y culturalmente apropiadas.

## ✨ Características

- 📸 Análisis visual de ingredientes mediante IA
- 🍳 Generación de recetas personalizadas
- 📋 Creación automática de listas de compras
- 🌍 Adaptación a preferencias culturales y ubicación
- 🥬 Soporte para restricciones dietéticas
- 💡 Interfaz intuitiva y fácil de usar

## 🛠️ Tecnologías

- Python 3.8+
- Streamlit
- Google Generative AI (Gemini)
- Pillow
- python-dotenv

## 📁 Estructura del Proyecto

``` 
fridge_menu_generator/
├── app/                        # Directorio principal de la aplicación
│   ├── __init__.py            
│   ├── main.py                # Punto de entrada (Streamlit)
│   ├── config/                # Configuración del proyecto
│   ├── services/              # Servicios externos y lógica
│   ├── utils/                 # Utilidades
│   └── interfaces/            # Interfaz de usuario
├── tests/                     # Pruebas
├── data/                      # Datos y recursos
├── requirements.txt           # Dependencias
├── .env                       # Variables de entorno
└── README.md                  # Documentación
```

## 🚀 Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/EliazarNoaLlas/fridge_menu_generator.git
cd fridge_menu_generator
```

2. **Crear y activar entorno virtual**
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/MacOS
python3 -m venv .venv
source .venv/bin/activate
```

3. **Instalar dependencias**
```bash
# Instalar dependencias principales
pip install -r requirements.txt

# Instalar Google Generative AI desde GitHub
pip install git+https://github.com/google/generative-ai-python.git
```

4. **Configurar variables de entorno**
```bash
# Crear archivo .env
cp .env.example .env

# Editar .env con tu API key de Google Gemini
GEMINI_API_KEY=tu_api_key_aqui
```

## 🎮 Uso

1. **Iniciar la aplicación**
```bash
streamlit run app/main.py
```

2. **Acceder a la aplicación**
- Abre tu navegador y ve a `http://localhost:8501`
- La interfaz te guiará a través del proceso:
  1. Configura tus preferencias dietéticas
  2. Selecciona tu ubicación
  3. Sube una imagen de tus ingredientes
  4. Recibe recetas personalizadas y lista de compras

## 📝 Configuración

### Requisitos del Sistema
- Python 3.8 o superior
- Conexión a Internet
- Clave API de Google Gemini

### Variables de Entorno
Crear un archivo `.env` en la raíz del proyecto con:
```
GEMINI_API_KEY=tu_api_key_aqui
ENVIRONMENT=development
DEBUG=True
```

## 🧪 Pruebas

```bash
# Ejecutar todas las pruebas
python -m pytest

# Ejecutar pruebas específicas
python -m pytest tests/test_gemini_service.py
```

## 📚 Documentación Adicional

### API de Gemini
- [Documentación oficial de Gemini](https://ai.google.dev/docs)
- [Guía de inicio rápido](https://ai.google.dev/tutorials/python_quickstart)

### Streamlit
- [Documentación de Streamlit](https://docs.streamlit.io)
- [Componentes personalizados](https://docs.streamlit.io/library/components)

## 🤝 Contribución

1. Fork el repositorio
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para más detalles.

## 👥 Autores

- **Tu Nombre** - *Trabajo Inicial* - [TuGitHub](https://github.com/tugithub)

## 🙏 Agradecimientos

- Google por proporcionar acceso a la API de Gemini
- Comunidad de Streamlit por sus excelentes herramientas
- Todos los contribuyentes que han participado en este proyecto

## 📧 Contacto

Para preguntas y soporte, por favor contacta a: tu@email.com
