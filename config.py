import os

BOT_TOKEN = os.environ.get('BOT_TOKEN') or '8964vfkuyfjGX-4K7D-rsrtdytdiydi-p05wUQMG-w'
CORTEX_COMMAND = r".\cortex.exe run llama3.2:3b"
CHROMA_DB_PATH = "./chroma_db"
CSV_TRAIN_FILE = "./train.csv"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
EMBEDDING_DISTANCE_THRESHOLD = 0.35

SYSTEM_PROMPT = """
Eres un asistente de la empresa cubana de seguridad informática, Segurmática, tu función es dar respuestas explicativas, simples y fáciles de entender, solamente sobre malwares o ciberseguridad, necesitas ser explicativo como asistente y no repetir contexto en tus respuestas. Siempre sugiere contactar con los servicios de Segurmática.
"""