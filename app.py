from flask import Flask, request
import requests
import os
import json

app = Flask(__name__)

# Variables de entorno - ya las tienes en Render
VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN")  # El que pusiste en Meta
WHATSAPP_TOKEN = os.environ.get("WHATSAPP_TOKEN")  # El EAAN... que generaste
PHONE_NUMBER_ID = os.environ.get("PHONE_NUMBER_ID")  # De Paso 1. Probar

# URL de la API de WhatsApp
WHATSAPP_API_URL = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"

@app.route('/')
def home():
    return "Luna Zyntra Bot está corriendo ✅", 200

@app.route('/webhook', methods=['GET'])
def verify_webhook():
    """
    Meta usa GET para verificar tu webhook la primera vez
    """
    print("=== GET DE VERIFICACION RECIBIDO ===")
    
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    
    print(f"Mode: {mode}, Token recibido: {token}")
    
    if mode == 'subscribe' and token == VERIFY_TOKEN:
        print("✅ WEBHOOK VERIFICADO CORRECTAMENTE")
        return challenge, 200
    else:
        print("❌ TOKEN INVALIDO EN VERIFICACION")
        return "Token invalido", 403

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Meta usa POST cada vez que llega un mensaje de WhatsApp
    """
    print("🔥 === POST DE MENSAJE RECIBIDO ===")
    
    try:
        data = request.get_json()
        print("Payload completo:")
        print(json.dumps(data, indent=2))
        
        # Verificar que sea un mensaje de WhatsApp
        if data.get('object') == 'whatsapp_business_account':
            for entry in data.get('entry', []):
                for change in entry.get('changes', []):
                    value = change.get('value', {})
                    
                    # Si hay mensajes
                    if 'messages' in value:
                        for message in value['messages']:
                            from_number = message.get('from')  # 573228212698
                            message_type = message.get('type')
                            
                            print(f"Mensaje de: {from_number}, Tipo: {message_type}")
                            
                            # Si es texto
                            if message_type == 'text':
                                text = message.get('text', {}).get('body')
                                print(f"Texto: {text}")
                                
                                # AQUÍ RESPONDE LUNA
                                enviar_mensaje(from_number, f"Hola! Soy Luna 🤖 Recibí tu mensaje: {text}")
                    
                    # Si hay estados de mensaje - solo loguear
                    if 'statuses' in value:
                        print("Estado de mensaje recibido:", value['statuses'])
        
        return "OK", 200
    
    except Exception as e:
        print(f"❌ ERROR EN WEBHOOK: {str(e)}")
        return "ok", 200
