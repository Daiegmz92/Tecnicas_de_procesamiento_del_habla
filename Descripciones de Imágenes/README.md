# 🖼️ Generación de Descripciones de Imágenes con IA

Este repositorio contiene dos notebooks diseñados para introducir y experimentar con la generación automática de descripciones para imágenes utilizando modelos de lenguaje-visión (VLMs) basados en Transformers.

## 📌 Contenido

### 1. `captioning_avanzado_colab.ipynb`  
Un notebook interactivo completo que permite:

- Cargar imágenes desde la interfaz.
- Generar subtítulos automáticos en inglés con el modelo BLIP (`Salesforce/blip-image-captioning-large`).
- Traducir automáticamente al español con `Helsinki-NLP/opus-mt-en-es`.
- Ejecutar todo mediante una interfaz Gradio amigable para el usuario.
- Reflexionar sobre la precisión, potencial y limitaciones del sistema.

Ideal para clases prácticas, demostraciones interactivas o prototipos de apps accesibles sin código.

### 2. `captioning_basico_blip.ipynb`  
Una versión más simple, pensada como introducción al tema:

- Instala y configura `transformers`, `Pillow` y `torch`.
- Usa el modelo `Salesforce/blip-image-captioning-base` para generar una descripción textual directamente en Python.
- Incluye una versión simple de interfaz con Gradio sin traducción automática.

Perfecto para usuarios sin experiencia previa que deseen comprender el pipeline básico de image captioning con IA.

---

## 🧠 Modelos Utilizados

| Tarea                         | Modelo                                | Fuente                            |
|------------------------------|----------------------------------------|-----------------------------------|
| Image Captioning             | `Salesforce/blip-image-captioning-*`  | [HuggingFace](https://huggingface.co/Salesforce) |
| Traducción (inglés → español) | `Helsinki-NLP/opus-mt-en-es`          | [HuggingFace](https://huggingface.co/Helsinki-NLP) |

---

## 🚀 Cómo Ejecutarlo

### En Google Colab:
1. Abrí uno de los notebooks desde tu repositorio.
2. Asegurate de habilitar el entorno con GPU para mayor velocidad.
3. Ejecutá las celdas en orden.

> En el caso del archivo avanzado, al final se abrirá una URL donde podrás interactuar con la interfaz Gradio.

---

## 📚 Recursos Recomendados

- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [BLIP Paper (Bootstrapping Language-Image Pre-training)](https://arxiv.org/abs/2201.12086)
- [Gradio Docs](https://www.gradio.app/docs)
- [Imagenet Dataset](https://www.image-net.org/)
- [Helsinki-NLP Translation Models](https://huggingface.co/Helsinki-NLP)

---

## ✨ Próximos pasos y sugerencias

- Explorar otros modelos de captioning (como GIT, Flamingo o Llava).
- Agregar funcionalidades de *detección de objetos* o *preguntas visuales* (VQA).
- Mejorar la calidad de traducción con modelos más grandes.
- Integrar un sistema de métricas de calidad automática de descripciones.
- Aplicaciones reales: accesibilidad web, curación de contenido, archivado multimedia, entre otras.

---

## 🛡️ Licencia

Este repositorio se distribuye solo con fines **educativos y de demostración**. No utilizar con fines comerciales ni para sistemas en producción sin revisión ética y validación previa.

