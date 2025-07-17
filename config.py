# Configuración de desarrollo para el proyecto Netflix Analysis
# Este archivo contiene variables y configuraciones para el desarrollo

# Configuración de paths
DATA_DIR = "data/"
OUTPUT_DIR = "outputs/"
MODELS_DIR = "models/"

# Configuración de datasets
NETFLIX_DATASET = "data/netflix_dataset.csv"
IMDB_MOVIES = "data/imdb-movies.csv"
IMDB_RATINGS = "data/imdb-ratings.csv"
NETFLIX_FULL = "data/netflix_full_2025.csv"
MAIN_NOTEBOOK = "practica-9.ipynb"  # Configuración de análisis
MAX_RECOMMENDATIONS = 10
CHUNK_SIZE = 1000  # Para procesamiento de matrices grandes
TF_IDF_MAX_FEATURES = 5000

# Configuración de visualización
PLOT_STYLE = "whitegrid"
FIGURE_SIZE = (12, 8)
DPI = 200

# Configuración de memoria
USE_MEMORY_MAPPING = True  # Para matrices de similitud grandes
COSINE_SIM_FILE = "models/cosine_sim_full_2025.dat"
