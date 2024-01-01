def create_translator_spanish():
    return {
        'the man': 'el hombre', 'the woman': 'la mujer', 'I am': 'yo soy', 'the boy': 'el niño', 'the girl': 'la niña',
        'he': 'él', 'she': 'ella', 'eats': 'come', 'is': 'es', 'you': 'usted', 'you are': 'eres',
        'the apple': 'la manzana', 'the bread': 'el pan', 'I eat': 'como', 'you eat': 'comes',
        'the water': 'el agua', 'the milk': 'la leche', 'it drinks': 'bebe', 'I drink': 'bebo', 'you drink': 'bebes',
        'hello': 'hola', 'bye': 'adiós', 'good morning': 'buenos días', 'good night': 'buenas noches',
        'thank you': 'gracias', 'nice to meet you': 'mucho gusto', 'yes': 'sí', 'no': 'no', 'please': 'por favor',
        'you are welcome': 'de nada', 'I am sorry': 'lo siento', 'excuse me': 'perdón', 'I speak': 'hablo',
        'you speak': 'hablas', 'Spanish': 'español', 'English': 'inglés', 'sorry': 'disculpe',
        'we': 'nosotros', 'we are': 'somos', 'the men': 'los hombres', 'the women': 'las mujeres',
        'you all': 'ustedes', 'they are': 'son', 'we drink': 'bebemos', 'they': 'ellas', 'they drink': 'beben',
        'the': 'las', 'the boys': 'los niños', 'the girls': 'las niñas', 'the wine': 'el vino',
        'the book': 'el libro', 'the letter': 'la carta', 'it writes': 'escribe', 'you write': 'escribes',
        'I write': 'escribo', 'we write': 'escribimos', 'they write': 'escriben', 'I read': 'leo',
        'you read': 'lees', 'we read': 'leemos', 'the boys': 'los niños', 'the girls': 'las niñas', 'we read': 'leemos',
        'I will eat': 'comeré', 'you will eat': 'comerás', 'he/she will eat': 'comerá',
        'I ate': 'comí', 'you ate': 'comiste', 'he/she ate': 'comió',
        'I am eating': 'estoy comiendo', 'you are eating': 'estás comiendo', 'he/she is eating': 'está comiendo',
        'I will drink': 'beberé', 'you will drink': 'beberás', 'he/she will drink': 'beberá',
        'I drank': 'bebí', 'you drank': 'bebiste', 'he/she drank': 'bebió',
        'I am drinking': 'estoy bebiendo', 'you are drinking': 'estás bebiendo', 'he/she is drinking': 'está bebiendo',
    }



def translate_text(text, translator):
    words = text.lower().split()  # Convert to lowercase and split into words
    translated_words = [translator.get(word, word) for word in words]
    translated_text = ' '.join(translated_words)
    return translated_text

def main():
    translator = create_translator_spanish()

    while True:
        user_input = input("Enter text in English (or 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Exiting the translator.")
            break

        translated_text = translate_text(user_input, translator)
        print("Translated text:", translated_text)

if __name__ == "__main__":
    main()

