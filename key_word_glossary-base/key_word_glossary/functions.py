# Cargamos librerias

import pandas as pd
import people_also_ask
from youtubesearchpython import VideosSearch
import time
from numpy import random

# Esta función saca key word, video y pregunta-respuesta en formto lista de la KeyWord que queramos en formato HTML

def key_word_glossary_html(kw, n=10, search='Search'):
    
    '''
    Esta función sirve para sacar las preguntas frecuentes y su respectiva respuesta
    para cualquier key word
    
    Parameters
    ----------
    kw: string
        key word de la que queremos encontrar las preguntas y respuestas frecuentes 
    
    n: int
        número de preguntas máximas que queremos sacar de la key word, por defecto 10
    
    search: string
        palabra 'Buscar' en el idioma que vamos a buscar las palabras frecuentes, por defecto en inglés
    
    Returns
    -------
    list
        devuelve una lista pregunta-respuesta de la key Word 
    '''
        
    # Esta parte saca las preguntas limpias
    preguntas = [pregunta.split(search)[0] for pregunta in people_also_ask.get_related_questions(kw, n)]

    # Esta parte saca las respuestas limpias
    respuestas= []

    for pregunta in preguntas:
        try:
            # Si la respuesta es una definición incluimos la respuesta
            if people_also_ask.get_answer(pregunta)['snippet_type'] == 'Definition Featured Snippet':
                time.sleep(random.uniform(1, 3))
                respuestas.append(people_also_ask.get_answer(pregunta)['response'])
            # Si no es una definición(tabla) incluimos un elemento vacío en la respuesta
            else:
                respuestas.append('')
        # Si no encuetra respuesta incluimos un elemento vacío en las respuestas
        except:
            respuestas.append('')
        time.sleep(random.uniform(3, 5))

    # Esta parte incluye en una lista key word, link video youtube y pregunta-respuesta
    pregunta_respuesta = [kw]
    
    try:
        pregunta_respuesta.append(VideosSearch(kw, limit = 1).result()['result'][0]['link'])
    except:
        pregunta_respuesta.append('')

    # Introducimos pregunta-respuesta en la lista anterior 
    contenido = []
    
    for pregunta, respuesta in zip(preguntas, respuestas):
        contenido.append('<h3>' + pregunta + '<h3>' + '<p>' + respuesta + '<p>')
        
    contenido = ''.join(contenido)
    pregunta_respuesta.append(contenido)
    
    return pregunta_respuesta

# Esta función saca key word, video y pregunta-respuesta en formto lista de la KeyWord que queramos

def key_word_glossary(kw, n=10, search='Search'):
    
    '''
    Esta función sirve para sacar las preguntas frecuentes y su respectiva respuesta
    para cualquier key word
    
    Parameters
    ----------
    kw: string
        key word de la que queremos encontrar las preguntas y respuestas frecuentes 
    
    n: int
        número de preguntas máximas que queremos sacar de la key word, por defecto 10
    
    search: string
        palabra 'Buscar' en el idioma que vamos a buscar las palabras frecuentes, por defecto en inglés
    
    Returns
    -------
    list
        devuelve una lista pregunta-respuesta de la key Word 
    '''
        
    # Esta parte saca las preguntas limpias
    preguntas = [pregunta.split(search)[0] for pregunta in people_also_ask.get_related_questions(kw, n)]

    # Esta parte saca las respuestas limpias
    respuestas= []

    for pregunta in preguntas:
        try:
            # Si la respuesta es una definición incluimos la respuesta
            if people_also_ask.get_answer(pregunta)['snippet_type'] == 'Definition Featured Snippet':
                time.sleep(random.uniform(1, 3))
                respuestas.append(people_also_ask.get_answer(pregunta)['response'])
            # Si no es una definición(tabla) incluimos un elemento vacío en la respuesta
            else:
                respuestas.append('')
        # Si no encuetra respuesta incluimos un elemento vacío en las respuestas
        except:
            respuestas.append('')
        time.sleep(random.uniform(3, 5))

    # Esta parte incluye en una lista key word, link video youtube y pregunta-respuesta
    pregunta_respuesta = [kw]
    
    try:
        pregunta_respuesta.append(VideosSearch(kw, limit = 1).result()['result'][0]['link'])
    except:
        pregunta_respuesta.append('')

    # Introducimos pregunta-respuesta en la lista anterior    
    for pregunta, respuesta in zip(preguntas, respuestas):
        pregunta_respuesta.append(pregunta)
        pregunta_respuesta.append(respuesta)
    
    return pregunta_respuesta

# Sacamos el excel de la lista anterior para todas las key words que queramos

def key_words_glossary_to_excel(kws, n=10, search='Search'):
    
    '''
    Esta función sirve para sacar las preguntas frecuentes y su respectiva respuesta
    para cualquier key word y almacenarlas en un excel
    
    Parameters
    ----------
    kws: list
        lista de keywords de las que queremos sacar las preguntas frecuentes
    
    n_preguntas: int
        número de preguntas máximas que queremos sacar de la key word, por defecto 10
    
    search: string
        palabra 'Buscar' en el idioma que vamos a buscar las palabras frecuentes, por defecto en inglés
    
    Returns
    -------
    df
        devuelve un df de preguntas y respuestas
    '''
    
    dffq = pd.DataFrame()
    for kw in kws:
        faq = key_word_glossary(kw, n, search)
        df = pd.DataFrame(faq).T
        dffq = pd.concat([dffq, df])
        dffq.to_excel('glosario.xlsx', index = False) # Vamos almacenando los resultados en un excel (marcar la ruta donde quieres que se ubique el excel)
        print(kw)
        time.sleep(random.uniform(1, 3))
        
    return dffq

# Traducimos el excel glosario al idioma que queramos

def glossary_traduction(route : str, language = 'ES'):
    
    '''
    Esta función sirve para traducir el glosario en formato excel al idioma que queramos
    
    Parameters
    ----------
    route: str
        Ruta en la que tenemos ubicado el excel glosario
    
    language: str
        Idioma al que queremos traducir el glosario
        
    
    Returns
    -------
    df
        devuelve el df traducido
    '''
    
    import deepl

    translator = deepl.Translator(str(input('Introduce la clave de autentificación de la API de DeepL:'))) # Introducimos la clave de autentificacion para poder acceder a las traducciones

    df_original = pd.read_excel(route) # Importamos el excel escrapeado

    df_traduction = pd.DataFrame() # Creamos un DataFrame vacío
    df_traduction[0] = df_original[0] # Añadimos al DataFrame la KeyWord
    df_traduction[1] = df_original[1] # Añadimos al DataFrame el link del video

    for column in range(2, df_original.shape[1]):
        print(column)
        traduction = []
        for sentence in df_original[column]:
            try:
                traduction.append(translator.translate_text(sentence, target_lang=language).text)
            except:
                traduction.append('')

        df_traduction[column] = traduction
        df_traduction.to_excel('glosario_traducido.xlsx', index = False)

    return df_traduction