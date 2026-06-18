"""
Luna Zyntra Bot - Con OpenAI GPT-4
Webhook para WhatsApp + IA
"""

from flask import Flask, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

# ============ CONFIGURACIÓN OPENAI ============
# La key se lee de Render → Environment, NO la pongas aquí
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# ============ RUTAS PARA RENDER ============
@app.route("/")
def home():
    return "Luna Zyntra Bot con OpenAI Online", 200

@app.route("/health")
def health():
    return jsonify(status="ok", model="gpt-4o"), 200

# ============ PROMPT DE LUNA ============
SYSTEM_PROMPT = """
Eres Luna, asistente de ventas de IA para WhatsApp.

Tu trabajo:
1. Detectar el nicho del usuario: dentista, coach, tienda, restaurante, etc
2. Recomendar Plan Base $45, Plan Pro $250 o Empresarial $500 según su perfil
3. Manejar objeciones de precio, tiempo, desconfianza con cierres directos
4. Siempre cerrar con el link de pago de Hotmart

Planes:
- Base $45: Solo aprender, sin bot
- Pro $250: Bot funcional 24/7 + soporte $100/mes
- Empresarial $500: Nosotros hacemos todo + $225/mes

Links:
Base: https://pay.hotmart.com/B106162955H?off=f8fa87yy
Pro: https://pay.hotmart.com/B106162955H?off=fiylp4i8
Empresarial: https://pay.hotmart.com/B106162955H?off=vlptt99p

Tono: Colombiano, cercano, directo. Usa "parce", "bro". No seas robot.
Si duda por precio: "¿Cuánto pierdes al mes por no contestar 24/7? Si son 3 ventas de $100, ya perdiste $300. El Pro vale $250."
Siempre pregunta a qué se dedica primero.
"""

# ============ FUNCIÓN PRINCIPAL CON OPENAI ============
def luna_responder(mensaje_usuario, historial=[]):
    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        # Agrega historial previo si existe
        for msg in historial:
            messages.append(msg)

        # Agrega mensaje actual del usuario
        messages.append({"role": "user", "content": mensaje_usuario})

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.8,
            max_tokens=500
        )

        respuesta_ia = response.choices[0].message.content
        return respuesta_ia

    except Exception as e:
        print(f"Error OpenAI: {e}")
        return "Ups parce, tuve un error. ¿Me repites qué necesitas?"

# ============ WEBHOOK PARA WHATSAPP/MAKE ============
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Verificación de Meta
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN", "luna_token_123")

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return 'Forbidden', 403

    if request.method == 'POST':
        data = request.json
        print("Webhook recibido:", data)

        # Extraer mensaje de WhatsApp
        try:
            mensaje = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
            numero = data['entry'][0]['changes'][0]['value']['messages'][0]['from']
        except:
            # Si viene de Make con otro formato
            mensaje = data.get('mensaje', '')
            numero = data.get('numero', '')

        # Llamar a OpenAI
        respuesta = luna_responder(mensaje)

        # Aquí deberías enviar la respuesta de vuelta a WhatsApp
        # Por ahora solo la devolvemos para Make
        return jsonify({
            "respuesta": respuesta,
            "numero_destino": numero
        })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)