import re
import logging
from cortex_runner import ejecutar_cortex
from knowledge_base import obtener_respuesta_semantica

def procesar_mensaje(bot, message):
    if re.search(r"[\$\&\|;]", message.text):
        bot.reply_to(message, "❌ Mensaje no permitido: caracteres peligrosos detectados.")
        return

    try:
        bot.send_chat_action(message.chat.id, 'typing')
        pregunta = message.text
        respuesta = obtener_respuesta_semantica(pregunta)

        if not respuesta:
            respuesta = ejecutar_cortex(pregunta)
            if not respuesta.strip():
                respuesta = "🤖 No recibí una respuesta válida de la IA. Intenta con otro mensaje."

        bot.reply_to(message, respuesta)

    except Exception as e:
        logging.error(f"Error crítico: {str(e)}")
        bot.reply_to(message, f"🔴 Error crítico: {str(e)}")