# Aplicaciones de Transformers en Procesamiento de Lenguaje Natural

# Texto de ejemplo para pruebas
texto = """Querido MercadoLibre, la semana pasada pedí una figura de acción de Optimus Prime desde su tienda online.
Para mi sorpresa, cuando abrí el paquete, descubrí horrorizado que me habían enviado una figura de Megatron.
Como fan de los Autobots, espero que entiendan mi decepción. Solicito un cambio urgente del producto."""

# 1. Clasificación de texto
from transformers import pipeline
import pandas as pd

classifier = pipeline("text-classification", model="pysentimiento/robertuito-sentiment-analysis")
outputs = classifier(texto)
print("Clasificación de texto:")
print(pd.DataFrame(outputs), end="\n\n")

# 2. Reconocimiento de Entidades Nombradas (NER)
ner_tagger = pipeline("ner", model="mrm8488/bert-spanish-cased-finetuned-ner", aggregation_strategy="simple")
print("Entidades en el primer texto:")
print(pd.DataFrame(ner_tagger(texto)), end="\n\n")

texto_2 = "Lionel Messi nació en Rosario, jugó en el FC Barcelona y ahora vive en Miami."
print("Entidades en el segundo texto:")
print(pd.DataFrame(ner_tagger(texto_2)), end="\n\n")

# 3. Respuesta a preguntas
reader = pipeline("question-answering", model="PlanTL-GOB-ES/roberta-large-bne-sqac")
pregunta = "¿Qué quiere el cliente?"
respuesta = reader(question=pregunta, context=texto)
print("Respuesta (modelo SQAC):")
print(pd.DataFrame([respuesta]), end="\n\n")

lector = pipeline("question-answering", model="mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es")
respuesta_alt = lector(question=pregunta, context=texto)
print("Respuesta (modelo SQuAD2 español):")
print(pd.DataFrame([respuesta_alt]), end="\n\n")

# 4. Resumen automático
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model_name = "csebuetnlp/mT5_multilingual_XLSum"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

resumidor = pipeline("summarization", model=model, tokenizer=tokenizer)
resumen = resumidor(texto, max_length=80, min_length=20, do_sample=False)
print("Resumen del texto:")
print(resumen[0]['summary_text'], end="\n\n")

# 5. Traducción (español a inglés y a alemán)
translator_es_en = pipeline("translation_es_to_en", model="Helsinki-NLP/opus-mt-es-en")
print("Traducción al inglés:")
print(translator_es_en(texto)[0]['translation_text'], end="\n\n")

traductor_es_de = pipeline("translation", model="Helsinki-NLP/opus-mt-es-de")
texto_extra = "La inteligencia artificial está transformando la forma en que vivimos y trabajamos."
print("Traducción al alemán:")
print(traductor_es_de(texto_extra)[0]['translation_text'], end="\n\n")

# 6. Generación automática de texto
generador = pipeline("text-generation", model="datificate/gpt2-small-spanish")
prompt = texto + "\n\nRespuesta del servicio al cliente:\nEstimado Bumblebee, lamentamos mucho lo ocurrido con su pedido. "

outputs = generador(
    prompt,
    max_new_tokens=150,
    do_sample=True,
    temperature=1.0,
    top_k=50,
    top_p=0.9,
    repetition_penalty=1.3,
    eos_token_id=50256
)

print("Respuesta generada por IA:")
print(outputs[0]['generated_text'])
