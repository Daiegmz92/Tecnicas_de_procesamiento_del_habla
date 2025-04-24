# 📊 Análisis de Texto con Bag of Words y TF-IDF

## 🚀 Descripción
Este proyecto implementa **Bag of Words (BoW) y TF-IDF** para el análisis de texto, utilizando `scikit-learn`. Estas técnicas permiten convertir documentos en representaciones numéricas, facilitando la evaluación de la relevancia de palabras dentro de un corpus.

## ⚙️ Instalación
Antes de ejecutar el código, asegúrate de tener `scikit-learn`, `pandas` y `numpy` instalados:

```bash
pip install scikit-learn pandas numpy


📌 Estructura del Código
- Bag of Words (BoW): Representa los textos como una matriz de frecuencias de palabras.
- TF-IDF: Ajusta la relevancia de cada término en función de su aparición en múltiples documentos.
- Visualización: Se generan DataFrames para interpretar los resultados.

🛠️ Cómo Ejecutar
Ejecuta el script en un entorno con Python 3.x:
python script.py


Se imprimirá el vocabulario generado, la representación BoW y la matriz TF-IDF.
📊 Ejemplo de Salida
Vocabulario generado: {'el': 4, 'perro': 7, 'muerde': 6, 'al': 0, 'hombre': 5, 'come': 2, 'carne': 1, 'comida': 3}

Representación Bag of Words:
   al  carne  come  comida  el  hombre  muerde  perro
0   1      0     0       0   1       1       1      1
1   1      0     0       0   1       1       1      1
2   0      1     1       0   1       0       0      1
3   0      0     1       1   1       1       0      0

Matriz TF-IDF:
        al     carne      come    comida        el    hombre   muerde    perro  
0  0.51647  0.000000  0.000000  0.000000  0.341846  0.418127  0.51647  0.418127  
1  0.51647  0.000000  0.000000  0.000000  0.341846  0.418127  0.51647  0.418127  
2  0.00000  0.659191  0.519714  0.000000  0.343993  0.000000  0.00000  0.420753  
3  0.00000  0.000000  0.519714  0.659191  0.343993  0.420753  0.00000  0.000000  

```
## 📚 Conclusión
- ✔️ **Bag of Words** convierte los textos en una matriz de frecuencia de palabras.
- ✔️ **TF-IDF** ajusta la importancia de cada término según su aparición en el corpus.
- ✔️ **Ambas técnicas** son esenciales para análisis de texto y modelos de Machine Learning.

## ✨ Contribuciones
- Si deseas mejorar este análisis, ¡envía un **Pull Request** o abre una **Issue**! 🚀






