"""
Bot Helper - codigoIA_7_1 con Webhook para Make/WhatsApp
Funciones + API Flask lista para integrar con Make, ManyChat, etc
"""

from flask import Flask, request, jsonify
from difflib import get_close_matches
import os

app = Flask(__name__)

# ============ RUTAS PARA RENDER - ARREGLA EL 404 ============
@app.route("/")
def home():
    # Render necesita 200 OK aquí para el health check
    return "Luna Zyntra Bot Online", 200

@app.route("/health")
def health():
    return jsonify(status="ok", bot="Luna Zyntra"), 200

# ============ DATA COMPLETA ============
DATA = {
    "Planes": [
        {
            "Plan": "Plan Base",
            "Precio": 45,
            "Qué incluye": "¿Qué incluye este módulo? 🧠 Introducción a la Metodología VAI (visión + estructura completa) 💬 Prompts base listos para empezar a aplicar IA de inmediato 📢 Fundamentos de publicidad en Meta Ads (nivel inicial) 🧩 Casos simples de uso para entender la aplicación real 📄 Plantillas básicas listas para usar en tu negocio",
            "Beneficio principal": "Aprenderás a dar tus primeros pasos con la Metodología VAI, entendiendo cómo aplicar la IA, crear tus primeras estrategias y empezar a generar resultados reales desde cero.",
            "Link de Pago Plan": "https://pay.hotmart.com/B106162955H?off=f8fa87yy",
            "Mensualidad": 0,
            "Que Incluye la Mensualidad": "NO",
            "Link de Pago Mensualidad": ""
        },
        {
            "Plan": "Plan Pro",
            "Precio": 225,
            "Qué incluye": "Curso y Asesoria Completa para la Implementación de la Metodología VAI, Asesoria en Marketin y Publicidad, Automatización de las ventas con Agente de Ventas IAQué obtienes? 🧠 Curso completo para la implementación de la Metodología VAI 📊 Asesoría en marketing y publicidad digital 🤖 Automatización de ventas con Agente de Ventas con IA 🎯 Estrategias para mejorar conversión y resultados ⚙️ ",
            "Beneficio principal": "Lo que lograrás 💰 Optimizar y automatizar tu proceso de ventas 🚀 Implementar sistemas de IA en tu negocio 📈 Mejorar el rendimiento de tus campañas y resultados",
            "Link de Pago Plan": "https://pay.hotmart.com/B106162955H?off=fiylp4i8",
            "Mensualidad": 100,
            "Que Incluye la Mensualidad": "Mejoras+ Soporte + Actulización del Agente de Ventas IA",
            "Link de Pago Mensualidad": "https://pay.hotmart.com/B106162955H?off=oijv58rj"
        },
        {
            "Plan": "Plan Empresarial ",
            "Precio": 500,
            "Qué incluye": "📚 ¿Qué incluye? 🧠 Curso completo de implementación de la Metodología VAI 📊 Asesoría en marketing y publicidad digital 🤖 Automatización de ventas con Agente de Ventas con IA 🎯 Creación e implementación de estrategias de conversión 👨‍💻 Equipo profesional para ti No estás solo. Contarás con un equipo especializado que se encarga de: 🎨 Diseño de piezas publicitarias 📢 Creación y gestión de campañas en Meta Ads 🔍 Optimización diaria de anuncios para mejores resultados 📈 Análisis constante del rendimiento 📦 Material listo para usar 🧩 Te entregamos todo el material publicitario listo 🚀 No tienes que preocuparte por la creación de anuncios ⚙️ Nosotros nos encargamos de la ejecución y mejora continua ",
            "Beneficio principal": "💡 Resultado final Te enfocas en tu negocio, mientras nosotros nos encargamos de: crear, automatizar y optimizar todo tu sistema de ventas con IA. 🤖💰",
            "Link de Pago Plan": "https://pay.hotmart.com/B106162955H?off=vlptt99p",
            "Mensualidad": 250,
            "Que Incluye la Mensualidad": "mejora + soporte + resultados sostenidos+ mentorias y diseño Publicitario Completo+ Actualizaciones del agente de Ventas IA",
            "Link de Pago Mensualidad": "https://pay.hotmart.com/B106162955H?off=wp1b3j6c"
        }
    ],
    "Links Hub": [
        {
            "Links": "Plan Base",
            "Unnamed: 1": "https://pay.hotmart.com/B106162955H?off=f8fa87yy"
        },
        {
            "Links": "Plan Pro",
            "Unnamed: 1": "https://pay.hotmart.com/B106162955H?off=fiylp4i8"
        },
        {
            "Links": "Plan Empresarial ",
            "Unnamed: 1": "https://pay.hotmart.com/B106162955H?off=vlptt99p"
        },
        {
            "Links": "Pagina del producto",
            "Unnamed: 1": "https://pay.hotmart.com/B106162955H?off=wp1b3j6c"
        },
        {
            "Links": "link whatsapp",
            "Unnamed: 1": ""
        },
        {
            "Links": "Imagen Plan Base ",
            "Unnamed: 1": "https://drive.google.com/file/d/1sirLqL7erc8KpimM0PSTR46QEuOo9A3_/view?usp=drive_link"
        },
        {
            "Links": "Imagen Plan Pro",
            "Unnamed: 1": "https://drive.google.com/file/d/1FYuNJsMq3U8wc2-4abdeqMSkfRT-SvUH/view?usp=drive_link"
        },
        {
            "Links": "Imagen Plan Empresarial",
            "Unnamed: 1": "https://drive.google.com/file/d/1uNqoFl3IbiUUExuzbwBBVngmIavh-wZ6/view?usp=drive_link"
        },
        {
            "Links": "Imagen Comparacion",
            "Unnamed: 1": "https://drive.google.com/file/d/1HMwi2tpeRk3InlrivOvHIuD38T_bxJlH/view?usp=drive_link"
        }
    ]
}

