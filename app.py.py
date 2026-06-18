"""
Bot Helper - codigoIA_7_1 con Webhook para Make/WhatsApp
Funciones + API Flask lista para integrar con Make, ManyChat, etc
Generado automáticamente el 18 Jun 2026
"""

from flask import Flask, request, jsonify
from difflib import get_close_matches

app = Flask(__name__)

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
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No tengo dinero ahora",
            "Respuesta que Cierra": "Este plan existe por esa razón: es el de menor inversión, $45 una vez, sin mensualidades. Si $45 es una barrera, el desafío es de ventas, no de la herramienta. Cada mensaje sin responder es ingreso perdido. ¿Cuántos mensajes sin atender tuvo esta semana?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No tengo dinero ahora",
            "Respuesta que Cierra": "Si el flujo de caja es ajustado, recomiendo iniciar con el Plan Base de $45. Importante: no invertir $225 de setup + $100/mes en automatizar significa seguir intercambiando tiempo por dinero. Hotmart permite dividir el setup en 3 pagos de $83. ¿Esa opción facilita el inicio?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No tengo dinero ahora",
            "Respuesta que Cierra": "Si actualmente no hay presupuesto de $500 de setup + $225/mes para adquisición, este servicio no es el paso correcto aún. Sugiero empezar con el Plan Pro. Nota: mientras se decide, la competencia sí está invirtiendo. ¿Evaluamos el costo de oportunidad?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No está en mi presupuesto",
            "Respuesta que Cierra": "Los presupuestos deben incluir adquisición de clientes. Esto no es un gasto, es un activo que trabaja 24/7 por $45. Si el presupuesto actual no contempla conseguir más clientes, debe ajustarse. ¿Cuánto se pierde al mes por leads sin atender?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No está en mi presupuesto",
            "Respuesta que Cierra": "Si el presupuesto para marketing es $0, hay un riesgo alto para el negocio. El Plan Pro requiere $225 de setup + $100/mes. Es el punto intermedio entre formación y ejecución. Se puede pagar el setup en 3 cuotas de $83 vía Hotmart. ¿Validamos esa alternativa?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No está en mi presupuesto",
            "Respuesta que Cierra": "Los presupuestos empresariales asignan entre 10% y 15% a adquisición de clientes. $225/mes para facturar $5K+ está dentro de ese rango. Si su estructura no lo contempla, es momento de revisar el modelo. ¿Cuál es su CAC actual?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Lo veo costoso para lo que ofrece",
            "Respuesta que Cierra": "Comparemos: ManyChat cobra $15/mes solo por botones. En 3 meses ya pagó más que esto. Este plan incluye metodología + bot básico por $45 una vez. Si en 7 días no retorna 3x, solicita reembolso. ¿Lo valida?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Lo veo costoso para lo que ofrece",
            "Respuesta que Cierra": "No se venden videos, se venden clientes. El plan integra bot + Meta Ads por $225 setup + $100/mes. Si hoy paga $10 por lead y lo reducimos a $4, con 63 leads recupera el setup. La mensualidad se paga con 2 ventas de $50. ¿Cuánto paga por lead hoy?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Lo veo costoso para lo que ofrece",
            "Respuesta que Cierra": "El valor está en el servicio completo: ads + bot + closer + reportes por $500 setup + $225/mes. Una agencia tradicional cobra $2,000+ solo por ads. Si no entregamos mínimo 5x ROAS, no se factura el tercer mes de soporte. ¿Qué agencia ofrece ese compromiso?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No estoy seguro de que lo valga",
            "Respuesta que Cierra": "Es válido tener dudas. Por eso Hotmart da 7 días de garantía total. Puede probarlo y si en 7 días no agenda 1 cita o no genera 1 venta, solicita la devolución. Si vende 1 producto de $50, ya recuperó la inversión. ¿Lo prueba sin riesgo?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No estoy seguro de que lo valga",
            "Respuesta que Cierra": "Para eliminar la incertidumbre, damos 30 días de garantía. Si no generamos mínimo 10 citas calificadas o $675 en ventas, extendemos el servicio sin costo hasta cumplirlo. El setup de $225 se protege. ¿Qué métrica específica necesita ver para validar?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No estoy seguro de que lo valga",
            "Respuesta que Cierra": "La validación es con datos. Agendemos 15 min sin costo: le muestro la proyección con sus números reales. Si no ve potencial claro de 30%+ en crecimiento, no avanzamos. ¿Qué horario le funciona? Mañana 10am o 4pm."
        },
        {
            "Plan": "Plan Base",
            "Objeción": "He visto opciones más baratas",
            "Respuesta que Cierra": "Existen opciones más económicas. ChatGPT es gratis y no vende. ManyChat $15/mes y solo da menús. Esta herramienta está diseñada para cerrar ventas por $45 única vez. ¿El objetivo es ahorrar $30 o facturar $300 extra al mes?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "He visto opciones más baratas",
            "Respuesta que Cierra": "¿Más económico que $225 de setup + $100/mes? Sí, un curso de $45. Pero un curso no responde mensajes a las 2am. El Pro sí. ¿La prioridad es aprender o empezar a vender?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "He visto opciones más baratas",
            "Respuesta que Cierra": "Si encontró un servicio por menos de $500 setup + $225/mes que incluya ads + bot + closer + reportes semanales, compártalo para analizarlo. En 4 años no lo hemos visto. ¿Comparamos propuestas con el mismo alcance?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Prefiero algo gratuito",
            "Respuesta que Cierra": "Lo gratuito entrega información. Este sistema entrega implementación paso a paso por $45 una vez. Si $45 es una barrera, el desafío actual no es la herramienta. ¿Continuamos?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Prefiero algo gratuito",
            "Respuesta que Cierra": "Lo gratuito es para aprender. El Pro es para ejecutar. Puede invertir 100 horas en YouTube sin costo o 48 horas y tener el sistema vendiendo. El setup de $225 se paga con 1 cliente. ¿Qué genera flujo de caja más rápido?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Prefiero algo gratuito",
            "Respuesta que Cierra": "Si la facturación actual es $0, este plan no aplica. Si factura $10K/mes y evalúa opciones gratuitas para escalar, hay una desconexión estratégica. La mensualidad de $225 es el 2.25% de $10K. ¿En qué etapa está el negocio realmente?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No puedo pagar en este momento",
            "Respuesta que Cierra": "El precio queda reservado 24h. Hotmart acepta PSE, Efecty, Nequi y tarjeta. Si hoy no es posible, ¿qué fecha sí? Cada día sin sistema son clientes potenciales perdidos."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No puedo pagar en este momento",
            "Respuesta que Cierra": "Hotmart permite dividir el setup de $225 en 3 pagos de $83. Solo requiere cupo para la primera cuota. La mensualidad de $100 inicia después. Si aún así no es viable, inicie con Base y escale después. ¿Qué opción se ajusta mejor?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No puedo pagar en este momento",
            "Respuesta que Cierra": "Podemos estructurar el setup de $500 a 60 días firmando contrato trimestral, sujeto a validación financiera. La mensualidad de $225 inicia en mes 2. ¿Le comparto el borrador de contrato para revisión?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No quiero endeudarme",
            "Respuesta que Cierra": "No es deuda, es una inversión de $45, pago único. Se pierde más dejando de atender $200/mes en clientes. ¿Es mayor el riesgo de invertir $45 o de seguir perdiendo ventas?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No quiero endeudarme",
            "Respuesta que Cierra": "Hotmart difiere el setup de $225 a 12 cuotas de $21/mes. La mensualidad de $100 es operativa, no deuda. Si $21 mensuales comprometen la operación, el problema es de flujo, no de la herramienta. ¿Revisamos los números base del negocio?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No quiero endeudarme",
            "Respuesta que Cierra": "Correcto, invertir no es endeudarse. Endeudarse es tener nómina improductiva. $500 setup + $225/mes por un equipo que debe generar $5K es ROI, no pasivo. ¿Analizamos el retorno proyectado?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Necesito pensarlo",
            "Respuesta que Cierra": "Es una decisión importante. Para facilitarlo: tiene 7 días de garantía Hotmart. Puede activarlo, probarlo y si en ese lapso no ve valor, solicita reembolso. ¿Qué información específica necesita para decidir en 24h?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Necesito pensarlo",
            "Respuesta que Cierra": "La indecisión tiene costo. Mientras evalúa, la competencia implementa. Tiene 30 días de garantía: si no ve resultados, devolvemos los $225 de setup y trabajamos 1 mes de soporte gratis. ¿Qué dato concreto falta para avanzar?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Necesito pensarlo",
            "Respuesta que Cierra": "Las decisiones de escala requieren datos, no tiempo. Le propongo 15 min para auditar su embudo sin costo. Si no identifico una oportunidad clara de 30%+, no avanzamos. ¿Hoy o mañana?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No tengo tiempo ahora",
            "Respuesta que Cierra": "Precisamente por falta de tiempo existe esta solución. La implementación toma 1 hora con el video guía. Después opera solo. El tiempo se pierde respondiendo \"info\" 3h al día. ¿Le agendo 20 min para dejarlo configurado?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No tengo tiempo ahora",
            "Respuesta que Cierra": "La implementación la realizamos nosotros en 48h. Usted solo invierte 1h en aprobar contenidos iniciales. Luego libera 20h/mes. La mensualidad de $100 cubre soporte para que no use su tiempo. ¿Agendamos esa hora esta semana?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No tengo tiempo ahora",
            "Respuesta que Cierra": "El modelo Empresarial es 100% delegado. Nosotros ejecutamos todo. Usted solo revisa el reporte de 5 min semanal. La mensualidad de $225 es para que no use su tiempo operativo. Si no dispone de 5 min para escalar, evaluemos si es el momento correcto. ¿Delegamos?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Lo haré después",
            "Respuesta que Cierra": "Después tiene un costo medible: ~$300/mes en citas perdidas. La herramienta cuesta $45 hoy. Hotmart da 7 días de prueba. Si no lo usa, devuelve. ¿Qué cambia si espera?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Lo haré después",
            "Respuesta que Cierra": "Cada día sin bot se pierden 3-5 leads calificados. En 1 semana son 25 leads = $500 potenciales. ¿Postergar le cuesta $500 o invertir $250 de setup? Hagamos el cálculo."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Lo haré después",
            "Respuesta que Cierra": "Postergar 30 días impacta el trimestre completo. Los clientes que implementan hoy ven ROI en día 45. El setup de $500 se paga con 1 cliente. ¿Iniciamos esta semana para cumplir la meta del Q4 o se re-agenda?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No es mi prioridad",
            "Respuesta que Cierra": "La prioridad debe ser conseguir clientes. La inversión es $45, pago único. Si eso no es prioridad, ¿cuál sí lo es? Tiene 7 días de garantía. Si no agenda 1 cita, solicita reembolso."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No es mi prioridad",
            "Respuesta que Cierra": "Si la adquisición automatizada no es prioridad, ¿cuál es su sistema actual de crecimiento? $250 de setup + $100/mes de soporte es una implementación que libera 20h/mes de su equipo. ¿Qué prioridad le ahorra $2,000/mes en operación?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No es mi prioridad",
            "Respuesta que Cierra": "En negocios de esta escala, la adquisición es prioridad #1 por defecto. Si no lo es en su caso, hay que revisar el modelo. La mensualidad de $225 es el 4.5% de una facturación de $5K. ¿Agendamos 15 min para auditar su costo de oportunidad por no automatizar?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No puedo comprometerme ahora",
            "Respuesta que Cierra": "No es un matrimonio, es una inversión de $45, sin mensualidad. Si $45 es mucho compromiso, el desafío es de ventas, no de la herramienta. ¿Cuánto pierde por no comprometerse con vender?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No puedo comprometerme ahora",
            "Respuesta que Cierra": "El Pro requiere $250 de setup + $100/mes. Se paga solo. Si no se compromete con una herramienta que, aplicada, genera entre $400 a $800 extra el primer mes, ¿con qué sí? Hotmart permite 3 pagos del setup. ¿Es compromiso o aversión al riesgo?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No puedo comprometerme ahora",
            "Respuesta que Cierra": "El contrato mínimo es trimestral porque escalar toma 90 días. Setup $500 + $225/mes. Si no puede comprometerse 90 días con su crecimiento, el Empresarial no es para usted aún. ¿Seguimos con Pro o pausamos el proceso?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Estoy saturado de trabajo",
            "Respuesta que Cierra": "Justo por eso existe. $45 para dejar de responder \"info\" 3h/día. ¿Prefiere seguir saturado sin costo o invertir $45 para tener 3h libres al día?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Estoy saturado de trabajo",
            "Respuesta que Cierra": "El Pro automatiza el 80% de la operación. Si está saturado ejecutando tareas de $10/hora, ¿cuándo ejecuta las de $100/hora? $250 de setup + $100/mes de soporte compra tiempo. ¿Cuánto vale su hora?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Estoy saturado de trabajo",
            "Respuesta que Cierra": "Delegue 100%. Nosotros ejecutamos, usted solo aprueba estrategia. Si está saturado con equipo, el problema es de delegación. $500 setup + $225/mes por un equipo vs el costo de no escalar. ¿Qué elige?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Tengo otros proyectos primero",
            "Respuesta que Cierra": "Si esos proyectos no generan clientes en automático, consumen recursos en vez de darlos. $45 y el bot vende mientras atiende sus otros proyectos. ¿Qué proyecto le da $300/mes sin su tiempo?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Tengo otros proyectos primero",
            "Respuesta que Cierra": "El Pro está diseñado para integrarse y potenciar sus otros proyectos. Sin centralizar la captación, cada unidad opera como un silo ineficiente. ¿Unificamos la adquisición o sigue manual en cada uno?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Tengo otros proyectos primero",
            "Respuesta que Cierra": "Nuestro onboarding incluye integración con sus operaciones actuales. No se detiene nada, se potencia. ¿Cuál de sus proyectos se vería afectado por facturar más?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No puedo comprometerme ahora",
            "Respuesta que Cierra": "No es un matrimonio, es una inversión de $45, sin mensualidad. Si $45 es mucho compromiso, el desafío es de ventas, no de la herramienta. ¿Cuánto pierde por no comprometerse con vender?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No puedo comprometerme ahora",
            "Respuesta que Cierra": "El Pro se paga solo. Si no se compromete con $225 que retorna $2,000, ¿con qué sí? Hotmart permite 3 pagos de $75. ¿Es compromiso o aversión al riesgo?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No puedo comprometerme ahora",
            "Respuesta que Cierra": "El contrato mínimo es trimestral porque escalar toma 90 días. Si no puede comprometerse 90 días con su crecimiento, el Empresarial no es para usted aún. ¿Seguimos con Pro o pausamos el proceso?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Estoy saturado de trabajo",
            "Respuesta que Cierra": "Justo por eso existe. $45 para dejar de responder \"info\" 3h/día. ¿Prefiere seguir saturado sin costo o invertir $45 para tener 3h libres al día?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Estoy saturado de trabajo",
            "Respuesta que Cierra": "El Pro automatiza el 80% de la operación. Si está saturado ejecutando tareas de $10/hora, ¿cuándo ejecuta las de $100/hora? $225 compra tiempo. ¿Cuánto vale su hora?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Estoy saturado de trabajo",
            "Respuesta que Cierra": "Delegue 100%. Nosotros ejecutamos, usted solo aprueba estrategia. Si está saturado con equipo, el problema es de delegación. $500/mes por un equipo vs el costo de no escalar. ¿Qué elige?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Lo reviso cuando tenga tiempo",
            "Respuesta que Cierra": "Lleva meses \"cuando tenga tiempo\". ¿Cuántos clientes perdió en ese periodo? Son $45. Revíselo en 20 min o sigue perdiendo ingresos. Link directo: [su link]"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Lo reviso cuando tenga tiempo",
            "Respuesta que Cierra": "Le preparo un Loom de 3 min con su caso específico. Lo ve cuando pueda. Si en 3 min no ve valor, lo descarta. ¿Le dedico esos 3 min de análisis o seguimos sin tiempo?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Lo reviso cuando tenga tiempo",
            "Respuesta que Cierra": "Un ejecutivo sin 15 min para escalar no tiene negocio, tiene autoempleo. Mi closer coordina 15 min en su agenda. ¿Hoy 5pm o mañana 9am?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No es el momento adecuado",
            "Respuesta que Cierra": "El momento adecuado fue hace 6 meses. El segundo mejor momento es hoy. $45, 7 días de garantía. ¿Cuándo será \"el momento\" si no es ahora?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No es el momento adecuado",
            "Respuesta que Cierra": "No existe el momento perfecto. Cada mes sin sistema pierde ~$1,000. La garantía de 30 días elimina el riesgo de \"momento\". ¿Qué debe ocurrir para que sea el momento?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No es el momento adecuado",
            "Respuesta que Cierra": "Si factura +$5K/mes, el momento es ahora. Si no, el momento es cuando llegue ahí. ¿En qué rango está para darle la solución correcta?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No confío todavía",
            "Respuesta que Cierra": "Es válido validar. Por eso Hotmart blinda la compra 7 días. Si en 7 días no le gusta, clic y devuelven 100%. ¿Confía en Hotmart? Yo no toco su dinero hasta que esté conforme. ¿Probamos?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No confío todavía",
            "Respuesta que Cierra": "La confianza se construye con garantías. Tiene 30 días: si no generamos 10 citas calificadas, devuelvo la inversión + 1 mes de servicio gratis. ¿Qué empresa ofrece eso sin funcionar?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No confío todavía",
            "Respuesta que Cierra": "Trabajamos con contrato por resultados + NDA. Si en 60 días no hay uplift de 20% en ventas, no factura el tercer mes. ¿Lo revisa su área legal para proceder?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "¿Es real esto?",
            "Respuesta que Cierra": "Más real que su competencia quitándole clientes por WhatsApp. $45, pruébelo 7 días. Si es falso, Hotmart le devuelve. Si es real, me agradece. ¿Lo validamos?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Es real esto?",
            "Respuesta que Cierra": "Tan real que tengo clientes facturando $3K/mes con esto. ¿Quiere ver pantallazos o prefiere ser el próximo caso? $225, 30 días de garantía."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Es real esto?",
            "Respuesta que Cierra": "Se lo demuestro en vivo: sesión de 15 min con acceso de solo lectura a dashboard de cliente real de su industria. Métricas de inversión, leads, ROAS. Si no es real, no firmamos. ¿Qué día revisa?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "¿Funciona realmente?",
            "Respuesta que Cierra": "Funciona si se implementa. $45 y 1h de configuración. Si en 7 días no tiene 1 venta, solicita reembolso. ¿Lo implementa o solo pregunta?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Funciona realmente?",
            "Respuesta que Cierra": "Funciona tanto que si no le trae 3x lo invertido en 60 días, trabajo sin costo hasta lograrlo. ¿Qué otra prueba necesita además de mi trabajo en riesgo?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Funciona realmente?",
            "Respuesta que Cierra": "Funciona bajo contrato: KPI de ROAS 5x. Si no se cumple, no paga mes 3 y le dejo los activos creados. ¿Su agencia actual firma algo similar?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Suena demasiado bueno para ser verdad",
            "Respuesta que Cierra": "Lo \"demasiado bueno\" sería pagar $800/mes a un community manager. Esto es $45 una vez. ¿Qué es más \"demasiado bueno\", ahorrar $755 o seguir sin sistema?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Suena demasiado bueno para ser verdad",
            "Respuesta que Cierra": "Lo bueno es que es verdad. $225 única vez, vende 24/7. Si fuera mentira, Hotmart suspende la cuenta. ¿Confía en la plataforma o no?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Suena demasiado bueno para ser verdad",
            "Respuesta que Cierra": "Es bueno porque es especializado y sin intermediarios. Una agencia de $3K tiene 70% de overhead. Nosotros no. Por eso vale $500. ¿Busca precio o busca resultados?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No conozco la empresa",
            "Respuesta que Cierra": "No necesita conocer la empresa, necesita que funcione. Para eso está la garantía de 7 días de Hotmart. Si hay incumplimiento, la plataforma responde. ¿Probamos o seguimos con la duda?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No conozco la empresa",
            "Respuesta que Cierra": "Busque \"Jorge Bots IA\". Si no hay rastro, no compre. Si encuentra casos reales, avance. $225 con 30 días para evaluar. ¿Qué más necesita validar?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No conozco la empresa",
            "Respuesta que Cierra": "Agendemos 15 min sin costo: conoce al equipo, ve casos y metodología. Si después del Meet no hay fit, no avanzamos. ¿Qué horario le funciona?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No tengo referencias",
            "Respuesta que Cierra": "La mejor referencia es Hotmart. 7 días para devolver sin explicación. Si 1 millón de usuarios confían en la plataforma, ¿le sirve o no?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No tengo referencias",
            "Respuesta que Cierra": "Le conecto con 2 clientes de su nicho para que valide directo. Si no le convencen, no avanza. ¿Le comparto los contactos?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No tengo referencias",
            "Respuesta que Cierra": "Le doy acceso temporal a reporte de campaña real con datos anonimizados. Ve inversión, CPL, citas agendadas. Si eso no es evidencia, ¿qué tipo de referencia requiere?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No sé si es seguro",
            "Respuesta que Cierra": "La transacción es por Hotmart, con certificación PCI-DSS. Yo no almaceno datos de pago. El riesgo es cero. Lo inseguro es seguir perdiendo clientes. ¿Avanza?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No sé si es seguro",
            "Respuesta que Cierra": "Lo inseguro es no automatizar y depender 100% de su tiempo. El Pro tiene 30 días de garantía. ¿Qué arriesga más: $225 con respaldo o seguir igual?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No sé si es seguro",
            "Respuesta que Cierra": "Firmamos NDA + contrato con cláusulas de protección de datos. Incumplimiento = responsabilidad legal. ¿Lo revisa su área legal para proceder?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "He tenido malas experiencias antes",
            "Respuesta que Cierra": "Por eso este vale $45 y no $2000. Si falla otra vez, perdió un almuerzo. Si funciona, ganó un negocio. Hotmart devuelve en 7 días. ¿Cuál es el riesgo real?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "He tenido malas experiencias antes",
            "Respuesta que Cierra": "Por eso la garantía es de 30 días + mes de servicio gratis si fallo. ¿Cuántos \"expertos\" le ofrecieron eso antes? Probemos diferente."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "He tenido malas experiencias antes",
            "Respuesta que Cierra": "Por eso trabajamos por resultados, no por horas. Si no hay uplift en 60 días, no paga mes 3. ¿Su mala experiencia anterior tenía ese contrato?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "¿Y si no funciona para mí?",
            "Respuesta que Cierra": "Si no funciona, solicita reembolso en 7 días. Hotmart devuelve sin disputa. Pero si funciona y no lo compra, pierde $300/mes. ¿Qué pesa más?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Y si no funciona para mí?",
            "Respuesta que Cierra": "Si en 30 días no le genera mínimo $675 en ventas, devuelvo la inversión y sigo trabajando gratis hasta lograrlo. Usted solo pierde 30 días, no dinero. ¿Acepta?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Y si no funciona para mí?",
            "Respuesta que Cierra": "Si en 60 días no hay ROAS de 5x, no factura el tercer mes y le entrego todos los activos creados. Su downside está cubierto. ¿Qué falta para firmar?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Necesito más pruebas",
            "Respuesta que Cierra": "La prueba definitiva es implementarlo en su negocio 7 días sin riesgo. Le hago auditoría gratuita de su WhatsApp antes: le digo cuánto pierde al mes. Si es menos de $45, no compre. ¿Le hago el análisis?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Necesito más pruebas",
            "Respuesta que Cierra": "Le doy acceso de vista a una cuenta activa 7 días. Ve leads entrando, costo, conversaciones. Si en 7 días no ve potencial, cerramos el proceso. ¿Le activo el acceso?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Necesito más pruebas",
            "Respuesta que Cierra": "Le doy acceso view-only a una cuenta activa 7 días. Ve leads entrando, costo, conversaciones. Si en 7 días no ve potencial, cerramos el proceso. ¿Le activo el acceso?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No entiendo bien cómo funciona",
            "Respuesta que Cierra": "En resumen: 1. Cliente escribe. 2. Bot califica y agenda. 3. Usted cierra. La implementación toma 1h con video guía. Si no queda claro, solicita reembolso. ¿Más claro o le hago diagrama?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No entiendo bien cómo funciona",
            "Respuesta que Cierra": "Le preparo Loom de 4 min con su caso específico. Si no queda claro, no avanza. ¿Qué parte genera duda: la captación o el cierre?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No entiendo bien cómo funciona",
            "Respuesta que Cierra": "Es la razón del Meet de diagnóstico de 15 min: mapear su proceso actual y mostrarle el nuevo flujo con números. Si sale sin claridad total, no seguimos. ¿Agendamos?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Necesito más información",
            "Respuesta que Cierra": "¿Qué info específica? ¿Si vende? Sí. ¿Si hay garantía? 7 días. ¿Si es $45? Sí. ¿Qué más? Pregunte puntual o compre ya. El tiempo es costo."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Necesito más información",
            "Respuesta que Cierra": "Le envío one-pager: alcance, casos de uso, garantía y ROI esperado. Si con 1 página no decide, el problema no es información. ¿A qué correo o WhatsApp?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Necesito más información",
            "Respuesta que Cierra": "Toda la información está en la sesión estratégica. 15 min. Enviar PDFs de 20 páginas no escala. ¿Cuándo revisamos su caso específico?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Está muy complicado",
            "Respuesta que Cierra": "La complejidad la absorbemos nosotros. Usted invierte 1h en kickoff, nosotros 48h en implementación. Después opera solo. ¿Sigue siendo complicado o ya es simple?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Está muy complicado",
            "Respuesta que Cierra": "Por eso existe el modelo Empresarial: cero complejidad operativa para usted. Nosotros ejecutamos todo. Su única tarea es revisar el reporte de 5 min semanal. ¿Eso es complicado?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No sé si es para mí",
            "Respuesta que Cierra": "Si vende algo por WhatsApp, es para usted. Si no vende nada, también es para usted. $45. ¿Para quién es si no es para usted?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No sé si es para mí",
            "Respuesta que Cierra": "Si vende servicios/productos de +$200 y atiende por WhatsApp, es para usted. Si no, no lo es. ¿En qué rango de ticket está?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No sé si es para mí",
            "Respuesta que Cierra": "Si factura +$8K/mes y su cuello de botella es adquisición o conversión, es 100% para usted. Si no llega a ese nivel, inicie con Pro. ¿Cuál es su MRR actual?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No entiendo la diferencia entre planes",
            "Respuesta que Cierra": "Base: formación. Pro: implementación hecha por nosotros. Empresarial: operación delegada + ads. ¿Su necesidad es aprender, implementar o delegar?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No entiendo la diferencia entre planes",
            "Respuesta que Cierra": "Base enseña a pescar. Pro entrega la caña. Empresarial sirve el pescado cocinado. ¿Quiere aprender, hacer o recibir resultados?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No entiendo la diferencia entre planes",
            "Respuesta que Cierra": "Pro: le entregamos el sistema. Empresarial: operamos el sistema para usted y garantizamos resultados. ¿Quiere una herramienta o un equipo?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Explícame mejor",
            "Respuesta que Cierra": "Le grabo Loom de 3 min explicando con su caso. Si después de verlo sigue con dudas, no es el momento. ¿Le parece o prefiere seguir con dudas?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Explícame mejor",
            "Respuesta que Cierra": "La explicación es en Meet de 15 min con pantalla compartida. No hay explicación por chat que reemplace ver los números. ¿Qué horario le funciona?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "¿Qué incluye exactamente?",
            "Respuesta que Cierra": "Video curso + plantillas + bot básico en Make. $45. Todo entregado vía Hotmart. ¿Le doy el índice tema por tema o avanza?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Qué incluye exactamente?",
            "Respuesta que Cierra": "Bot en Make + conexión con WhatsApp + integración a Meta Ads + 1 grupo de soporte + 30 días garantía. Entrega en 48h. ¿Necesita el detalle técnico o avanzamos?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Qué incluye exactamente?",
            "Respuesta que Cierra": "Gestión de Ads + Bot avanzado + Closer asignado + Loom semanal + Dashboard en tiempo real + Contrato por resultados. ¿Revisamos el SOW en Meet?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No entiendo el proceso",
            "Respuesta que Cierra": "1. Paga. 2. Recibe acceso por mail. 3. Ve video. 4. Bot vende. ¿En qué paso se pierde? Si es el 1, le paso link."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No entiendo el proceso",
            "Respuesta que Cierra": "1. Paga. 2. Kickoff 30 min. 3. Entregamos en 48h. 4. Usted vende. ¿Qué paso le genera fricción?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No entiendo el proceso",
            "Respuesta que Cierra": "1. Firma trimestral. 2. Onboarding 7 días. 3. Operamos 90 días. 4. Reportamos ROAS. ¿Le diseño el Gantt o empezamos?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "¿Cómo empiezo?",
            "Respuesta que Cierra": "Realiza el pago de $45 aquí: [link]. Acceso inmediato por mail en 2 min. ¿Necesita que le dé clic yo también?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Cómo empiezo?",
            "Respuesta que Cierra": "Paga $225 y mi asistente le agenda kickoff en las próximas 24h hábiles. ¿Le comparto el link de pago?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Cómo empiezo?",
            "Respuesta que Cierra": "Firmamos contrato y paga mes 1. Hoy mismo queda agendado el onboarding estratégico. ¿Le envío el contrato para firma?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Me confunde un poco",
            "Respuesta que Cierra": "La confusión cuesta dinero. Le simplifico: invierte $45, si no retorna, devuelve. ¿Menos confuso ahora o necesita otra variable?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Me confunde un poco",
            "Respuesta que Cierra": "Para eso me contrata: para que usted no se confunda. Nosotros ejecutamos, usted aprueba estrategia. ¿Delegamos la complejidad o la sigue cargando?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Estoy comparando con otras opciones",
            "Respuesta que Cierra": "Compare esto: $45 pago único vs $15/mes recurrente. En 3 meses ya pagó más con el otro. ¿Sigo o ya ganó?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Estoy comparando con otras opciones",
            "Respuesta que Cierra": "Compare garantías: Yo 30 días + trabajo gratis si fallo. ¿Su otra opción le da eso por escrito? Si sí, tómela. Si no, esta es la opción."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Estoy comparando con otras opciones",
            "Respuesta que Cierra": "Compare contratos: nosotros por resultados, otros por horas. ¿Prefiere pagar por intentar o pagar por ganar? Le doy 48h para decidir, luego el cupo se libera."
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Voy a revisar otras alternativas",
            "Respuesta que Cierra": "Perfecto. Mientras revisa, le hago auditoría gratuita de su embudo. Si no encuentro cómo generarle +$1K/mes, no me contacte más. ¿Le sirve el análisis sin compromiso?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Voy a revisar otras alternativas",
            "Respuesta que Cierra": "Le mantengo la propuesta 7 días. Si no cierra, el precio se ajusta 15% el próximo Q. ¿Cuándo tiene la decisión para reservar el cupo?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No estoy decidido aún",
            "Respuesta que Cierra": "La indecisión es una decisión: la de no crecer. Tiene 7 días para decidir con el producto en mano. Si no le gusta, reembolsa. ¿Más fácil que eso?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No estoy decidido aún",
            "Respuesta que Cierra": "Los mercados no esperan indecisos. O lidera o sigue. Le doy 15 min de mi tiempo para decidir con datos. Si no agenda, asumo que no es el perfil. ¿Agendamos?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Quiero pensarlo",
            "Respuesta que Cierra": "Piénselo con el bot comprado. Tiene 7 días. Si pensando no le genera, devuelve. Si genera, ya ganó. ¿Qué análisis supera a la prueba real?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Quiero pensarlo",
            "Respuesta que Cierra": "Pensar sin datos es adivinar. En el Meet de 15 min le doy los datos de su industria. Después de eso, pensar es redundante. ¿Cuándo piensa con datos?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Necesito consultarlo",
            "Respuesta que Cierra": "Envíele este resumen a su socio: \"$45, 7 días garantía, si falla trabajo gratis. ROI esperado 3x en 60 días\". Si dice no, el socio es el problema. ¿Se lo envío yo?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Necesito consultarlo",
            "Respuesta que Cierra": "Sumemos a su socio al Meet. Yo presento el caso de negocio. Si no logro convencerlo con números, no cobro el setup. ¿Cuándo los tengo a ambos 15 min?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Tengo que hablarlo con alguien",
            "Respuesta que Cierra": "Perfecto. Le grabo un Loom de 2 min para que lo comparta. Si su socio/empresa no ve valor en 2 min, no es el momento. ¿A quién se lo envío?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Tengo que hablarlo con alguien",
            "Respuesta que Cierra": "Agendemos reunión a 3 partes. Yo expongo, ustedes deciden. Si no cerramos, la consultoría fue gratis. ¿Qué día les funciona?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Estoy evaluando varias opciones",
            "Respuesta que Cierra": "La evaluación #1 es: ¿Cuál le da garantía de resultados por escrito? Si ninguna, esta gana. Si alguna sí, compárela y me cuenta. ¿Cuál otra le da 30 días + trabajo gratis si falla?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Estoy evaluando varias opciones",
            "Respuesta que Cierra": "Le doy acceso de vista 7 días a campañas reales. Evalúe con datos, no con PDFs. Si en 7 días no supera a sus opciones, descarte. ¿Le activo el acceso?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No estoy convencido todavía",
            "Respuesta que Cierra": "No vendo convicción, vendo resultados con garantía. Pruebe 7 días. Si no hay 1 venta, devuelve. Si hay 1, me agradece. ¿Eso lo convence o qué falta?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No estoy convencido todavía",
            "Respuesta que Cierra": "No necesita estar convencido, necesita ver ROAS. Contrato por resultados: si no hay 5x, no paga mes 3. ¿Le convencen las matemáticas o las promesas?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "Quizás más adelante",
            "Respuesta que Cierra": "Quizás le cuesta ~$1,500/mes en oportunidad. La implementación hoy se paga sola en 15 días. ¿Qué cambia su \"quizás\" en 30 días que no tenga hoy?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Quizás más adelante",
            "Respuesta que Cierra": "Los \"más adelante\" pagan la pauta de los que entraron hoy. ¿Lidera su categoría en 2026 o la deja ir? El cupo de onboarding de este mes cierra el viernes. ¿Entra o espera?"
        },
        {
            "Plan": "Plan Base",
            "Objeción": "No estoy listo para decidir",
            "Respuesta que Cierra": "La preparación es un mito. Se decide y se ajusta en el camino. Tiene 7 días para decidir con el sistema operando. ¿Más listo que eso cómo?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No estoy listo para decidir",
            "Respuesta que Cierra": "Si factura +$8K/mes y no está listo para escalar, hay un freno estratégico. ¿Lo identificamos en 15 min o sigue sin estar listo?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Qué pasa si la IA se equivoca?",
            "Respuesta que Cierra": "La IA se ajusta con parámetros; monitoreamos para que aprenda de cada interacción."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Prefiero hacerlo yo mismo",
            "Respuesta que Cierra": "VAI libera tu tiempo para gestionar el negocio, no para operar mensajes."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Quién garantiza que esto funcione?",
            "Respuesta que Cierra": "Resultados medibles respaldan la metodología; vamos por objetivos claros desde el inicio."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Es seguro para mis datos?",
            "Respuesta que Cierra": "Trabajamos con APIs oficiales que garantizan seguridad y privacidad total."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "He probado otras herramientas y fallaron",
            "Respuesta que Cierra": "Las herramientas son solo una parte; VAI integra la estrategia completa de negocio."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No tengo tiempo para aprender a usarlo",
            "Respuesta que Cierra": "No requieres ser experto; nosotros nos encargamos del setup técnico completo."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Mi negocio es muy específico",
            "Respuesta que Cierra": "Entrenamos la IA con el contexto y lenguaje específico de tu marca."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Necesito cambiar de proveedor de telefonía?",
            "Respuesta que Cierra": "No, integramos la API con tu infraestructura actual sin cambios necesarios."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Y si se cae el sistema?",
            "Respuesta que Cierra": "Tenemos protocolos de redundancia para asegurar continuidad las 24 horas."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Funciona con otros canales además de WhatsApp?",
            "Respuesta que Cierra": "Sí, la metodología VAI es escalable y adaptable a otros canales."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Es una inversión mensual alta",
            "Respuesta que Cierra": "Un empleado humano costaría 5 veces más con menor disponibilidad."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Quiero ver resultados antes de pagar",
            "Respuesta que Cierra": "El setup es un trabajo especializado; el valor está en la automatización inmediata."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Tienen planes de prueba?",
            "Respuesta que Cierra": "El Plan Base es ideal para validar la potencia sin grandes compromisos."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No veo cómo esto aumenta mis ventas",
            "Respuesta que Cierra": "La rapidez aumenta la conversión; cada minuto sin responder es dinero perdido."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Me garantizas un número exacto de ventas?",
            "Respuesta que Cierra": "Optimizamos el flujo y el lead; el cierre es un trabajo conjunto entre IA y equipo."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Déjame consultarlo con mi socio",
            "Respuesta que Cierra": "¿Qué puntos específicos necesita validar para que podamos avanzar juntos?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Te aviso el próximo mes",
            "Respuesta que Cierra": "En un mes, ¿cuántos clientes potenciales se habrán ido a la competencia?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Estoy muy ocupado ahora",
            "Respuesta que Cierra": "Justo por eso necesitas automatizar, para dejar de apagar fuegos."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No estoy listo para escalar",
            "Respuesta que Cierra": "La automatización prepara tu sistema para crecer de forma sostenible."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Lo analizaré con calma",
            "Respuesta que Cierra": "¿Qué información adicional te falta para tomar una decisión hoy mismo?"
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "El servicio técnico es lento",
            "Respuesta que Cierra": "Nuestro soporte prioritario asegura soluciones rápidas en el Plan Empresarial."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Mi equipo no quiere usar IA",
            "Respuesta que Cierra": "La IA simplifica su carga de trabajo, permitiéndoles enfocarse en cerrar."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Prefiero el trato humano",
            "Respuesta que Cierra": "La IA gestiona lo rutinario para que el humano cierre con valor."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "La IA suena robótica",
            "Respuesta que Cierra": "Configuramos el tono de voz para que suene humano y cercano."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Puedo cancelar en cualquier momento?",
            "Respuesta que Cierra": "Sí, la flexibilidad es parte de nuestro compromiso de resultados."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Ofrecen capacitación al personal?",
            "Respuesta que Cierra": "Incluimos capacitación básica en los planes Pro y Empresarial."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Cómo mido el éxito de esto?",
            "Respuesta que Cierra": "Medimos el ROI, el flujo de atención y el incremento en ventas."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Es fácil de integrar?",
            "Respuesta que Cierra": "Es un proceso guiado por nosotros desde la integración inicial."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Tengo miedo de perder el control",
            "Respuesta que Cierra": "Tú siempre supervisas; la IA solo sigue tus reglas de negocio."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Qué incluye el soporte?",
            "Respuesta que Cierra": "Soporte continuo y actualizaciones de tu Asistente IA incluido."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No entiendo la metodología VAI",
            "Respuesta que Cierra": "VAI significa Visibilidad, Automatización e Inteligencia; es un sistema, no solo un bot."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "El contrato es muy largo",
            "Respuesta que Cierra": "Es un contrato por resultados para tu tranquilidad."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Prefiero anuncios pagados tradicionales",
            "Respuesta que Cierra": "La publicidad necesita la IA para convertir; sin ella, es tráfico desperdiciado."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Mi competencia no usa IA",
            "Respuesta que Cierra": "Ser los primeros en tu sector con IA te da una ventaja competitiva enorme."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Esto es una moda pasajera",
            "Respuesta que Cierra": "La automatización con IA es el estándar actual para negocios escalables."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Puedo cambiar de plan después?",
            "Respuesta que Cierra": "Sí, puedes escalar o ajustar tu plan según el crecimiento."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "La configuración parece compleja",
            "Respuesta que Cierra": "Nosotros realizamos la configuración; tú solo recibes el sistema andando."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Qué pasa con los clientes antiguos?",
            "Respuesta que Cierra": "La IA también puede gestionar la fidelización y re-compra de clientes."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Cómo manejo las quejas?",
            "Respuesta que Cierra": "La IA categoriza y escala quejas a humanos según gravedad."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿La IA puede cerrar ventas?",
            "Respuesta que Cierra": "La IA califica y guía al cliente; tú finalizas la venta."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "El precio no incluye impuestos",
            "Respuesta que Cierra": "Los precios son netos; te entregamos factura para tu contabilidad."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Tienen casos de éxito?",
            "Respuesta que Cierra": "Sí, casos como Muebles Venecia donde pasamos de 20 a 120 ventas."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿La IA aprende sola?",
            "Respuesta que Cierra": "Aprendizaje continuo bajo supervisión humana constante."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Necesito una prueba gratuita",
            "Respuesta que Cierra": "El valor del sistema está en el setup profesional que garantiza resultados."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "Me parece muy técnico",
            "Respuesta que Cierra": "No es técnico, es estrategia de negocio puesta en piloto automático."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "¿Puedo personalizar los mensajes?",
            "Respuesta que Cierra": "Totalmente, redactamos los prompts bajo tu guía de marca."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "El setup inicial es muy alto",
            "Respuesta que Cierra": "El setup es un pago único por el diseño de un activo que genera dinero."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "No tengo base de datos",
            "Respuesta que Cierra": "La IA te ayuda a construir tu base de datos desde cero."
        },
        {
            "Plan": "Plan Empresarial",
            "Objeción": "La IA no entiende mi jerga",
            "Respuesta que Cierra": "La entrenamos con tu terminología específica en la fase de setup."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Mi negocio es local y tradicional",
            "Respuesta que Cierra": "Precisamente, la IA ayuda a digitalizar negocios tradicionales sin perder su esencia."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Qué pasa si la IA se equivoca?",
            "Respuesta que Cierra": "La IA se ajusta con parámetros; monitoreamos para que aprenda de cada interacción."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Prefiero hacerlo yo mismo",
            "Respuesta que Cierra": "VAI libera tu tiempo para gestionar el negocio, no para operar mensajes."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Quién garantiza que esto funcione?",
            "Respuesta que Cierra": "Resultados medibles respaldan la metodología; vamos por objetivos claros desde el inicio."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Es seguro para mis datos?",
            "Respuesta que Cierra": "Trabajamos con APIs oficiales que garantizan seguridad y privacidad total."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "He probado otras herramientas y fallaron",
            "Respuesta que Cierra": "Las herramientas son solo una parte; VAI integra la estrategia completa de negocio."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No tengo tiempo para aprender a usarlo",
            "Respuesta que Cierra": "No requieres ser experto; nosotros nos encargamos del setup técnico completo."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Mi negocio es muy específico",
            "Respuesta que Cierra": "Entrenamos la IA con el contexto y lenguaje específico de tu marca."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Necesito cambiar de proveedor de telefonía?",
            "Respuesta que Cierra": "No, integramos la API con tu infraestructura actual sin cambios necesarios."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Y si se cae el sistema?",
            "Respuesta que Cierra": "Tenemos protocolos de redundancia para asegurar continuidad las 24 horas."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Funciona con otros canales además de WhatsApp?",
            "Respuesta que Cierra": "Sí, la metodología VAI es escalable y adaptable a otros canales."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Es una inversión mensual alta",
            "Respuesta que Cierra": "Un empleado humano costaría 5 veces más con menor disponibilidad."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Quiero ver resultados antes de pagar",
            "Respuesta que Cierra": "El setup es un trabajo especializado; el valor está en la automatización inmediata."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Tienen planes de prueba?",
            "Respuesta que Cierra": "El Plan Base es ideal para validar la potencia sin grandes compromisos."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No veo cómo esto aumenta mis ventas",
            "Respuesta que Cierra": "La rapidez aumenta la conversión; cada minuto sin responder es dinero perdido."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Me garantizas un número exacto de ventas?",
            "Respuesta que Cierra": "Optimizamos el flujo y el lead; el cierre es un trabajo conjunto entre IA y equipo."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Déjame consultarlo con mi socio",
            "Respuesta que Cierra": "¿Qué puntos específicos necesita validar para que podamos avanzar juntos?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Te aviso el próximo mes",
            "Respuesta que Cierra": "En un mes, ¿cuántos clientes potenciales se habrán ido a la competencia?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Estoy muy ocupado ahora",
            "Respuesta que Cierra": "Justo por eso necesitas automatizar, para dejar de apagar fuegos."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No estoy listo para escalar",
            "Respuesta que Cierra": "La automatización prepara tu sistema para crecer de forma sostenible."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Lo analizaré con calma",
            "Respuesta que Cierra": "¿Qué información adicional te falta para tomar una decisión hoy mismo?"
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "El servicio técnico es lento",
            "Respuesta que Cierra": "Nuestro soporte prioritario asegura soluciones rápidas en el Plan Empresarial."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Mi equipo no quiere usar IA",
            "Respuesta que Cierra": "La IA simplifica su carga de trabajo, permitiéndoles enfocarse en cerrar."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Prefiero el trato humano",
            "Respuesta que Cierra": "La IA gestiona lo rutinario para que el humano cierre con valor."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "La IA suena robótica",
            "Respuesta que Cierra": "Configuramos el tono de voz para que suene humano y cercano."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Puedo cancelar en cualquier momento?",
            "Respuesta que Cierra": "Sí, la flexibilidad es parte de nuestro compromiso de resultados."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Ofrecen capacitación al personal?",
            "Respuesta que Cierra": "Incluimos capacitación básica en los planes Pro y Empresarial."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Cómo mido el éxito de esto?",
            "Respuesta que Cierra": "Medimos el ROI, el flujo de atención y el incremento en ventas."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Es fácil de integrar?",
            "Respuesta que Cierra": "Es un proceso guiado por nosotros desde la integración inicial."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Tengo miedo de perder el control",
            "Respuesta que Cierra": "Tú siempre supervisas; la IA solo sigue tus reglas de negocio."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Qué incluye el soporte?",
            "Respuesta que Cierra": "Soporte continuo y actualizaciones de tu Asistente IA incluido."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No entiendo la metodología VAI",
            "Respuesta que Cierra": "VAI significa Visibilidad, Automatización e Inteligencia; es un sistema, no solo un bot."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "El contrato es muy largo",
            "Respuesta que Cierra": "Es un contrato por resultados para tu tranquilidad."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Prefiero anuncios pagados tradicionales",
            "Respuesta que Cierra": "La publicidad necesita la IA para convertir; sin ella, es tráfico desperdiciado."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Mi competencia no usa IA",
            "Respuesta que Cierra": "Ser los primeros en tu sector con IA te da una ventaja competitiva enorme."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Esto es una moda pasajera",
            "Respuesta que Cierra": "La automatización con IA es el estándar actual para negocios escalables."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Puedo cambiar de plan después?",
            "Respuesta que Cierra": "Sí, puedes escalar o ajustar tu plan según el crecimiento."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "La configuración parece compleja",
            "Respuesta que Cierra": "Nosotros realizamos la configuración; tú solo recibes el sistema andando."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Qué pasa con los clientes antiguos?",
            "Respuesta que Cierra": "La IA también puede gestionar la fidelización y re-compra de clientes."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Cómo manejo las quejas?",
            "Respuesta que Cierra": "La IA categoriza y escala quejas a humanos según gravedad."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿La IA puede cerrar ventas?",
            "Respuesta que Cierra": "La IA califica y guía al cliente; tú finalizas la venta."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "El precio no incluye impuestos",
            "Respuesta que Cierra": "Los precios son netos; te entregamos factura para tu contabilidad."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Tienen casos de éxito?",
            "Respuesta que Cierra": "Sí, casos como Muebles Venecia donde pasamos de 20 a 120 ventas."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿La IA aprende sola?",
            "Respuesta que Cierra": "Aprendizaje continuo bajo supervisión humana constante."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Necesito una prueba gratuita",
            "Respuesta que Cierra": "El valor del sistema está en el setup profesional que garantiza resultados."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Me parece muy técnico",
            "Respuesta que Cierra": "No es técnico, es estrategia de negocio puesta en piloto automático."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "¿Puedo personalizar los mensajes?",
            "Respuesta que Cierra": "Totalmente, redactamos los prompts bajo tu guía de marca."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "El setup inicial es muy alto",
            "Respuesta que Cierra": "El setup es un pago único por el diseño de un activo que genera dinero."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "No tengo base de datos",
            "Respuesta que Cierra": "La IA te ayuda a construir tu base de datos desde cero."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "La IA no entiende mi jerga",
            "Respuesta que Cierra": "La entrenamos con tu terminología específica en la fase de setup."
        },
        {
            "Plan": "Plan Pro",
            "Objeción": "Mi negocio es local y tradicional",
            "Respuesta que Cierra": "Precisamente, la IA ayuda a digitalizar negocios tradicionales sin perder su esencia."
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
        },
        {
            "Plan": "Plan Base",
            "Pregunta": "¿Para qué sirve este programa?",
            "Respuesta": "Sirve para entender qué es la IA, cómo funciona en marketing y decidir si quiere escalar. Inversión $45 pago único."
        },
        {
            "Plan": "Plan Pro",
            "Pregunta": "¿Para qué sirve este programa?",
            "Respuesta": "Sirve para implementar un asistente de ventas IA que atiende 24/7 y califica clientes. Inversión primer mes $250 setup. Mes 2 solo $100/mes si decide continuar con soporte."
        },
        {
            "Plan": "Plan Empresarial",
            "Pregunta": "¿Para qué sirve este programa?",
            "Respuesta": "Sirve para delegar 100% la operación de ads + bot + seguimiento. Nuestro equipo ejecuta. Inversión primer mes $500 setup. Desde mes 2 $225/mes. ROI objetivo 5x-10x en 90 días."
        },
        {
            "Plan": "Plan Base",
            "Pregunta": "¿Es para principiantes?",
            "Respuesta": "Sí. Diseñado para quien no tiene experiencia en IA ni marketing. Empieza desde cero."
        },
        {
            "Plan": "Plan Pro",
            "Pregunta": "¿Es para principiantes?",
            "Respuesta": "Sí. Todo se explica con video guía. Si sabe usar WhatsApp, puede implementarlo. El setup de $250 incluye 1h de acompañamiento inicial."
        },
        {
            "Plan": "Plan Empresarial",
            "Pregunta": "¿Es para principiantes?",
            "Respuesta": "Sí. No requiere experiencia porque nuestro equipo hace la implementación. Usted solo revisa el reporte semanal de 5 min."
        },
        {
            "Plan": "Plan Base",
            "Pregunta": "¿Necesito experiencia en marketing?",
            "Respuesta": "No. Aprende los conceptos básicos dentro del curso."
        },
        {
            "Plan": "Plan Pro",
            "Pregunta": "¿Necesito experiencia en marketing?",
            "Respuesta": "No. El sistema incluye guías de copy y estrategia. Si tiene dudas, el soporte de $100/mes lo asiste."
        },
        {
            "Plan": "Plan Empresarial",
            "Pregunta": "¿Necesito experiencia en marketing?",
            "Respuesta": "No. Nuestro equipo de marketing diseña y ejecuta las campañas por usted."
        },
        {
            "Plan": "Plan Base",
            "Pregunta": "¿Incluye prompts de IA?",
            "Respuesta": "Incluye biblioteca básica de prompts para aprender a generar contenido."
        },
        {
            "Plan": "Plan Pro",
            "Pregunta": "¿Incluye prompts de IA?",
            "Respuesta": "Incluye biblioteca avanzada de prompts de venta, objeciones y seguimiento. Listos para copiar-pegar en su bot."
        },
        {
            "Plan": "Plan Empresarial",
            "Pregunta": "¿Incluye prompts de IA?",
            "Respuesta": "Incluye biblioteca avanzada + nuestro equipo crea y optimiza prompts personalizados para su negocio cada mes."
        },
        {
            "Plan": "Plan Base",
            "Pregunta": "¿Incluye publicidad en Meta Ads?",
            "Respuesta": "Incluye módulo teórico: cómo funciona Meta Ads y estructura de campañas. No incluye ejecución."
        },
        {
            "Plan": "Plan Pro",
            "Pregunta": "¿Incluye publicidad en Meta Ads?",
            "Respuesta": "Incluye plantillas de campañas y guía de implementación. Usted ejecuta sus ads. Soporte técnico incluido en $100/mes."
        },
        {
            "Plan": "Plan Empresarial",
            "Pregunta": "¿Incluye publicidad en Meta Ads?",
            "Respuesta": "Sí. Creación, gestión y optimización de campañas incluida. Nuestro equipo invierte su presupuesto de ads y reporta ROAS semanal. Incluido en $225/mes."
        },
        {
            "Plan": "Plan Base",
            "Pregunta": "¿Se enseña automatización?",
            "Respuesta": "Sí. Aprende concepto y ve ejemplos en Make. No incluye bot funcional."
        },
        {
            "Plan": "Plan Pro",
            "Pregunta": "¿Se enseña automatización?",
            "Respuesta": "Sí. Se entrega 1 Agente de Ventas IA funcional en Make + video de edición. Soporte y actualización incluidos en $100/mes."
        },
        {
            "Plan": "Plan Empresarial",
            "Pregunta": "¿Se enseña automatización?",
            "Respuesta": "No se enseña. Se implementa. Nuestro equipo configura bot avanzado con conexión a stock, CRM y agenda. Mantenimiento incluido en $225/mes."
        },
        {
            "Plan": "Plan Base",
            "Pregunta": "¿En cuánto tiempo se ven resultados?",
            "Respuesta": "Depende de su implementación. Si aplica el método, puede ver primeras interacciones en 7 días. Es formación."
        },
        {
            "Plan": "Plan Pro",
            "Pregunta": "¿En cuánto tiempo se ven resultados?",
            "Respuesta": "Si implementa en 48h como indica la guía, verá primeros leads calificados en 7 días. Garantía 30 días: si no genera 5 clientes, devolvemos $250 setup."
        },
        {
            "Plan": "Plan Empresarial",
            "Pregunta": "¿En cuánto tiempo se ven resultados?",
            "Respuesta": "Desde semana 1 verá leads. Objetivo contractual: +20% facturación en 60 días o mes 3 de soporte $225 no se factura."
        },
        {
            "Plan": "Plan Base",
            "Pregunta": "¿El precio incluye soporte?",
            "Respuesta": "Incluye acceso a grupo de comunidad para dudas generales. Soporte 1-a-1 no incluido."
        },
        {
            "Plan": "Plan Pro",
            "Pregunta": "¿El precio incluye soporte?",
            "Respuesta": "El setup $250 incluye 1h de onboarding. La mensualidad $100/mes incluye soporte vía WhatsApp para dudas técnicas y ajustes del bot."
        },
        {
            "Plan": "Plan Empresarial",
            "Pregunta": "¿El precio incluye soporte?",
            "Respuesta": "Sí. $225/mes incluye equipo completo: ads manager, setter, bot manager. Soporte diario y reportes semanales."
        },
        {
            "Plan": "Plan Base",
            "Pregunta": "¿Incluye agentes de IA?",
            "Respuesta": "No incluye agente funcional. Incluye lección de cómo funciona un agente para que entienda el concepto."
        },
        {
            "Plan": "Plan Pro",
            "Pregunta": "¿Incluye agentes de IA?",
            "Respuesta": "Sí. Incluye 1 Agente IA de Ventas funcional para WhatsApp. Usted lo edita. Soporte de ajustes incluido en $100/mes."
        },
        {
            "Plan": "Plan Empresarial",
            "Pregunta": "¿Incluye agentes de IA?",
            "Respuesta": "Sí. Incluye Agente IA Avanzado: vende, asesora, consulta stock en tiempo real y agenda. Creado y optimizado por nuestro equipo. Incluido en $225/mes."
        },
        {
            "Plan": "Plan Pro",
            "Pregunta": "¿En cuánto tiempo recupero los $250?",
            "Respuesta": "Si su ticket es $50, con 5 ventas recupera el setup. Un bot bien configurado cierra 1 venta cada 3 días solo por responder rápido 24/7. Si en 30 días no genera 5 clientes, devolvemos los $250."
        },
        {
            "Plan": "Plan Pro",
            "Pregunta": "¿Por qué pagar $100 mensual después?",
            "Respuesta": "Porque $100/mes cubre: servidor del bot, actualizaciones cuando Meta cambia, ajustes de prompts y soporte técnico. Contratar eso por separado vale $400+/mes. Si no quiere soporte, usa solo el curso base."
        },
        {
            "Plan": "Plan Pro",
            "Pregunta": "¿Y si WhatsApp me bloquea el número?",
            "Respuesta": "Usamos WhatsApp Business API oficial de Meta, la misma de bancos y retail. Cero riesgo de bloqueo. Los baneos ocurren con bots no oficiales que hacen spam. Aquí aprende el método correcto y a largo plazo."
        },
        {
            "Plan": "Plan Pro",
            "Pregunta": "¿Si es tan bueno por qué no vale $1000?",
            "Respuesta": "Porque el objetivo es volumen y casos de éxito. Prefiero 1000 clientes en $250 contando resultados, que 10 en $1000. Más testimonios = más mercado para todos."
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
        },
        {
            "Nicho": "",
            "Dolor Principal": "",
            "Mensaje del Bot": "",
            "Cierre Específico": ""
        },
        {
            "Nicho": "",
            "Dolor Principal": "",
            "Mensaje del Bot": "",
            "Cierre Específico": ""
        },
        {
            "Nicho": "",
            "Dolor Principal": "",
            "Mensaje del Bot": "",
            "Cierre Específico": ""
        },
        {
            "Nicho": "",
            "Dolor Principal": "",
            "Mensaje del Bot": "",
            "Cierre Específico": ""
        },
        {
            "Nicho": "",
            "Dolor Principal": "",
            "Mensaje del Bot": "",
            "Cierre Específico": ""
        },
        {
            "Nicho": "",
            "Dolor Principal": "",
            "Mensaje del Bot": "",
            "Cierre Específico": ""
        },
        {
            "Nicho": "",
            "Dolor Principal": "",
            "Mensaje del Bot": "",
            "Cierre Específico": ""
        },
        {
            "Nicho": "",
            "Dolor Principal": "",
            "Mensaje del Bot": "",
            "Cierre Específico": ""
        },
        {
            "Nicho": "",
            "Dolor Principal": "",
            "Mensaje del Bot": "",
            "Cierre Específico": ""
        },
        {
            "Nicho": "",
            "Dolor Principal": "",
            "Mensaje del Bot": "",
            "Cierre Específico": ""
        },
        {
            "Nicho": "",
            "Dolor Principal": "",
            "Mensaje del Bot": "        . ",
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
    "Cierre de Ventas": [
        {
            "Situación": "1. Caliente, ya preguntó precio",
            "Cierre para el bot": "Listo 🔥 Te dejo el acceso al Plan Pro aquí: [LINK_PRO]. ¿Lo haces con tarjeta o PSE? Así te activo de una.",
            "Cuándo usarlo": "Cuando ya vio beneficios y solo falta pagar"
        },
        {
            "Situación": "2. Duda entre Base y Pro",
            "Cierre para el bot": "Mira, el Base es pa’ aprender. El Pro es pa’ ganar. Si tu negocio ya factura, el Pro se paga solo en la primera venta que cierre el bot. Te paso el link del Pro: [LINK_PRO] ¿Lo tomas?",
            "Cuándo usarlo": "Cuando compara planes"
        },
        {
            "Situación": "3. Dice \"lo pienso\"",
            "Cierre para el bot": "Total, piénsalo bien. Solo recuerda: cada día sin bot son clientes que se van con la competencia que sí responde 24/7. Te guardo tu cupo 12h en este link: [LINK_PRO]. Si vuelves después, me avisas.",
            "Cuándo usarlo": "Objeción de tiempo"
        },
        {
            "Situación": "4. Dice \"está caro\"",
            "Cierre para el bot": "Te entiendo. \\$250 suena duro hoy. Pero ¿cuánto pierdes al mes por no responder en la noche? Si son 3 ventas de \\$100, ya perdiste \\$300. El bot vale \\$250 una vez y te trabaja 24/7. ¿Lo vemos así? Link aquí: [LINK_PRO]",
            "Cuándo usarlo": "Objeción de precio"
        },
        {
            "Situación": "5. Ya confía, solo falta empujar",
            "Cierre para el bot": "Brutal, ya tienes claro que esto es pa’ ti. Último paso: entra aquí [LINK_PRO], paga y en 5 min te llega todo + te meto al grupo de WhatsApp. ¿Le damos?",
            "Cuándo usarlo": "Cuando ya dijo \"sí\" pero no paga"
        },
        {
            "Situación": "6. Empresario ocupado",
            "Cierre para el bot": "Sé que andas full. Por eso el Empresarial es pa’ ti: nosotros hacemos todo. Tú solo apruebas. Link directo: [LINK_EMPRESARIAL] ¿Activo el equipo hoy mismo?",
            "Cuándo usarlo": "Pa’ Plan de \\$500"
        },
        {
            "Situación": "7. Quiere mensualidad más baja",
            "Cierre para el bot": "El Pro son \\$100/mes porque incluye soporte + mejoras del bot. Es como tener un empleado por \\$3 al día que nunca duerme. Si arrancas hoy te respeto el precio. Link: [LINK_PRO] ¿Arrancamos?",
            "Cuándo usarlo": "Objeción mensualidad"
        },
        {
            "Situación": "8. Pidió garantía",
            "Cierre para el bot": "Tienes 7 días de garantía Hotmart. Si en 7 días no tienes el bot respondiendo, pides reembolso y listo. Cero riesgo. Link: [LINK_PRO] ¿Lo pruebas sin miedo?",
            "Cuándo usarlo": "Miedo a perder plata"
        },
        {
            "Situación": "9. Dijo \"no tengo plata ahora\"",
            "Cierre para el bot": "Te entiendo total. Mira, el Base son \\$45 sin mensualidad pa’ que arranques ya. Cuando vendas gracias a eso, subes al Pro. Te dejo el Base aquí: [LINK_BASE] ¿Empezamos por ahí?",
            "Cuándo usarlo": "Downsell inteligente"
        },
        {
            "Situación": "10. Cierre agresivo, ya calificó",
            "Cierre para el bot": "Parce, ya hablamos todo. Tu negocio necesita esto y tú lo sabes. Son 3 clics: entra [LINK_PRO], paga, y mañana amaneces con ventas automáticas. ¿Cuál excusa te vas a poner hoy?",
            "Cuándo usarlo": "Cuando ya calentó mucho"
        },
        {
            "Situación": "11. Escéptico con IA",
            "Cierre para el bot": "Mira, no te vendo “IA mágica”. Te vendo 3 horas diarias de tu vida de vuelta. Eso vale \\$250 una sola vez. Si en 7 días no ves la diferencia, pides reembolso. Link: [LINK_PRO] ¿Lo probamos sin riesgo?",
            "Cuándo usarlo": "Cuando duda de la tecnología"
        },
        {
            "Situación": "12. Compara con freelancer",
            "Cierre para el bot": "Un freelancer te cobra \\$300 y si se enferma, te quedas sin responder. El bot son \\$250 y trabaja 24/7 sin pedir vacaciones. Te paso el link: [LINK_PRO] ¿Prefieres depender de humanos o de sistemas?",
            "Cuándo usarlo": "Cuando dice “mejor contrato a alguien”"
        },
        {
            "Situación": "13. Dice “vuelvo luego”",
            "Cierre para el bot": "Parce, “vuelvo luego” es el primo de “nunca”. Si de verdad te sirve, lo arreglamos ya en 2 min: [LINK_PRO]. Si no, tranquilo. Pero no te mientas. ¿Le damos o qué?",
            "Cuándo usarlo": "Pa’ los que se escapan"
        },
        {
            "Situación": "14. Tiene miedo al cambio",
            "Cierre para el bot": "Entiendo el susto. Yo también lo tuve. Pero ¿sabes qué da más miedo? Seguir igual en 6 meses mientras tu competencia te pasa por encima con bots. Link [LINK_PRO]. Yo te llevo de la mano. ¿Arrancamos?",
            "Cuándo usarlo": "Miedo/ansiedad"
        },
        {
            "Situación": "15. Pregunta por resultados garantizados",
            "Cierre para el bot": "No te garantizo millones porque sería mentiroso. Te garantizo esto: si sigues el paso a paso, en 72h tienes un bot respondiendo. Si no, te devuelvo el dinero. Link: [LINK_PRO] ¿Trato justo?",
            "Cuándo usarlo": "Busca garantías"
        },
        {
            "Situación": "16. Es dueño y no delega",
            "Cierre para el bot": "Sé que te gusta hacer todo tú. Por eso esto te sirve: montas el bot 1 vez y te olvidas de responder “info” a las 11pm. Sigues teniendo control, pero sin quemarte. Link: [LINK_PRO] ¿Te liberas o sigues esclavo?",
            "Cuándo usarlo": "Control freaks"
        },
        {
            "Situación": "17. Ya tiene ManyChat/Bot básico",
            "Cierre para el bot": "ManyChat es pa’ mandar PDF. Esto es pa’ cerrar ventas. Es la diferencia entre un mesero que toma pedido y un vendedor que cobra. Sube de nivel: [LINK_PRO] ¿Cambias bicicleta por Ferrari?",
            "Cuándo usarlo": "Upgrade de bot malo"
        },
        {
            "Situación": "18. Dice “tengo que hablarlo con mi socio”",
            "Cierre para el bot": "Total. Habla con tu socio y pregúntale esto: ¿Preferimos perder \\$500/mes por no contestar o invertimos \\$225 una vez? Cuando decidan, el link sigue aquí: [LINK_PRO]. Me avisas.",
            "Cuándo usarlo": "Objeción del socio"
        },
        {
            "Situación": "19. Cierre por escasez real",
            "Cierre para el bot": "No es presión falsa: solo meto 20 alumnos/mes al grupo de soporte pa’ darles calidad. Quedan 3 cupos esta semana. Si te sirve, asegura el tuyo: [LINK_PRO] ¿Te guardo uno?",
            "Cuándo usarlo": "Escasez verdadera"
        },
        {
            "Situación": "20. Cierre “última bala”",
            "Cierre para el bot": "Parce, ya te di precio, beneficios, garantía y casos. Si aún no, es porque no es pa’ ti y todo bien. Pero si es pa’ ti y no actúas, en 3 meses me vas a escribir bravo porque no lo hiciste antes. Link final: [LINK_PRO] ¿Sí o no?",
            "Cuándo usarlo": "Cuando ya se dijo todo"
        }
    ],
    "Comparativas": [
        {
            "Característica": "Objetivo",
            "Plan Base $45": "Aprender",
            "Plan Pro $250": "Vender en automático",
            "Empresarial $500": "Escalar sin tocar nada"
        },
        {
            "Característica": "Metodología VAI",
            "Plan Base $45": "Intro",
            "Plan Pro $250": "Completa + Plantillas",
            "Empresarial $500": "Completa + Implementación + mentorías"
        },
        {
            "Característica": "Bot de WhatsApp IA",
            "Plan Base $45": "No incluido",
            "Plan Pro $250": "sí 100% funcional y listo para vender + optimización diaria",
            "Empresarial $500": "sí 100% funcional y listo para vender + optimización diaria"
        },
        {
            "Característica": "Responde 24/7",
            "Plan Base $45": "No",
            "Plan Pro $250": "Sí",
            "Empresarial $500": "Sí"
        },
        {
            "Característica": "Soporte",
            "Plan Base $45": "No",
            "Plan Pro $250": "Grupo WhatsApp + En vivos",
            "Empresarial $500": "Equipo dedicado, comunicación directa vía WhatsApp, Google Meet y Loom"
        },
        {
            "Característica": "Campañas Meta Ads",
            "Plan Base $45": "Teoría básica",
            "Plan Pro $250": "Asesoría pa’ que las hagas",
            "Empresarial $500": "Nosotros las creamos y optimizamos"
        },
        {
            "Característica": "Diseño publicitario",
            "Plan Base $45": "Plantillas básicas",
            "Plan Pro $250": "Te asesoramos",
            "Empresarial $500": "Te creamos y diseñamos todo el material publicitario"
        },
        {
            "Característica": "Mensualidad",
            "Plan Base $45": "$0 - Sin mensualidad",
            "Plan Pro $250": "$100/mes: Soporte + Mejoras",
            "Empresarial $500": "$225/mes: Resultados + Mentorías + soporte 24/7"
        },
        {
            "Característica": "¿Pa' quién es?",
            "Plan Base $45": "Si quieres solo aprender",
            "Plan Pro $250": "Si ya vendes y quieres automatizar",
            "Empresarial $500": "Si ya tienes ventas pero quieres escalar sin tocar nada"
        },
        {
            "Característica": "ROI esperado",
            "Plan Base $45": "Conocimiento",
            "Plan Pro $250": "Recuperas en 5 ventas",
            "Empresarial $500": "Equipo se paga solo con 1 cliente nuevo"
        },
        {
            "Característica": "Link",
            "Plan Base $45": "Comprar Base",
            "Plan Pro $250": "Comprar Pro",
            "Empresarial $500": "Comprar Empresarial"
        }
    ],
    "Diccionario_Router": [
        {
            "Palabra_Clave": "ropa",
            "Vertical_Master": "E-commerce/Tiendas"
        },
        {
            "Palabra_Clave": "calzado",
            "Vertical_Master": "E-commerce/Tiendas"
        },
        {
            "Palabra_Clave": "zapatos",
            "Vertical_Master": "E-commerce/Tiendas"
        },
        {
            "Palabra_Clave": "shopify",
            "Vertical_Master": "E-commerce/Tiendas"
        },
        {
            "Palabra_Clave": "tienda online",
            "Vertical_Master": "E-commerce/Tiendas"
        },
        {
            "Palabra_Clave": "ecommerce",
            "Vertical_Master": "E-commerce/Tiendas"
        },
        {
            "Palabra_Clave": "carrito",
            "Vertical_Master": "E-commerce/Tiendas"
        },
        {
            "Palabra_Clave": "stock",
            "Vertical_Master": "E-commerce/Tiendas"
        },
        {
            "Palabra_Clave": "abogado",
            "Vertical_Master": "Servicios Profesionales"
        },
        {
            "Palabra_Clave": "psicolog",
            "Vertical_Master": "Servicios Profesionales"
        },
        {
            "Palabra_Clave": "dentista",
            "Vertical_Master": "Servicios Profesionales"
        },
        {
            "Palabra_Clave": "coach",
            "Vertical_Master": "Servicios Profesionales"
        },
        {
            "Palabra_Clave": "consultorio",
            "Vertical_Master": "Servicios Profesionales"
        },
        {
            "Palabra_Clave": "contador",
            "Vertical_Master": "Servicios Profesionales"
        },
        {
            "Palabra_Clave": "nutricionista",
            "Vertical_Master": "Servicios Profesionales"
        },
        {
            "Palabra_Clave": "terapia",
            "Vertical_Master": "Servicios Profesionales"
        },
        {
            "Palabra_Clave": "restaurante",
            "Vertical_Master": "Negocios Locales"
        },
        {
            "Palabra_Clave": "barberia",
            "Vertical_Master": "Negocios Locales"
        },
        {
            "Palabra_Clave": "peluqueria",
            "Vertical_Master": "Negocios Locales"
        },
        {
            "Palabra_Clave": "spa",
            "Vertical_Master": "Negocios Locales"
        },
        {
            "Palabra_Clave": "cafe",
            "Vertical_Master": "Negocios Locales"
        },
        {
            "Palabra_Clave": "hotel",
            "Vertical_Master": "Negocios Locales"
        },
        {
            "Palabra_Clave": "delivery",
            "Vertical_Master": "Negocios Locales"
        },
        {
            "Palabra_Clave": "infoproductor",
            "Vertical_Master": "Emprendedor Digital"
        },
        {
            "Palabra_Clave": "mentor",
            "Vertical_Master": "Emprendedor Digital"
        },
        {
            "Palabra_Clave": "afiliado",
            "Vertical_Master": "Emprendedor Digital"
        },
        {
            "Palabra_Clave": "curso",
            "Vertical_Master": "Emprendedor Digital"
        },
        {
            "Palabra_Clave": "lanzamiento",
            "Vertical_Master": "Emprendedor Digital"
        },
        {
            "Palabra_Clave": "diseñador",
            "Vertical_Master": "Agencias/Freelancers"
        },
        {
            "Palabra_Clave": "freelancer",
            "Vertical_Master": "Agencias/Freelancers"
        },
        {
            "Palabra_Clave": "agencia",
            "Vertical_Master": "Agencias/Freelancers"
        },
        {
            "Palabra_Clave": "community",
            "Vertical_Master": "Agencias/Freelancers"
        },
        {
            "Palabra_Clave": "marketer",
            "Vertical_Master": "Agencias/Freelancers"
        },
        {
            "Palabra_Clave": "publicidad",
            "Vertical_Master": "Agencias/Freelancers"
        },
        {
            "Palabra_Clave": "consultor",
            "Vertical_Master": "Profesionales Independientes"
        },
        {
            "Palabra_Clave": "fotografo",
            "Vertical_Master": "Profesionales Independientes"
        },
        {
            "Palabra_Clave": "arquitecto",
            "Vertical_Master": "Profesionales Independientes"
        },
        {
            "Palabra_Clave": "independiente",
            "Vertical_Master": "Profesionales Independientes"
        },
        {
            "Palabra_Clave": "sede",
            "Vertical_Master": "Empresa Mediana"
        },
        {
            "Palabra_Clave": "sucursal",
            "Vertical_Master": "Empresa Mediana"
        },
        {
            "Palabra_Clave": "equipo",
            "Vertical_Master": "Empresa Mediana"
        },
        {
            "Palabra_Clave": "empresa",
            "Vertical_Master": "Empresa Mediana"
        },
        {
            "Palabra_Clave": "10 empleados",
            "Vertical_Master": "Empresa Mediana"
        },
        {
            "Palabra_Clave": "b2b",
            "Vertical_Master": "B2B/Servicios Corp"
        },
        {
            "Palabra_Clave": "corporativo",
            "Vertical_Master": "B2B/Servicios Corp"
        },
        {
            "Palabra_Clave": "distribuidor",
            "Vertical_Master": "B2B/Servicios Corp"
        },
        {
            "Palabra_Clave": "mayorista",
            "Vertical_Master": "B2B/Servicios Corp"
        },
        {
            "Palabra_Clave": "chat",
            "Vertical_Master": "E-commerce Grande"
        },
        {
            "Palabra_Clave": "soporte",
            "Vertical_Master": "E-commerce Grande"
        },
        {
            "Palabra_Clave": "retail",
            "Vertical_Master": "E-commerce Grande"
        },
        {
            "Palabra_Clave": "franquicia",
            "Vertical_Master": "E-commerce Grande"
        },
        {
            "Palabra_Clave": "500 mensajes",
            "Vertical_Master": "E-commerce Grande"
        },
        {
            "Palabra_Clave": "clinica",
            "Vertical_Master": "Salud/Educación"
        },
        {
            "Palabra_Clave": "hospital",
            "Vertical_Master": "Salud/Educación"
        },
        {
            "Palabra_Clave": "universidad",
            "Vertical_Master": "Salud/Educación"
        },
        {
            "Palabra_Clave": "colegio",
            "Vertical_Master": "Salud/Educación"
        },
        {
            "Palabra_Clave": "paciente",
            "Vertical_Master": "Salud/Educación"
        },
        {
            "Palabra_Clave": "inmobiliaria",
            "Vertical_Master": "Franquicias/Inmobiliarias"
        },
        {
            "Palabra_Clave": "constructora",
            "Vertical_Master": "Franquicias/Inmobiliarias"
        },
        {
            "Palabra_Clave": "desarrolladora",
            "Vertical_Master": "Franquicias/Inmobiliarias"
        },
        {
            "Palabra_Clave": "apartamento",
            "Vertical_Master": "Franquicias/Inmobiliarias"
        },
        {
            "Palabra_Clave": "saas",
            "Vertical_Master": "Agencias/SaaS"
        },
        {
            "Palabra_Clave": "software",
            "Vertical_Master": "Agencias/SaaS"
        },
        {
            "Palabra_Clave": "revender",
            "Vertical_Master": "Agencias/SaaS"
        }
    ],
    "Metodos de pago": [
        {
            "Pregunta": "¿Cuáles son los métodos de pago?",
            "Colombia": "Tarjeta crédito/débito, PSE, Efecty, Baloto, Nequi, Daviplata",
            "Chile": "Tarjeta crédito/débito, WebPay, Khipu, Servipag",
            "México": "Tarjeta crédito/débito, OXXO, SPEI, PayPal",
            "Ecuador": "Tarjeta crédito/débito"
        },
        {
            "Pregunta": "¿Puedo pagar desde mi país?",
            "Colombia": "Sí, 100% habilitado",
            "Chile": "Sí, 100% habilitado",
            "México": "Sí, 100% habilitado",
            "Ecuador": "Sí, 100% habilitado"
        },
        {
            "Pregunta": "¿Hay cuotas o pago único?",
            "Colombia": "Sí. Hasta 12 cuotas con tarjeta. Hotmart divide el pago y solo necesitas cupo pa’ 1 cuota",
            "Chile": "Sí. Hasta 12 cuotas con tarjeta",
            "México": "Sí. Hasta 12 cuotas con tarjeta",
            "Ecuador": "Pago único con tarjeta. Cuotas depende del banco"
        },
        {
            "Pregunta": "¿Se puede pagar en moneda local?",
            "Colombia": "Sí. Pagas en COP. Hotmart convierte automático",
            "Chile": "Sí. Pagas en CLP",
            "México": "Sí. Pagas en MXN",
            "Ecuador": "Sí. Pagas en USD. Ecuador usa dólar"
        },
        {
            "Pregunta": "¿Hay reembolsos?",
            "Colombia": "Sí. 7 días de garantía Hotmart. Si no te gusta, pides reembolso desde tu correo de compra.",
            "Chile": "Sí. 7 días de garantía",
            "México": "Sí. 7 días de garantía",
            "Ecuador": "Sí. 7 días de garantía"
        },
        {
            "Pregunta": "¿Qué incluye el pago?",
            "Colombia": "Plan Base/Pro/Empresarial completo. Acceso inmediato + actualizaciones. Pro y Empresarial incluyen soporte.",
            "Chile": "Igual",
            "México": "Igual",
            "Ecuador": "Igual"
        },
        {
            "Pregunta": "¿Hay costos ocultos?",
            "Colombia": "No. El precio que ves es el que pagas. Sin mensualidades en Base.",
            "Chile": "No",
            "México": "No",
            "Ecuador": "No"
        },
        {
            "Pregunta": "¿Puedo cambiar de plan después?",
            "Colombia": "Sí. Si compras Base, luego pagas la diferencia pa’ subir a Pro.",
            "Chile": "Sí",
            "México": "Sí",
            "Ecuador": "Sí"
        },
        {
            "Pregunta": "¿Puedo actualizar de plan?",
            "Colombia": "Sí. Escríbenos y te mandamos link de upgrade con descuento.",
            "Chile": "Sí",
            "México": "Sí",
            "Ecuador": "Sí"
        },
        {
            "Pregunta": "¿El precio incluye soporte?",
            "Colombia": "Base: No. Pro: Grupo WhatsApp. Empresarial: Equipo dedicado 1-a-1",
            "Chile": "Igual",
            "México": "Igual",
            "Ecuador": "Igual"
        }
    ]
}

