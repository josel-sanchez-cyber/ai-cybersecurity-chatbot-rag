import subprocess
from threading import Lock
from config import CORTEX_COMMAND, SYSTEM_PROMPT
from utils import clean_output

process_lock = Lock()

def ejecutar_cortex(mensaje_usuario):
    try:
        with process_lock:
            prompt_final = f"{SYSTEM_PROMPT}\nPregunta: {mensaje_usuario}\nRespuesta:"
            proc = subprocess.run(
                CORTEX_COMMAND.split(),
                input=prompt_final + "\n",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8',
                shell=True,
                timeout=30
            )
            respuesta = clean_output(proc.stdout)
            return respuesta if respuesta else f"⚠️ Error: {proc.stderr.strip() or 'La IA no respondió'}"
    except subprocess.TimeoutExpired:
        return "🕒 La IA tardó demasiado en responder"
    except Exception as e:
        return f"⚠️ Error inesperado: {str(e)}"