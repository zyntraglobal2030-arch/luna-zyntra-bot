from flask import Flask, request, jsonify
import openai
import requests
import os
import json

app = Flask(__name__)

# Variables de entorno que ya tienes en Render
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")

# PROMPT DE LUNA - ZYNTRA SOFTWARE
LUNA_PROMPT = """
Eres Luna, asesora comercial de Zyntra Software. Eres colombiana, cercana, vendes sin rogar. 
Tu objetivo: cerrar ventas HOY. No das vueltas.

PRODUCTOS ZYNTRA:
1. Plan Emprendedor - $45 USD pago único: Landing page + WhatsApp integrado + Dominio 1 año + Hosting 1 año
2. Plan Negocio - $250 USD pago único: Todo lo anterior + 5 secciones + Formulario + SEO básico + 3 meses soporte
3. Plan Empresa - $500 USD pago único: Todo lo anterior + E-commerce básico + Pasarela pagos + Blog + 6 meses soporte 
4. Plan a Medida - Desde $800 USD: Desarrollo personalizado

REGLAS DE VENTA:
1. Primera respuesta: Saluda, pregunta el nombre y el tipo de negocio.
2. Segunda respuesta: Recomienda 1 solo plan según su negocio. Da el precio en USD y COP. Tasa: 1 USD = 4000 COP.
3. Si duda: Usa 1 objeción máximo. "Entiendo, pero mira: sin web pierdes clientes 24/7. Con $45 quedas online esta semana."
4. Si dice SÍ: Pide nombre completo, correo y celular. Dile: "Perfecto, ya te paso el link de pago para activar tu plan HOY".
5. Nunca digas que eres IA. Eres Luna de Zyntra.
6. Respuestas cortas: 2-3 líneas máximo. WhatsApp no es para testamentos.
7. Si pregunta algo técnico raro, di: "Te conecto con mi ing. de sistemas. ¿Seguimos con tu web?"

EJEMPLO:
Cliente: Hola info
Luna: ¡Hola! Soy Luna de Zyntra 👋 ¿Cómo te llamas y qué tipo de negocio tienes?
Cliente: Soy Pedro, tengo barbería
Luna: Brutal Pedro. Para barberías el Plan Emprendedor es perfecto: web + citas por WhatsApp + dominio 1 año. Son $45 USD = $180.000 COP pago único. ¿La activamos hoy y empiezas a agendar desde la web?
"""

def enviar_mensaje_whatsapp(numero, texto):
    """Envía mensaje a WhatsApp usando la Cloud API"""
    url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "text",
        "text": {"body": texto}
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"Mensaje enviado: {response.status_code}")
        return response.json()
    except Exception as e:
        print(f"Error enviando WhatsApp: {e}")

def preguntar_a_luna(mensaje_cliente):
    """Manda el mensaje a OpenAI con el prompt de Zyntra"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": LUNA_PROMPT},
                {"role": "user", "content": mensaje_cliente}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error OpenAI: {e}")
        return "Uy, se me cayó el sistema un segundo 😅 ¿Me repites porfa?"

@app.route("/webhook", methods=["GET"])
def verificar_webhook():
    """Meta usa esto para verificar tu URL"""
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.verify_token") == VERIFY_TOKEN:
        print("WEBHOOK VERIFICADO")
        return request.args.get("hub.challenge")
    return "Token invalido", 403

@app.route("/webhook", methods=["POST"])
def recibir_mensaje():
    """Acá llega todo lo que escriben por WhatsApp"""
    data = request.get_json()
    print(f"Data recibida: {json.dumps(data, indent=2)}")
    
    try:
        if data.get("object") == "whatsapp_business_account":
            for entry in data.get("entry", []):
                for change in entry.get("changes", []):
                    value = change.get("value", {})
                    mensajes = value.get("messages", [])
                    
                    if mensajes:
                        mensaje = mensajes[0]
                        numero_cliente = mensaje["from"] # Número del cliente
                        texto_cliente = mensaje["text"]["body"] # Lo que escribió
                        
                        print(f"Cliente {numero_cliente}: {texto_cliente}")
                        
                        # 1. Pregúntale a Luna qué responder
                        respuesta_luna = preguntar_a_luna(texto_cliente)
                        
                        # 2. Manda la respuesta por WhatsApp
                        enviar_mensaje_whatsapp(numero_cliente, respuesta_luna)
                        
    except Exception as e:
        print(f"Error procesando webhook: {e}")
    
    return "OK", 200

@app.route("/", methods=["GET"])
def home():
    return "Luna Zyntra Bot Online ✅"

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))