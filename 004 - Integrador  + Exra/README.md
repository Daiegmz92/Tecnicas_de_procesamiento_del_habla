# 🧠 Análisis de Noticias sobre IA  
📌 Autor: Daiana E. Gomez 
📅 Última actualización: Abril 2025

Este proyecto extrae artículos de *La Nación*, los analiza con **NLP** y envía un resumen por correo.  

## 🚀 Funcionalidades  
- **Scraping:** Obtiene noticias automáticamente.  
- **Procesamiento NLP:** Usa `spaCy` para analizar el texto.  
- **Nube de palabras:** Identifica términos clave.  
- **Envío de noticias:** Automatización con `yagmail`.  

## 📄 Instalación  
```bash
pip install spacy yagmail beautifulsoup4 wordcloud
python -m spacy download es_core_news_lg
📧 Configuración de correo
1️⃣ Configura OAuth en Google Console.
2️⃣ Guarda el archivo JSON en entorno local o drive de google.
3️⃣ Usa yagmail para el envío automático.












