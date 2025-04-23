🧠 Análisis de Noticias sobre IA
Este proyecto extrae noticias de La Nación Web, las analiza con NLP y envía un resumen por correo.
🚀 Funciones principales:
✅ Scraping: Obtiene los últimos artículos sobre inteligencia artificial.
✅ Procesamiento NLP: Usa spaCy para estructurar el texto.
✅ Análisis de palabras: Genera una nube de palabras y estadísticas.
✅ Envío de noticias: Automatización con yagmail.
📄 Instalación
!pip install spacy yagmail beautifulsoup4 wordcloud -q  
!python -m spacy download es_core_news_lg  


📧 Configuración de correo
1️⃣ Configura OAuth en Google Console.
2️⃣ Guarda el archivo JSON en /content/drive/MyDrive/archivoCredencialG.json.
3️⃣ Usa yagmail para el envío automático.
🔮 Mejoras futuras
- Integrar otros medios de noticias.
- Mejorar visualización de datos.
- Automatizar reportes.

📌 Autor: Daiana E. Gomez  📅 Última actualización: Abril 2025