# ============ FUNCIONES PRINCIPALES ============

def detectar_vertical(mensaje):
    """Detecta el vertical/nicho del usuario según palabras clave."""
    mensaje = mensaje.lower()
    for palabra, vertical in DATA['Diccionario_Router'].items():
        if palabra.lower() in mensaje:
            for item in DATA['Para quien es']:
                if vertical.lower() in item['Ahora cae en Vertical'].lower():
                    return {
                        'vertical': vertical,
                        'plan_recomendado': item['Plan'],
                        'match': palabra
                    }
            return {'vertical': vertical, 'plan_recomendado': 'Plan Pro', 'match': palabra}
    return {'vertical': 'General', 'plan_recomendado': 'Plan Base', 'match': None}


def buscar_objecion(mensaje, plan=None):
    """Busca la objeción más cercana y devuelve la respuesta que cierra."""
    mensaje = mensaje.lower()
    objeciones_filtradas = DATA['objecciones']
    
    if plan:
        objeciones_filtradas = [o for o in objeciones_filtradas if plan.lower() in o['Plan'].lower()]
    
    for obj in objeciones_filtradas:
        if obj['Objeción'].lower() in mensaje or mensaje in obj['Objeción'].lower():
            return {
                'objecion': obj['Objeción'],
                'respuesta': obj['Respuesta que Cierra'],
                'plan': obj['Plan']
            }
    
    todas_objeciones = [o['Objeción'] for o in objeciones_filtradas]
    matches = get_close_matches(mensaje, todas_objeciones, n=1, cutoff=0.4)
    if matches:
        for obj in objeciones_filtradas:
            if obj['Objeción'] == matches[0]:
                return {
                    'objecion': obj['Objeción'],
                    'respuesta': obj['Respuesta que Cierra'],
                    'plan': obj['Plan']
                }
    return None


