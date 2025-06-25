# 🤖 Sistema de Detección de Quejas y Respuesta Automática para E-commerce

Este proyecto fue desarrollado como trabajo final para la materia **Procesamiento del Habla**. Su objetivo es crear un sistema prototipo capaz de detectar quejas en mensajes de clientes y generar respuestas automáticas, simulando el funcionamiento de un sistema de soporte en empresas de e-commerce.

---

## 🎯 Objetivo

Automatizar la atención al cliente mediante un sistema que:

- Detecta si un ticket contiene una queja.
- Clasifica el tipo de problema.
- Extrae información clave del mensaje.
- Genera una respuesta automática basada en la queja.

---

## 🛠️ Herramientas utilizadas

- `Pandas` para la manipulación de datos.
- `Transformers` y `Pipelines` de [Hugging Face](https://huggingface.co/).
- API de `Gemini` (Google AI) para generación de texto.
- `Gradio` para prototipar una interfaz simple.
- `Python` y `Jupyter Notebook` para desarrollo y presentación.

---

## ⚙️ Cómo funciona el sistema

1. ### **Simulación de datos**
   Se genera un conjunto de tickets simulados con diferentes tipos de mensajes: quejas, consultas y comentarios neutros.

2. ### **Clasificación de quejas**
   Se utiliza un modelo de Transformers para identificar si el texto es una queja.

3. ### **Extracción de tema principal**
   Se implementa una pipeline de análisis para detectar cuál es el problema principal: entrega, producto, atención, etc.

4. ### **Generación de respuesta automática**
   Se conecta a la API de Gemini o se usa un modelo local para generar una respuesta personalizada según el contenido del mensaje.

5. ### **Interfaz en Gradio**
   Se crea una demo visual donde se puede escribir un mensaje y recibir una respuesta automática en tiempo real.

---

📚 Créditos
Desarrollado por Maria Florencia Lopez, Daiana Elizabeth Gomez y Jordi Galman como proyecto final de la materia Procesamiento del Habla.

📌 Notas
Este proyecto es un prototipo y no reemplaza un sistema de atención profesional.

La API de Gemini requiere credenciales. Podés sustituirla por un modelo local de Hugging Face si no tenés acceso.

