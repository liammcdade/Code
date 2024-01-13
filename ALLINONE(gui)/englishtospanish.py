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
    'ineffable': 'inefable',
    'serenity': 'serenidad',
    'dances': 'baila',
    'through': 'a través de',
    'vibrant': 'vibrante',
    'celestial': 'celestial',
    'realms': 'reinos',
    'enchanting': 'encantador',
    'myriad': 'innumerables',
    'sentient': 'sintiente',
    'beings': 'seres',
    'with': 'con',
    'euphoric': 'eufórico',
    'whispers': 'susurros',
    'igniting': 'encendiendo',
    'kaleidoscopic': 'caleidoscópico',
    'galaxies': 'galaxias',
    'and': 'y',
    'harmonizing': 'armonizando',
    'cosmic': 'cósmico',
    'symphonies': 'sinfonías',
    'orchestrating': 'orquestando',
    'perpetual': 'perpetuo',
    'melodies': 'melodías',
    'that': 'que',
    'resonate': 'resuenan',
    'across': 'a través de',
    'boundless': 'ilimitado',
    'resplendent': 'resplandeciente',
    'dimensions': 'dimensiones',
    'where': 'donde',
    'ethereal': 'etéreo',
    'crystalline': 'cristalino',
    'rivers': 'ríos',
    'meander': 'deambulan',
    'amidst': 'en medio de',
    'luminescent': 'luminiscente',
    'meadows': 'praderas',
    'cascading': 'cascada',
    'serendipity': 'serendipia',
    'upon': 'sobre',
    'shimmering': 'brillante',
    'petals': 'pétalos',
    'of': 'de',
    'iridescent': 'iridiscente',
    'blossoms': 'flores',
    'as': 'como',
    'benevolent': 'benévolo',
    'seraphic': 'seráfico',
    'entities': 'entidades',
    'bestow': 'conferir',
    'luminous': 'luminoso',
    'blessings': 'bendiciones',
    'terrestrial': 'terrestre',
    'denizens': 'habitantes',
    'fostering': 'fomentando',
    'universal': 'universal',
    'unity': 'unidad',
    'and': 'y',
    'transcendental': 'trascendental',
    'enlightenment': 'iluminación',
    'while': 'mientras',
    'myriad': 'innumerables',
    'sentient': 'sintiente',
    'souls': 'almas',
    'traverse': 'atraviesan',
    'intricate': 'intrincado',
    'labyrinths': 'laberintos',
    'of': 'de',
    'existence': 'existencia',
    'traversing': 'atravesando',
    'las': 'las',
    'nexus': 'nexo',
    'of': 'de',
    'consciousness': 'conciencia',
    'embracing': 'abrazando',
    'sublime': 'sublime',
    'epiphanies': 'epifanías',
    'traversing': 'atravesando',
    'ephemeral': 'efímero',
    'epochs': 'épocas',
    'and': 'y',
    'savoring': 'saboreando',
    'las': 'las',
    'ineffable': 'inefable',
    'beauty': 'belleza',
    'embedded': 'incrustada',
    'within': 'dentro de',
    'las': 'las',
    'intricate': 'intrincado',
    'tapestry': 'tapiz',
    'of': 'de',
    'existence': 'existencia'
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