def buscar_faq(pregunta, plan=None):
    """Busca en las FAQ. Retorna respuesta o None"""
    pregunta = pregunta.lower()
    faqs = DATA['FAQ']
    
    if plan:
        faqs = [f for f in faqs if plan.lower() in f['Plan'].lower()]
    
    for faq in faqs:
        if faq['Pregunta'].lower() in pregunta or pregunta in faq['Pregunta'].lower():
            return {
                'pregunta': faq['Pregunta'],
                'respuesta': faq['Respuesta'],
                'plan': faq['Plan']
            }
    return None


def obtener_plan(nombre_plan):
    """Devuelve toda la info de un plan: precio, links, beneficios"""
    for plan in DATA['Planes']:
        if nombre_plan.lower() in plan['Plan'].lower():
            return plan
    return None


def obtener_cierre_nicho(nicho):
    """Devuelve el mensaje y cierre específico para un nicho"""
    for item in DATA['Nichos']:
        if nicho.lower() in item['Nicho'].lower():
            return {
                'dolor': item['Dolor Principal'],
                'mensaje': item['Mensaje del Bot'],
                'cierre': item['Cierre Específico']
            }
    return None


def obtener_cierre_venta(situacion):
    """Devuelve el cierre según la situación: 'caliente', 'lo pienso', 'está caro', etc"""
    situacion = situacion.lower()
    for cierre in DATA['Cierre de Ventas']:
        if situacion in cierre['Situación'].lower() or situacion in cierre['Cuándo usarlo'].lower():
            return {
                'cierre': cierre['Cierre para el bot'],
                'cuando_usar': cierre['Cuándo usarlo']
            }
    return None


