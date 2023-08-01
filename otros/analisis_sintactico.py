# Importamos las librerías necesarias
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import ne_chunk
from nltk.chunk import RegexpParser
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.parse import CoreNLPParser
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews

# Descargamos los recursos necesarios para trabajar con NLTK
nltk.download('punkt')                # Tokenizador de oraciones y palabras
nltk.download('averaged_perceptron_tagger')  # Etiquetador gramatical
nltk.download('vader_lexicon')        # Analizador de sentimiento
nltk.download('stopwords')           # Palabras vacías (stopwords)
nltk.download('wordnet')             # Diccionario WordNet
nltk.download('maxent_ne_chunker')   # Named entity chunker
nltk.download('words')               # Corpus de palabras
nltk.download('movie_reviews')       # Diccionario movies

# Definimos una cadena de texto para trabajar con ella
texto = "El gato está sentado en la alfombra. El perro está jugando con su pelota."

# Tokenizamos el texto en oraciones
oraciones = sent_tokenize(texto)

# Creamos un objeto SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Analizamos el sentimiento de cada oración del texto
for i, oracion in enumerate(oraciones, 1):
    print(f"Oración {i}:")
    print(oracion)
    scores = sia.polarity_scores(oracion)
    print("Puntaje de sentimiento:", scores)
    print("Sentimiento más probable:",
          max(scores, key=lambda x: scores[x]), end="\n\n")

# Definimos una cadena de texto de ejemplo
texto = "Me encanta el verano. Es mi estación favorita."

# Analizamos el sentimiento del texto completo
scores = sia.polarity_scores(texto)
print("Puntaje de sentimiento:", scores)

# Definimos una cadena de texto de ejemplo
texto = "El perro ladra. El gato maulla. El perro y el gato juegan juntos."

# Tokenizamos el texto en palabras
palabras = word_tokenize(texto)

# Calculamos la frecuencia de palabras
frecuencia_palabras = FreqDist(palabras)
print(frecuencia_palabras.most_common(5))

# Definimos una oración de ejemplo
oracion = "El gato está jugando en el jardín."

# Tokenizamos la oración en palabras
palabras = word_tokenize(oracion)

# Etiquetamos gramaticalmente las palabras
pos_tags = nltk.pos_tag(palabras)
print(pos_tags)
# NNP representa un nombre propio singular (Proper Noun, singular).
# NN representa un sustantivo singular (Noun, singular).
# VB representa un verbo base (Verb, base form).
# VBG representa un gerundio (Verb, gerund or present participle).
# IN representa una preposición o subordinador (Preposition or subordinating conjunction).
# DT representa un determinante (Determiner).
# El punto final, que se muestra como un punto (punctuation).

# Tokenizamos el texto en palabras
palabras = word_tokenize(texto)

# Definimos una lista de palabras vacías (stopwords) en español
stop_words = set(stopwords.words('spanish'))

# Filtramos las palabras vacías del texto
palabras_filtradas = [
    palabra for palabra in palabras if palabra.casefold() not in stop_words]
print(palabras_filtradas)

# Definimos una lista de palabras para el ejemplo
palabras = ["running", "jumps", "jumping", "better", "best", "dogs", "mice"]

# Stemming con Porter's Stemmer
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in palabras]
print("Stemming:", stemmed_words)

# Lemmatization con WordNet Lemmatizer
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in palabras]
print("Lemmatization:", lemmatized_words)


# Definir un texto de muestra
texto = "Barack Obama nació en Hawaii."

# Tokenizar el texto en palabras
words = word_tokenize(texto)

# Realizar el reconocimiento de entidades nombradas en las palabras
ne_tree = ne_chunk(nltk.pos_tag(words))

# Imprimir las entidades nombradas encontradas en el texto
for subtree in ne_tree.subtrees():
    if subtree.label() == 'PERSON':
        print(' '.join([word for word, tag in subtree.leaves()]))

# Definir un patrón de expresión regular para el chunking
pattern = 'NP: {<DT>?<JJ>*<NN>}'

# Crear un analizador de chunks usando el patrón
chunk_parser = RegexpParser(pattern)

# Analizar las palabras etiquetadas POS usando el analizador de chunks
chunks = chunk_parser.parse(pos_tags)

# Imprimir los chunks encontrados en el texto
for subtree in chunks.subtrees():
    if subtree.label() == 'NP':
        print(' '.join([word for word, tag in subtree.leaves()]))
