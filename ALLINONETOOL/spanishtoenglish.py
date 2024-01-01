def create_translator_english():
    return {
        'el hombre': 'the man', 'la mujer': 'the woman', 'yo soy': 'I am', 'el niño': 'the boy', 'la niña': 'the girl',
        'él': 'he', 'ella': 'she', 'come': 'eats', 'es': 'it is', 'tú': 'you', 'eres': 'you are', 'usted': 'you',
        'la manzana': 'the apple', 'el pan': 'the bread', 'como': 'I eat', 'comes': 'you eat', 'el agua': 'the water',
        'la leche': 'the milk', 'bebe': 'it drinks', 'bebo': 'I drink', 'bebes': 'you drink', 'hola': 'hello',
        'adiós': 'bye', 'buenos días': 'good morning', 'buenas noches': 'good night', 'gracias': 'thank you',
        'mucho gusto': 'nice to meet you', 'sí': 'yes', 'no': 'no', 'por favor': 'please', 'de nada': 'you are welcome',
        'lo siento': 'I am sorry', 'perdón': 'excuse me', 'hablo': 'I speak', 'hablas': 'you speak',
        'español': 'Spanish', 'inglés': 'English', 'disculpe': 'sorry', 'nosotros': 'we', 'nosotras': 'we',
        'somos': 'we are', 'los hombres': 'the men', 'las mujeres': 'the women', 'ustedes': 'you all',
        'son': 'they are', 'bebemos': 'we drink', 'ellos': 'they', 'ellas': 'they', 'beben': 'they drink',
        'los': 'the', 'las': 'the', 'los niños': 'the boys', 'las niñas': 'the girls', 'el vino': 'the wine',
        'el libro': 'the book', 'la carta': 'the letter', 'escribe': 'it writes', 'escribes': 'you write',
        'escribo': 'I write', 'escribimos': 'we write', 'escriben': 'they write', 'leo': 'I read',
        'lees': 'you read', 'leemos': 'we read', 'los niños': 'the boys', 'las niñas': 'the girls', 'we read': 'we read',
        'I will eat': 'comeré', 'you will eat': 'comerás', 'he/she will eat': 'comerá',
        'I ate': 'comí', 'you ate': 'comiste', 'he/she ate': 'comió',
        'I am eating': 'estoy comiendo', 'you are eating': 'estás comiendo', 'he/she is eating': 'está comiendo',
        'I will drink': 'beberé', 'you will drink': 'beberás', 'he/she will drink': 'beberá',
        'I drank': 'bebí', 'you drank': 'bebiste', 'he/she drank': 'bebió',
        'I am drinking': 'estoy bebiendo', 'you are drinking': 'estás bebiendo', 'he/she is drinking': 'está bebiendo',
    }
# Create English Dictionary by swapping keys and values
english_dict = {v: k for k, v in create_translator_english.items()}

# Print the English Dictionary
print(english_dict)
