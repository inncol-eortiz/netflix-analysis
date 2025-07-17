# Sistema de Recomendación de Películas y Series de Netflix 🎬

Este proyecto re### 📈 Resultados Principales

### Estadísticas del Dataset
- **Dataset principal**: `netflix_dataset.csv`
- **Análisis completo**: En el notebook `practica-9.ipynb`
- **Distribución de contenido**: Películas vs Series de TV
- **Sistema de recomendación**: Basado en similitud de contenido

### Sistema de Recomendación
- Precisión basada en similitud semántica usando TF-IDF
- Recomendaciones personalizadas por contenido
- Análisis de descripción, director, cast y género
- Optimización para datasets grandeslisis exploratorio completo del catálogo de Netflix y desarrolla un sistema de recomendación basado en contenido utilizando técnicas de procesamiento de lenguaje natural y machine learning.

## 🎯 Objetivos

- Realizar análisis exploratorio de datos (EDA) del catálogo de Netflix
- Identificar patrones en el contenido disponible
- Desarrollar un sistema de recomendación basado en similitud de contenido
- Integrar datos de calificaciones de IMDb para análisis de calidad

## 📊 Características del Análisis

### Análisis Exploratorio
- **Distribución de contenido**: Películas vs Series de TV
- **Análisis temporal**: Patrones de adición de contenido por año y mes
- **Análisis geográfico**: Países productores de contenido
- **Análisis de calificaciones**: Ratings y clasificaciones
- **Análisis de duración**: Tiempo de películas y número de temporadas

### Sistema de Recomendación
- **Basado en contenido**: Utiliza descripción, director, cast, género
- **TF-IDF Vectorization**: Para procesamiento de texto
- **Similitud de coseno**: Para calcular similitudes entre títulos
- **Optimización de memoria**: Manejo eficiente de matrices grandes

## 🗂️ Estructura del Proyecto

```
netflix-analisis/
├── netflix_dataset.csv             # Dataset principal de Netflix
├── practica-9.ipynb               # Notebook principal de análisis
├── data/                           # Carpeta para datos adicionales
├── outputs/                        # Carpeta para resultados y gráficos
├── models/                         # Carpeta para modelos guardados
├── .venv/                          # Entorno virtual Python
├── config.py                       # Configuración del proyecto
├── requirements.txt                # Dependencias del proyecto
├── setup.py                        # Script de configuración automática
├── .gitignore                      # Archivos ignorados por Git
├── .vscode/                        # Configuración de VS Code
│   ├── settings.json
│   └── tasks.json
└── README.md                       # Este archivo
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.9+**
- **Pandas**: Manipulación y análisis de datos
- **NumPy**: Computación numérica
- **Matplotlib & Seaborn**: Visualización de datos
- **Plotly**: Visualizaciones interactivas
- **Scikit-learn**: Machine learning y TF-IDF
- **Jupyter Notebook**: Desarrollo y documentación

## 🚀 Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd netflix-analisis
```

### 2. Crear entorno virtual
```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar el análisis
```bash
jupyter notebook practica-9.ipynb
```

## 📊 Dataset Utilizado

El proyecto utiliza el archivo `netflix_dataset.csv` que contiene información completa del catálogo de Netflix, incluyendo:

- **Información básica**: Título, director, cast, país, fecha de adición
- **Categorización**: Tipo (Movie/TV Show), rating, género
- **Descripción**: Sinopsis para el sistema de recomendación
- **Metadatos**: Año de lanzamiento, duración

## 📈 Resultados Principales

### Estadísticas del Dataset
- **Total de títulos**: ~7,783 únicos
- **Películas**: ~5,377
- **Series de TV**: ~2,410
- **Países productores**: Estados Unidos lidera la producción

### Sistema de Recomendación
- Precisión basada en similitud semántica
- Recomendaciones personalizadas por contenido
- Optimización para datasets grandes (+10k títulos)

## 🔍 Ejemplos de Uso del Sistema de Recomendación

```python
# Obtener recomendaciones para una película
recommendations = get_recommendations('Avengers: Infinity War')
print(recommendations)

# Resultado: Lista de 10 películas similares
```

## 📋 Requisitos del Sistema

- **Python**: 3.9 o superior
- **RAM**: Mínimo 4GB (recomendado 8GB para datasets grandes)
- **Almacenamiento**: ~500MB para datasets y archivos temporales

## 🤝 Contribuciones

Este proyecto es parte de un análisis académico. Las contribuciones son bienvenidas:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto es para uso académico y educativo.

## 📧 Contacto

Para preguntas o sugerencias, por favor contacta al equipo de desarrollo.

---

**Nota**: El proyecto utiliza un dataset de Netflix (`netflix_dataset.csv`) que debe estar en la carpeta raíz del proyecto para el correcto funcionamiento del análisis.
