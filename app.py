from flask import Flask, request
import requests
import os
from threading import Thread

app = Flask(__name__)

# Variables de entorno - ponlas en Render
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

# Health check para Render
@app.route('/')
def home():
    return "Luna Zyntra Bot Online ✅", 200

# Función para enviar mensajes a WhatsApp
def enviar_mensaje(numero, texto):
    url = f"https://graph.facebook.com/v25.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "text",
        "text": {"body": texto}
    }
    try:
        r = requests.post(url, headers=headers, json=data)
        print(f"📤 Enviando a {numero}: {texto}")
        print(f"Respuesta de Meta: {r.status_code}")
        if r.status_code!= 200:
            print(f"Error Meta: {r.text}")
    except Exception as e:
        print(f"❌ Error enviando mensaje: {str(e)}")

# Función para procesar mensaje con OpenAI o lógica de Luna
def preguntar_a_luna(texto_usuario):
    # Aquí va tu lógica. Por ahora responde eco para probar
    respuesta = f"Hola! Soy Luna 🤖 Recibí tu mensaje: {texto_usuario}"

    # Si usas OpenAI, sería algo así:
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    # completion = openai.ChatCompletion.create(
    # model="gpt-4o-mini",
    # messages=[{"role": "user", "content": texto_usuario}]
    # )
    # respuesta = completion.choices[0].message.content

    return respuesta

# Procesa el mensaje en background para responder rápido a Meta
def procesar_mensaje_async(numero, texto):
    try:
        respuesta = preguntar_a_luna(texto)
        enviar_mensaje(numero, respuesta)
    except Exception as e:
        print(f"❌ ERROR procesando mensaje: {str(e)}")
        enviar_mensaje(numero, "Ups, tuve un error procesando tu mensaje 😅")

# Verificación del webhook de Meta
@app.route('/webhook', methods=['GET'])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("✅ WEBHOOK VERIFICADO")
        return challenge, 200
    else:
        print("❌ Verificación fallida")
        return "Forbidden", 403

# Recibe mensajes de WhatsApp
@app.route('/webhook', methods=['POST'])
def webhook():
    print("🔥 === POST DE MENSAJE RECIBIDO ===")
    try:
        data = request.get_json()
        print(f"Payload completo: {data}")

        if data.get("object") == "whatsapp_business_account":
            for entry in data.get("entry", []):
                for change in entry.get("changes", []):
                    value = change.get("value", {})
                    messages = value.get("messages", [])

                    if messages:
                        for message in messages:
                            from_number = message.get("from")
                            msg_type = message.get("type")

                            print(f"Mensaje de: {from_number}, Tipo: {msg_type}")

                            if msg_type == "text":
                                text = message.get("text", {}).get("body")
                                print(f"Texto: {text}")

                                # Responde en background para no bloquear a Meta
                                Thread(target=procesar_mensaje_async, args=(from_number, text)).start()

        # Siempre devuelve 200 OK rápido para que Meta no te pause el webhook
        return "OK", 200

    except Exception as e:
        print(f"❌ ERROR EN WEBHOOK: {str(e)}")
        # Aún con error, devuelve 200 para que Meta no desactive el webhook
        return "OK", 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))