def comparar_planes():
    """Devuelve tabla comparativa de los 3 planes"""
    return DATA['Comparativas']


def obtener_metodo_pago(pais='Colombia'):
    """Devuelve métodos de pago disponibles por país"""
    pais = pais.capitalize()
    for metodo in DATA['Metodos de pago']:
        if pais in metodo:
            return metodo
    return DATA['Metodos de pago'][0]


def obtener_link(tipo):
    """Obtiene links de pago o whatsapp."""
    for link in DATA['Links Hub']:
        if tipo.lower() in link['Links'].lower():
            return link['Unnamed: 1']
    return None


# ============ LÓGICA PRINCIPAL LUNA ============

def luna_responder(mensaje_usuario, estado_conversacion={}):
    """
    Función principal que procesa el mensaje usando todas las reglas del JSON
    estado_conversacion guarda: {'plan': 'Pro', 'vertical': 'Profesionales', 'paso': 'objecion'}
    """
    mensaje = mensaje_usuario.lower()
    
    # 1. SALUDO INICIAL
    if any(p in mensaje for p in ['hola', 'info', 'planes', 'buenas', 'buenos']) and not estado_conversacion:
        return {
            'respuesta': "¡Hola! 👋 Soy Luna, tu asistente de IA para ventas. ¿A qué te dedicas?",
            'estado': {'paso': 'detectar_nicho'}
        }
    
    # 2. DETECTAR NICHO/VERTICAL
    if estado_conversacion.get('paso') == 'detectar_nicho':
        vertical_info = detectar_vertical(mensaje)
        plan = obtener_plan(vertical_info['plan_recomendado'])
        
        texto = f"Perfecto, para {vertical_info['vertical']} recomiendo el {plan['Plan']}.\n\n"
        texto += f"💰 Inversión: ${plan['Precio']} USD\n"
        texto += f"✅ {plan['Beneficio principal']}\n\n"
        texto += "¿Te explico qué incluye o tienes alguna duda?"
        
        return {
            'respuesta': texto,
            'estado': {'paso': 'presentar_plan', 'plan': plan['Plan'], 'vertical': vertical_info['vertical']}
        }
    
    # 3. MANEJAR OBJECIONES - Usa las 238 del JSON
    palabras_objecion = ['caro', 'precio', 'dudo', 'pienso', 'después', 'no tengo', 'garantía', 'tiempo', 'difícil']
    if any(p in mensaje for p in palabras_objecion):
        plan_actual = estado_conversacion.get('plan', 'Plan Pro')
        obj = buscar_objecion(mensaje, plan=plan_actual)
        
        if obj:
            respuesta = obj['respuesta'] + "\n\n¿Te comparto el link de pago para asegurar tu cupo?"
            return {
                'respuesta': respuesta,
                'estado': {**estado_conversacion, 'paso': 'cierre'}
            }
    
    # 4. PREGUNTAS FAQ
    faq = buscar_faq(mensaje, plan=estado_conversacion.get('plan'))
    if faq:
        return {
            'respuesta': faq['respuesta'] + "\n\n¿Resuelve tu duda?",
            'estado': estado_conversacion
        }
    
    # 5. CIERRE DE VENTA
    if mensaje in ['sí', 'si', 'dale', 'ok', 'listo', 'quiero'] and estado_conversacion.get('paso') == 'cierre':
        plan = obtener_plan(estado_conversacion.get('plan', 'Plan Pro'))
        link = obtener_link(plan['Plan'])
        
        cierre_nicho = obtener_cierre_nicho(estado_conversacion.get('vertical', ''))
        texto_cierre = cierre_nicho['cierre'] if cierre_nicho else obtener_cierre_venta('caliente')['cierre']
        
        respuesta = f"{texto_cierre}\n\n👉 Link de pago: {link}\n\n"
        respuesta += "Una vez pagues, te llega acceso inmediato por correo. ¿Alguna última duda?"
        
        return {
            'respuesta': respuesta,
            'estado': {**estado_conversacion, 'paso': 'post_pago'}
        }
    
    # 6. COMPARAR PLANES
    if 'diferencia' in mensaje or 'comparar' in mensaje or 'planes' in mensaje:
        comp = comparar_planes()
        texto = "**Comparativa rápida:**\n\n"
        texto += f"Base $45: {comp['Bot de WhatsApp IA']['plan_base']}\n"
        texto += f"Pro $250: {comp['Bot de WhatsApp IA']['plan_pro']}\n"
        texto += f"Empresarial $500: {comp['Bot de WhatsApp IA']['empresarial']}\n\n"
        texto += "¿Cuál se ajusta más a ti?"
        return {'respuesta': texto, 'estado': estado_conversacion}
    
    # 7. MÉTODOS DE PAGO
    if any(p in mensaje for p in ['pago', 'pagar', 'tarjeta', 'cuotas']):
        metodos = obtener_metodo_pago('Colombia')
        texto = f"Métodos de pago: {metodos['Colombia']}. {metodos['Pregunta']}"
        return {'respuesta': texto, 'estado': estado_conversacion}
    
    # DEFAULT
    return {
        'respuesta': "No entendí bien 😅 ¿Me dices a qué te dedicas o qué duda tienes sobre los planes?",
        'estado': estado_conversacion
    }


# ============ API WEBHOOK PARA MAKE ============

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Endpoint para Make/ManyChat/WhatsApp
    Recibe: {"mensaje": "texto del usuario", "estado": {}}
    Devuelve: {"respuesta": "texto del bot", "estado": {}}
    """
    data = request.json
    mensaje = data.get('mensaje', '')
    estado = data.get('estado', {})
    
    # Llama a Luna con las reglas duras + 238 objeciones del JSON
    resultado = luna_responder(mensaje, estado)
    
    return jsonify({
        "respuesta": resultado['respuesta'],
        "estado": resultado['estado']
    })


@app.route('/health', methods=['GET'])
def health():
    """Health check para Make"""
    return jsonify({"status": "ok", "objeciones_cargadas": len(DATA['objecciones'])})


if __name__ == '__main__':
    print(f"🚀 Luna Bot iniciado con {len(DATA['objecciones'])} objeciones cargadas")
    app.run(host='0.0.0.0', port=5000, debug=False)
