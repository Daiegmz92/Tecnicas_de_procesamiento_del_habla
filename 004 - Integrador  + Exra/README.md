# 🧠 Análisis de Noticias sobre IA  

Este proyecto obtiene artículos de *La Nación*, los analiza con **NLP** y envía un resumen por correo.  

## 🚀 Funciones principales  
✅ **Scraping:** Extrae noticias automáticamente.  
✅ **Procesamiento NLP:** Usa `spaCy` para estructurar el texto.  
✅ **Análisis de palabras:** Crea una nube de palabras.  
✅ **Envío automático:** Usa `yagmail` para enviar resúmenes.  

## 📄 Instalación  
```bash
pip install spacy yagmail beautifulsoup4 wordcloud
python -m spacy download es_core_news_lg    

📧 Configuración de correo
1️⃣ Configura OAuth en Google Console.
2️⃣ Guarda el archivo JSON en /content/drive/MyDrive/archivoCredencialG.json.
3️⃣ Usa yagmail para el envíoautomático.

🔮 Mejoras futuras
- Integrar otros medios de noticias.
- Mejorar visualización de datos.
- Automatizar reportes.

📌 Autor: Daiana E. Gomez  📅 Última actualización: Abril 2025