# ============ FUNCIONES PRINCIPALES ============
def obtener_plan(nombre_plan):
    for plan in DATA['Planes']:
        if nombre_plan.lower() in plan['Plan'].lower():
            return plan
    return None

def obtener_link(tipo):
    for link in DATA['Links Hub']:
        if tipo.lower() in link['Links'].lower():
            return link['Unnamed: 1']
    return None

def luna_responder(mensaje_usuario, estado_conversacion={}):
    mensaje = mensaje_usuario.lower()
    
    if any(p in mensaje for p in ['hola', 'info', 'planes', 'buenas', 'buenos']) and not estado_conversacion:
        return {
            'respuesta': "¡Hola! 👋 Soy Luna, tu asistente de IA para ventas. ¿A qué te dedicas?",
            'estado': {'paso': 'detectar_nicho'}
        }
    
    if 'precio' in mensaje or 'costo' in mensaje or 'vale' in mensaje:
        plan = obtener_plan('Plan Pro')
        texto = f"El Plan Pro vale ${plan['Precio']} USD pago único + ${plan['Mensualidad']}/mes de soporte.\n\n"
        texto += f"✅ {plan['Beneficio principal']}\n\n"
        texto += f"Link: {plan['Link de Pago Plan']}\n\n¿Lo activamos?"
        return {'respuesta': texto, 'estado': estado_conversacion}
    
    return {
        'respuesta': "No entendí bien 😅 ¿Me dices a qué te dedicas o qué duda tienes sobre los planes?",
        'estado': estado_conversacion
    }

# ============ API WEBHOOK PARA MAKE ============
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    mensaje = data.get('mensaje', '')
    estado = data.get('estado', {})
    
    resultado = luna_responder(mensaje, estado)
    
    return jsonify({
        "respuesta": resultado['respuesta'],
        "estado": resultado['estado']
    })

if __name__ == '__main__':
    print("🚀 Luna Bot iniciado")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)