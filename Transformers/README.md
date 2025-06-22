# 📚 Aplicaciones Prácticas de PLN con Modelos Generativos

Este repositorio contiene notebooks interactivos que demuestran cómo aplicar modelos de lenguaje preentrenados (Transformers) en español para resolver tareas reales de **Procesamiento de Lenguaje Natural (PLN)**, sin necesidad de entrenar modelos desde cero.

Incluye dos enfoques complementarios:

- 🧠 **Hugging Face Transformers**: Modelos BERT, GPT y T5 optimizados para español.
- 🌐 **Google Gemini API**: Modelos de lenguaje de última generación de Google vía `google-generativeai`.

---

## 🔍 Notebooks disponibles

### ✅ `huggingface_transformers_pln.ipynb`
Uso de pipelines de Hugging Face para:

- Análisis de sentimiento
- Clasificación Zero-Shot
- Resumen automático
- Traducción
- Generación de texto
- Evaluación en frases con sarcasmo y jergas locales

### ✅ `google_gemini_pln.ipynb`
Aplicaciones de Gemini en:

- Sumarización
- Clasificación de sentimiento
- NER (Reconocimiento de Entidades)
- Respuesta a preguntas
- Traducción y generación
- Clasificación Zero-Shot
- Actividad práctica con texto libre

---

## ⚙️ Requisitos

### Para el notebook de Hugging Face:
```bash
pip install transformers
🧪 ¿Qué vas a aprender?
Usar modelos preentrenados con una sola línea de código (pipeline)

Aplicar PLN real: clasificación, resumen, QA, generación, NER y más

Evaluar limitaciones de los modelos (sesgos, contexto, sarcasmo)

Integrar modelos de Gemini en flujos de trabajo personalizados

💡 Casos de uso sugeridos
Automatización de respuestas en atención al cliente

Clasificación de comentarios o tickets

Resumen de artículos extensos

Traducción de contenidos multilingües

Asistentes virtuales o chatbots

📁 Estructura del repositorio
Copiar
Editar
📂 pln-transformers
├── huggingface_transformers_pln.ipynb
├── google_gemini_pln.ipynb
└── README.md
📬 Contacto
¿Comentarios o sugerencias?
Podés abrir un issue o contactarme vía LinkedIn https://www.linkedin.com/in/daiana-elizabeth-gomez/ o [d.e.g.983@gmail.com].

¡Explorá el poder de los modelos de lenguaje en español! 🇦🇷🤖🌐
