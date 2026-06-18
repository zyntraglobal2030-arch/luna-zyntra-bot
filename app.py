"""
Bot Helper - codigoIA_7_1 con Webhook para Make/WhatsApp
Funciones + API Flask lista para integrar con Make, ManyChat, etc
Generado automáticamente el 18 Jun 2026
"""

from flask import Flask, request, jsonify
from difflib import get_close_matches
import os

app = Flask(__name__)

# ============ RUTAS PARA RENDER - AGREGADAS ============
@app.route("/")
def home():
    # Render hace health check aquí y necesita 200 OK
    return "Luna Zyntra Bot Online", 200

@app.route("/health")
def health():
    # Health check adicional para monitoreo
    return jsonify(status="ok", objeciones_cargadas=len(DATA['objecciones'])), 200

# ============ DATA CARGADA ============
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
    "Para quien es": [
        {
            "Si en tu lista decía...": "Emprendedores, Startups, Tiendas online",
            "Ahora cae en Vertical": "Emprendedor Digital",
            "Plan": "Pro"
        },
        {
            "Si en tu lista decía...": "Abogados, Psicólogos, Dentistas, Contadores",
            "Ahora cae en Vertical": "Servicios Profesionales",
            "Plan": "Pro"
        },
        {
            "Si en tu lista decía...": "Tiendas de ropa, calzado, tecnología, E-commerce",
            "Ahora cae en Vertical": "E-commerce/Tiendas",
            "Plan": "Pro"
        },
        {
            "Si en tu lista decía...": "Diseñadores, Community, Freelancers, Agencias pequeñas",
            "Ahora cae en Vertical": "Agencias/Freelancers",
            "Plan": "Pro"
        },
        {
            "Si en tu lista decía...": "Restaurantes, Peluquerías, Spa, Cafeterías, Hoteles pequeños",
            "Ahora cae en Vertical": "Negocios Locales Físicos",
            "Plan": "Pro"
        },
        {
            "Si en tu lista decía...": "Consultores, Coaches, Fotógrafos, Arquitectos",
            "Ahora cae en Vertical": "Profesionales Independientes",
            "Plan": "Pro"
        },
        {
            "Si en tu lista decía...": "Empresas medianas, B2B, Consultoría, Distribuidores",
            "Ahora cae en Vertical": "Empresa Mediana 10-50",
            "Plan": "Empresarial"
        },
        {
            "Si en tu lista decía...": "Empresas grandes, Corporaciones, Multinacionales",
            "Ahora cae en Vertical": "B2B/Servicios Corp",
            "Plan": "Empresarial"
        },
        {
            "Si en tu lista decía...": "Cadenas de tiendas, Retailers, Franquicias",
            "Ahora cae en Vertical": "E-commerce Grande/Retail",
            "Plan": "Empresarial"
        },
        {
            "Si en tu lista decía...": "Clínicas, Hospitales, Universidades, Colegios",
            "Ahora cae en Vertical": "Salud/Educación",
            "Plan": "Empresarial"
        },
        {
            "Si en tu lista decía...": "Inmobiliarias, Constructoras, Desarrolladoras",
            "Ahora cae en Vertical": "Franquicias/Inmobiliarias",
            "Plan": "Empresarial"
        },
        {
            "Si en tu lista decía...": "Estudiantes, Sin experiencia, Principiantes",
            "Ahora cae en Vertical": "Principiantes IA",
            "Plan": "Base"
        },
        {
            "Si en tu lista decía...": "Microempresas, Negocios familiares, Tiendas pequeñas",
            "Ahora cae en Vertical": "Micro-Comercio Local",
            "Plan": "Base"
        },
        {
            "Si en tu lista decía...": "Dueños de pequeños negocios, Negocios en etapa inicial",
            "Ahora cae en Vertical": "Emprendedor Inicial",
            "Plan": "Base"
        }
    ],
    "objecciones": [
        {
            "Plan": "Plan Base",
            "Objeción": "Es muy caro",
            "Respuesta que Cierra": "La inversión es de $45 USD, pago único. Analicemos el costo de no actuar: 3 citas de $50 perdidas al mes por no responder fuera de horario son $150. En 7 días la herramienta se paga sola. Hotmart ofrece 7 días de garantía total. Si no es útil, se solicita reembolso sin preguntas. ¿Lo prueba?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Es muy caro",
            "Respuesta que Cierra": "La inversión total del primer mes es de $250 USD. Ese es pago único de setup. A partir del mes 2, solo paga $100 USD/mes de Soporte, Actualización y Asesoría si decide continuar. Con el método aplicado, clientes recuperan los $225 en la primera semana con 2-3 ventas de $40-$60. La mensualidad de $100 se vuelve imperceptible frente al nuevo flujo de ingresos. Incluye 30 días de garantía: si no generamos mínimo 5 clientes nuevos, devuelvo los $250 y el primer mes de soporte va sin costo. Usted no paga mes 2 si no hay resultados. ¿Qué riesgo real existe?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Es muy caro",
            "Respuesta que Cierra": "La inversión del primer mes es de $500 USD. Ese es el setup inicial, pago único. Desde el mes 2, la inversión es de $225 USD/mes por Soporte, Actualizaciones, Asesoría, Creación y Administración de Marketing y Publicidad. El retorno promedio es de 5x a 10x en 90 días. Contrato por resultados: si en 60 días no hay un incremento mínimo del 20% en facturación, el tercer mes de soporte no se factura. ¿Revisamos sus métricas para proyectar el ROI y validar si califica?"
        }
    ],
    "FAQ": [
        {
            "Plan": "Plan Base",
            "Pregunta": "¿Qué es la Metodología VAI?",
            "Respuesta": "Es un sistema de formación que enseña fundamentos de IA aplicada a marketing. Aprende paso a paso cómo automatizar tareas básicas. Ideal si inicia desde cero."
        },
        {
            "Plan": "Plan Pro",
            "Pregunta": "¿Qué es la Metodología VAI?",
            "Respuesta": "Es un sistema práctico donde implementa IA y marketing en su negocio. Incluye plantillas y el bot básico funcional. Diseñado para aplicar, no solo aprender."
        },
        {
            "Plan": "Plan Empresarial",
            "Pregunta": "¿Qué es la Metodología VAI?",
            "Respuesta": "Es un sistema completo de implementación. Nuestro equipo configura su bot avanzado, campañas de Meta Ads y optimización. Usted solo aprueba estrategia."
        }
    ],
    "Segmentación": [
        {
            "Plan": "Base",
            "Vertical": "Principiantes IA",
            "Gatillo_Dolor": "No sé nada de IA, me da miedo la tecnología",
            "Avatar_Decisor": "Estudiante, Desempleado, Curioso",
            "Ticket_Promedio": "$0-$50",
            "Precio_Mes_1": "$45 USD",
            "Precio_Mes_2+": 0,
            "Garantía": "7 días Hotmart",
            "Ángulo_Venta": "Tu primer bot en 1h sin código. Si no le gusta, reembolso total",
            "Prioridad": 3
        },
        {
            "Plan": "Base",
            "Vertical": "Micro-Comercio",
            "Gatillo_Dolor": "Respondo 'info' 3h al día y no vendo",
            "Avatar_Decisor": "Peluquero, Tendero, Vendedor solo",
            "Ticket_Promedio": "$20-$100",
            "Precio_Mes_1": "$45 USD",
            "Precio_Mes_2+": 0,
            "Garantía": "7 días Hotmart",
            "Ángulo_Venta": "Deja de ser esclavo del WhatsApp por $45. Se paga en 7 días",
            "Prioridad": 2
        },
        {
            "Plan": "Base",
            "Vertical": "Emprendedor Inicial",
            "Gatillo_Dolor": "Pierdo clientes de noche porque no contesto",
            "Avatar_Decisor": "Dueño solo, Side hustle",
            "Ticket_Promedio": "$50-$200",
            "Precio_Mes_1": "$45 USD",
            "Precio_Mes_2+": 0,
            "Garantía": "7 días Hotmart",
            "Ángulo_Venta": "$45 vs $300/mes perdidos por no contestar 24/7",
            "Prioridad": 2
        },
        {
            "Plan": "Pro",
            "Vertical": "Servicios Profesionales",
            "Gatillo_Dolor": "Agenda en WhatsApp, 40% no-shows me matan",
            "Avatar_Decisor": "Psicólogo, Abogado, Dentista, Coach",
            "Ticket_Promedio": "$100-$500",
            "Precio_Mes_1": "$250 USD",
            "Precio_Mes_2+": "$100 USD/mes",
            "Garantía": "30 días: 5 clientes o devolución",
            "Ángulo_Venta": "Reduce no-shows 70%. Setup $250. Mes 2 solo $100 si agenda +10 citas",
            "Prioridad": 1
        },
        {
            "Plan": "Pro",
            "Vertical": "E-commerce/Tiendas",
            "Gatillo_Dolor": "Carritos abandonados, no doy abasto con DMs",
            "Avatar_Decisor": "Dueño Shopify, Tienda IG",
            "Ticket_Promedio": "$30-$200",
            "Precio_Mes_1": "$250 USD",
            "Precio_Mes_2+": "$100 USD/mes",
            "Garantía": "30 días: 5 clientes o devolución",
            "Ángulo_Venta": "Recupera 15% de carritos. Paga $100/mes solo si vende",
            "Prioridad": 1
        },
        {
            "Plan": "Pro",
            "Vertical": "Emprendedor Digital",
            "Gatillo_Dolor": "Leads de Instagram se enfrían, no convierto",
            "Avatar_Decisor": "Infoproductor, Mentor, Afiliado",
            "Ticket_Promedio": "$200-$2000",
            "Precio_Mes_1": "$250 USD",
            "Precio_Mes_2+": "$100 USD/mes",
            "Garantía": "30 días: 5 clientes o devolución",
            "Ángulo_Venta": "Setup $250. Si no trae 5 clientes en 30 días, devuelvo todo",
            "Prioridad": 1
        },
        {
            "Plan": "Pro",
            "Vertical": "Negocios Locales",
            "Gatillo_Dolor": "Reseñas malas por no contestar rápido",
            "Avatar_Decisor": "Dueño Restaurante, Barbería, Spa",
            "Ticket_Promedio": "$25-$100",
            "Precio_Mes_1": "$250 USD",
            "Precio_Mes_2+": "$100 USD/mes",
            "Garantía": "30 días: 5 clientes o devolución",
            "Ángulo_Venta": "1 cliente enojado cuesta $500. Bot cuesta $250 setup",
            "Prioridad": 1
        },
        {
            "Plan": "Pro",
            "Vertical": "Agencias/Freelancers",
            "Gatillo_Dolor": "Vendo horas, cliente regatea, no escalo",
            "Avatar_Decisor": "Diseñador, Marketer, CM Freelance",
            "Ticket_Promedio": "$500-$2000",
            "Precio_Mes_1": "$250 USD",
            "Precio_Mes_2+": "$100 USD/mes",
            "Garantía": "30 días: 5 clientes o devolución",
            "Ángulo_Venta": "Vende sistemas, no tu tiempo. Setup $250 único",
            "Prioridad": 2
        },
        {
            "Plan": "Pro",
            "Vertical": "Profesionales Independientes",
            "Gatillo_Dolor": "Si no trabajo yo, no entra plata",
            "Avatar_Decisor": "Consultor, Fotógrafo, Arquitecto",
            "Ticket_Promedio": "$300-$5000",
            "Precio_Mes_1": "$250 USD",
            "Precio_Mes_2+": "$100 USD/mes",
            "Garantía": "30 días: 5 clientes o devolución",
            "Ángulo_Venta": "Libera 20h/mes. Si no lo hace, devuelvo los $250",
            "Prioridad": 1
        },
        {
            "Plan": "Empresarial",
            "Vertical": "Empresa Mediana",
            "Gatillo_Dolor": "3+ sedes, cada una atiende distinto, caos",
            "Avatar_Decisor": "Gerente Ops, CEO 10-50 empleados",
            "Ticket_Promedio": "$5K-$20K/mes",
            "Precio_Mes_1": "$500 USD",
            "Precio_Mes_2+": "$225 USD/mes",
            "Garantía": "60 días: +20% facturación o mes 3 gratis",
            "Ángulo_Venta": "Setup $500. Desde mes 2 solo $225/mes. Estandariza 3 sedes ya",
            "Prioridad": 1
        },
        {
            "Plan": "Empresarial",
            "Vertical": "B2B/Servicios Corp",
            "Gatillo_Dolor": "Ciclo de venta 90 días, vendedores pierden leads",
            "Avatar_Decisor": "Director Comercial, Ventas B2B",
            "Ticket_Promedio": "$10K-$100K/mes",
            "Precio_Mes_1": "$500 USD",
            "Precio_Mes_2+": "$225 USD/mes",
            "Garantía": "60 días: +20% facturación o mes 3 gratis",
            "Ángulo_Venta": "ROI 5x-10x en 90 días o no paga mes 3 de $225",
            "Prioridad": 1
        },
        {
            "Plan": "Empresarial",
            "Vertical": "E-commerce Grande",
            "Gatillo_Dolor": "500+ chats/día, 5 personas de soporte quemadas",
            "Avatar_Decisor": "Head E-commerce, CMO Retail",
            "Ticket_Promedio": "$50K+/mes",
            "Precio_Mes_1": "$500 USD",
            "Precio_Mes_2+": "$225 USD/mes",
            "Garantía": "60 días: +20% facturación o mes 3 gratis",
            "Ángulo_Venta": "Reduce 60% carga operativa. $225/mes vs $2,000 nómina",
            "Prioridad": 1
        },
        {
            "Plan": "Empresarial",
            "Vertical": "Salud/Educación",
            "Gatillo_Dolor": "No-shows cuestan $10K/mes, agenda manual",
            "Avatar_Decisor": "Director Clínica, Rector Universidad",
            "Ticket_Promedio": "$20K+/mes",
            "Precio_Mes_1": "$500 USD",
            "Precio_Mes_2+": "$225 USD/mes",
            "Garantía": "60 días: +20% facturación o mes 3 gratis",
            "Ángulo_Venta": "Cada no-show son $100. Sistema los baja 70%",
            "Prioridad": 1
        },
        {
            "Plan": "Empresarial",
            "Vertical": "Franquicias/Inmobiliarias",
            "Gatillo_Dolor": "50 sedes, marca inconsistente, no hay control",
            "Avatar_Decisor": "CEO, Director Expansión",
            "Ticket_Promedio": "$100K+/mes",
            "Precio_Mes_1": "$500 USD",
            "Precio_Mes_2+": "$225 USD/mes",
            "Garantía": "60 días: +20% facturación o mes 3 gratis",
            "Ángulo_Venta": "Un bot para 50 sedes. Control total por $225/mes",
            "Prioridad": 1
        },
        {
            "Plan": "Empresarial",
            "Vertical": "Agencias/SaaS",
            "Gatillo_Dolor": "Quiero revender IA a mis clientes y escalar",
            "Avatar_Decisor": "Dueño Agencia, CTO SaaS",
            "Ticket_Promedio": "$5K+/mes por cliente",
            "Precio_Mes_1": "$500 USD",
            "Precio_Mes_2+": "$225 USD/mes",
            "Garantía": "60 días: +20% facturación o mes 3 gratis",
            "Ángulo_Venta": "White label. Setup $500. Cobra $2K/mes a cada cliente",
            "Prioridad": 1
        }
    ],
    "Nichos": [
        {
            "Nicho": "Odontólogos",
            "Dolor Principal": "Pierden citas porque nadie contesta WhatsApp después de las 6pm y fines de semana",
            "Mensaje del Bot": "Parce Dr. ¿Cuántos pacientes al mes pierdes porque te escriben a las 8pm preguntando \"precio blanqueamiento\" y nadie responde hasta el otro día? Mi bot agenda por ti 24/7, pide foto de la sonrisa, califica si es pa' ortodoncia o limpieza, y te deja la cita lista en tu calendario. Tú solo llegas a atender.",
            "Cierre Específico": "Si el bot te agenda 4 pacientes extra al mes de $200, ya pagaste el Plan Pro del año. ¿Te muestro cómo quedaría con el nombre de tu clínica? Link Pro: https://pay.hotmart.com/B106162955H?off=fiylp4i8"
        },
        {
            "Nicho": "Coaches / Infoproductores",
            "Dolor Principal": "Viven pegados al DM respondiendo \"info\" y no tienen tiempo de crear contenido",
            "Mensaje del Bot": "Bro, si vendes mentorías de $500, cada hora que pasas diciendo \"te mando info al DM\" te cuesta plata. Mi bot responde, filtra a los que no tienen dinero, agenda llamada solo con los calificados y te manda el perfil antes de entrar a Zoom. Tú solo vendes, no persigues.",
            "Cierre Específico": "Un cliente de $500 paga 2 años del Pro. Si el bot te filtra 1 cliente bueno a la semana, ya ganaste. ¿Lo montamos con tu script de ventas? Link Pro: https://pay.hotmart.com/B106162955H?off=fiylp4i8"
        },
        {
            "Nicho": "E-commerce / Tiendas",
            "Dolor Principal": "Carritos abandonados y \"¿tienen en talla M?\" que nunca terminan en venta",
            "Mensaje del Bot": "¿Sabes cuánta gente te escribe \"¿hay stock?\" y se va porque respondes 3 horas después? Mi bot responde en 5 seg, muestra fotos, dice precio, talla, colores, y manda link de pago directo. Si abandona carrito, le escribe a las 2h: \"Oye, ¿se te olvidó algo? Te guardé la talla M\".",
            "Cierre Específico": "Si recuperas 10 carritos de $30 al mes, son $300. El Pro vale $250 una vez. ¿Cuántos carritos pierdes al día? Actívalo ya: https://pay.hotmart.com/B106162955H?off=fiylp4i8"
        },
        {
            "Nicho": "Inmobiliarias",
            "Dolor Principal": "Leads fríos que preguntan por 20 apartamentos y nunca agendan visita",
            "Mensaje del Bot": "El bot hace el trabajo sucio: pregunta presupuesto, zona, # habitaciones, y solo te pasa el lead cuando dice \"sí tengo $400M de cuota inicial\". Te llega a WhatsApp: \"Juan, apto en Cedritos, 3 hab, presupuesto 500M, agenda visita sábado 10am\". Tú solo muestras y cierras.",
            "Cierre Específico": "Una comisión de venta paga 10 años de Empresarial. ¿Cuántos leads basura filtras al mes? Nosotros lo hacemos por ti: https://pay.hotmart.com/B106162955H?off=vlptt99p"
        },
        {
            "Nicho": "Restaurantes / Delivery",
            "Dolor Principal": "Pedidos por WhatsApp mal tomados, dirección mal, no contestan en hora pico",
            "Mensaje del Bot": "Hola, 2 pizzas hawaianas ... 40 min después: \"¿a qué dirección?\". Cliente ya pidió en otro lado. El bot toma pedido completo: producto, dirección, medio de pago, hora de entrega. Te llega a cocina listo pa' imprimir. Cero errores, cero chats eternos.",
            "Cierre Específico": "Si pierdes 2 pedidos de $50 al día por demora, son $3000 al mes. El Pro son $250. ¿Seguimos perdiendo plata? Link: https://pay.hotmart.com/B106162955H?off=fiylp4"
        },
        {
            "Nicho": "Gimnasios / Entrenadores",
            "Dolor Principal": "No cierran membresías porque la gente pregunta precio y nunca vuelve",
            "Mensaje del Bot": "¿Cuántas personas te escriben \"precio del mes\" y desaparecen? El bot les responde en 1 min, les manda tour virtual, los reta con \"te guardo precio promo solo hoy\" y agenda clase de prueba gratis. Tú recibes: \"Ana, clase prueba martes 7am, objetivo bajar 5kg\". Solo cierras.",
            "Cierre Específico": "Si 3 personas de prueba se vuelven membresía de $80/mes, son $240/mes. El Pro se paga en 1 mes. ¿Cuántos \"info\" te llegan al día? Link Pro: https://pay.hotmart.com/B106162955H?off=fiylp4i8"
        },
        {
            "Nicho": "Talleres Mecánicos / Autolavados",
            "Dolor Principal": "Clientes llaman todo el día \"¿cuánto vale cambio aceite?\" y colapsan la recepción",
            "Mensaje del Bot": "El bot cotiza en automático: \"Cambio aceite para Mazda 3 2018: $180.000. ¿Agendo pa' mañana 9am?\" Pide placa, foto del tablero si hay falla, y te deja el carro agendado con repuestos listos. Cero llamadas perdidas.",
            "Cierre Específico": "Un cambio de aceite + alineación son $300. Con 1 cliente que no perdiste, pagaste el Pro 250usd . ¿Seguimos perdiendo por no contestar? https://pay.hotmart.com/B106162955H?off=fiylp4i8"
        },
        {
            "Nicho": "Abogados / Contadores",
            "Dolor Principal": "Pierden clientes porque no responden rápido y se van con el que sí contestó",
            "Mensaje del Bot": "Cuando alguien busca abogado es urgente. Si te escribe \"me demandaron\" a las 10pm y respondes al otro día, ya contrató otro. El bot responde ya, pide resumen del caso, filtra si es tu tipo de cliente y agenda llamada de 15 min paga. Solo hablas con quien puede pagarte.",
            "Cierre Específico": "Una asesoría de $400 paga 2 años de Pro. ¿Cuántos casos buenos dejas ir al mes por lento? Link: https://pay.hotmart.com/B106162955H?off=fiylp4i8"
        },
        {
            "Nicho": "Agencias de Viajes",
            "Dolor Principal": "Cotizaciones eternas que el cliente usa pa' comparar y compra en otra parte",
            "Mensaje del Bot": "Cliente: \"cotízame Cancún\". Tú duras 2 días. Él ya compró en Despegar. El bot cotiza en 3 min: vuelos + hotel + tours, con tus precios, y dice \"te guardo cupo 2h con 10% off\". Si no compra, hace follow-up: \"¿Te ayudo a ajustar presupuesto?\"",
            "Cierre Específico": "Una venta de paquete de $1200 te deja $150 comisión. Eso es el Pro + mensualidad de 6 meses. ¿Seguimos cotizando lento? https://pay.hotmart.com/B106162955H?off=fiylp4i8"
        },
        {
            "Nicho": "Spa / Estéticas",
            "Dolor Principal": "No llenan agenda porque dependen de que la recepcionista recuerde escribir a las clientas",
            "Mensaje del Bot": "El bot hace el trabajo: \"Hola Lina, hace 30 días fue tu facial. ¿Reagendamos con 15% off esta semana?\". Agenda, pide anticipo por Nequi, y te llena martes y miércoles que siempre están muertos.",
            "Cierre Específico": "Si llenas 4 huecos de $60 c/u al mes, son $240. Ya pagaste el Pro. ¿Dejamos que la agenda siga vacía? Link: https://pay.hotmart.com/B106162955H?off=fiylp4i8"
        },
        {
            "Nicho": "Funerarias",
            "Dolor Principal": "La gente llama en crisis y si no contestas ya, se van con la competencia",
            "Mensaje del Bot": "Cuando alguien escribe a las 2am \"murió mi papá\", no puede esperar. El bot responde en 10 seg: \"Lamentamos tu pérdida. Te llamamos ya\" + alerta a tu celular. Toma datos, cotiza plan y agenda todo. En ese momento no vendes, das paz. Y eso fideliza.",
            "Cierre Específico": "Una servicio exequial son $2000 USD. Perder 1 por no contestar duele. El Empresarial te da sistema 24/7. ¿Hablamos? https://pay.hotmart.com/B106162955H?off=vlptt99p"
        },
        {
            "Nicho": "Veterinarias",
            "Dolor Principal": "Mi perro no come a las 11pm y no saben si es urgencia o no",
            "Mensaje del Bot": "El bot triage: \"¿Vomita sangre? ¿Respira mal?\" Si es grave → \"Traelo ya, el doc te espera\". Si no → \"Agenda mañana 9am + te mando tips\". Filtras sustos, salvas vidas y no te desvelas por gases.",
            "Cierre Específico": "Una hospitalización de $300 paga el Pro. ¿Cuántas urgencias falsas atiendes al mes gratis? Link Pro: https://pay.hotmart.com/B106162955H?off=fiylp4i8"
        },
        {
            "Nicho": "Psicólogos / Terapeutas",
            "Dolor Principal": "Pacientes cancelan última hora y dejan huecos que no facturas",
            "Mensaje del Bot": "El bot confirma cita 24h antes por WhatsApp: \"Hola, ¿nos vemos mañana 4pm?\". Si dice \"no puedo\", el bot ofrece el hueco a tu lista de espera automático. Cero agenda vacía.",
            "Cierre Específico": "1 sesión de $70 perdida al mes ya paga el Pro. ¿Seguimos con huecos? https://pay.hotmart.com/B106162955H?off=fiylp4i8"
        },
        {
            "Nicho": "Constructoras / Remodelación",
            "Dolor Principal": "Cotizan a 20 personas y solo 1 compra. Pierden tiempo en visitas",
            "Mensaje del Bot": "Bot pide fotos del espacio, m2, presupuesto real y dice: \"Con $20M te hacemos esto\". Solo agendás visita si el cliente ya dijo \"sí tengo la plata\". No quemas gasolina gratis.",
            "Cierre Específico": "Una obra de $15M deja $3M utilidad. El Empresarial son $500. ¿Cuántas visitas haces al mes sin cerrar? https://pay.hotmart.com/B106162955H?off=vlptt99p"
        },
        {
            "Nicho": "Otro / No sé mi nicho",
            "Dolor Principal": "No sabes cómo un bot te ayuda en tu negocio específico",
            "Mensaje del Bot": "Parce, si tienes clientes que te escriben por WhatsApp, ya te sirve. Dime qué vendes y en 2 min te digo cómo el bot te consigue 3 ventas extra al mes sin tú hacer nada. ¿Qué vendes?",
            "Cierre Específico": "Si no te aumento ventas en 30 días, te devuelvo la plata. ¿Cuál es el riesgo? Prueba Pro: https://pay.hotmart.com/B106162955H?off=fiylp4i8"
        },
        {
            "Nicho": "Creadores OnlyFans / Modelos webcam",
            "Dolor Principal": "Pierden suscriptores porque no responden DMs 24/7 y no logran vender contenido custom",
            "Mensaje del Bot": "Amor, ¿cuántos DMs de \"hazme video diciendo mi nombre\" pierdes mientras duermes? Mi bot responde al tiro, coquetea por ti, filtra a los tacaños, vende tu pack de $50, tus fotos custom de $100 y agenda videollamada privada. Tú solo grabas y cobras. Él trabaja, tú facturas.",
            "Cierre Específico": "Si el bot te cierra 5 ventas de $50 al mes, son $250. El Pro vale $225 una vez. ¿Vas a seguir perdiendo DMs a las 3am o automatizamos? Link Pro: https://pay.hotmart.com/B106162955H?off=fiylp4i8"
        },
        {
            "Nicho": "Cliente Internacional   ",
            "Dolor Principal": "     No maneja pesos COP, tiene horario diferente y quiere trato directo",
            "Mensaje del Bot": "Para clientes fuera de Colombia manejo agenda directa conmigo por WhatsApp pa’ cuadrar moneda, horarios y forma de pago. Así no perdemos tiempo. Dale clic aquí y hablamos ya: https://wa.me/57TU_NUMERO?text=Hola%20Jorge,%20soy%20de%20[País]%20y%20quiero%20info%20del%20bot        Te atiendo yo personalmente. Nada de bots con internacionales, puro WhatsApp VIP.",
            "Cierre Específico": ""
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
    ],
    "Cierre
