import os

BOT_TOKEN = os.environ.get('BOT_TOKEN') or 'Token del Bot de Telegram'
CORTEX_COMMAND = r".\cortex.exe run llama3.2:3b"
CHROMA_DB_PATH = "./chroma_db"
CSV_TRAIN_FILE = "./train.csv"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
EMBEDDING_DISTANCE_THRESHOLD = 0.35

SYSTEM_PROMPT = """ Instrucción del sistema para condicionar una mejor respuesta del LLM"""
