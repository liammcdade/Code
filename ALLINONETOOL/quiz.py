
import random

quiz_questions = {
    "What is the capital city of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the largest planet in our solar system?": "Jupiter",
    "In which year did World War I begin?": "1914",
    "What is the currency of Japan?": "Japanese Yen",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the chemical symbol for gold?": "Au",
    "Which ocean is the largest?": "Pacific Ocean",
    "What is the capital city of Australia?": "Canberra",
    "Who is the author of 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the capital of Canada?": "Ottawa",
    "In what year did the Titanic sink?": "1912",
    "Who was the first President of the United States?": "George Washington",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the largest mammal in the world?": "Blue Whale",
    "Who wrote '1984'?": "George Orwell",
    "What is the capital of Brazil?": "Brasília",
    "In which year did World War II end?": "1945",
    "What is the currency of China?": "Chinese Yuan",
    "Who discovered penicillin?": "Alexander Fleming",
    "What is the capital of South Africa?": "Pretoria (one of the three capitals)",
    "Who wrote 'Pride and Prejudice'?": "Jane Austen",
    "What is the chemical symbol for water?": "H2O",
    "Which mountain is the tallest in the world?": "Mount Everest",
    "In what year did the Berlin Wall fall?": "1989",
    "Who painted 'Starry Night'?": "Vincent van Gogh",
    "What is the capital city of Russia?": "Moscow",
    "What is the largest bird in the world?": "Ostrich",
    "Who is known as the 'Father of Computer Science'?": "Alan Turing",
    "What is the currency of India?": "Indian Rupee",
    "Who wrote 'The Great Gatsby'?": "F. Scott Fitzgerald",
    "What is the capital of Mexico?": "Mexico City",
    "In which year did the Apollo 11 mission land on the moon?": "1969",
    "Who painted the Sistine Chapel ceiling?": "Michelangelo",
    "What is the chemical symbol for oxygen?": "O2",
    "Which river is the longest in the world?": "Nile River",
    "What is the capital of Italy?": "Rome",
    "Who was the first woman to win a Nobel Prize?": "Marie Curie",
    "What is the currency of the United Kingdom?": "British Pound",
    "Who wrote 'Hamlet'?": "William Shakespeare",
    "What is the capital of China?": "Beijing",
    "In which year did the American Civil War end?": "1865",
    "What is the largest ocean on Earth?": "Pacific Ocean",
    "Who wrote 'The Catcher in the Rye'?": "J.D. Salinger",
    "What is the capital of Argentina?": "Buenos Aires",
    "In what year did the French Revolution begin?": "1789",
    "Who discovered the theory of relativity?": "Albert Einstein",
    "What is the currency of Germany?": "Euro",
    "Who painted 'The Persistence of Memory'?": "Salvador Dalí",
    "What is the capital city of Turkey?": "Ankara",
    "Who wrote 'Wuthering Heights'?": "Emily Brontë",
    "What is the chemical symbol for iron?": "Fe",
    "Which planet is known as the 'Morning Star' or 'Evening Star'?": "Venus",
    "In which year did Columbus reach the Americas?": "1492",
    "What is the capital of Spain?": "Madrid",
    "Who is known as the 'Queen of Pop'?": "Madonna",
    "What is the largest desert in the world?": "Antarctica (technically a cold desert)",
    "Who wrote 'The Odyssey'?": "Homer",
    "What is the chemical symbol for carbon dioxide?": "CO2",
    "Which mountain range is the longest in the world?": "Andes",
    "What is the capital of South Korea?": "Seoul",
    "Who was the first woman in space?": "Valentina Tereshkova",
    "Who wrote 'One Hundred Years of Solitude'?": "Gabriel García Márquez",
    "What is the capital city of Egypt?": "Cairo",
    "In what year did the Industrial Revolution begin?": "18th century (commonly associated with the late 1700s)",
    "Who discovered the laws of motion?": "Sir Isaac Newton",
    "What is the currency of Brazil?": "Brazilian Real",
    "Who painted 'The Last Supper'?": "Leonardo da Vinci",
    "What is the chemical symbol for gold?": "Au",
    "Which ocean is the smallest?": "Arctic Ocean",
    "Who wrote 'The Iliad'?": "Homer",
    "What is the capital of Saudi Arabia?": "Riyadh",
    "In which year did the Russian Revolution take place?": "1917",
    "What is the largest tree species in the world?": "Giant Sequoia",
    "Who is known as the 'Father of Modern Physics'?": "Albert Einstein",
    "What is the currency of France?": "Euro",
    "Who painted 'American Gothic'?": "Grant Wood",
    "What is the capital of Nigeria?": "Abuja",
    "In what year did the Renaissance begin?": "14th century",
    "What is the chemical symbol for silver?": "Ag",
    "Which river is known as the 'Cradle of Civilization'?": "Tigris and Euphrates",
    "What is the capital of South Korea?": "Seoul",
    "Who wrote 'Brave New World'?": "Aldous Huxley",
    "What is the largest island in the world?": "Greenland",
    "What is the currency of South Africa?": "South African Rand",
    "Who discovered penicillin?": "Alexander Fleming",
    "What is the capital city of Thailand?": "Bangkok",
    "In which year did the first manned moon landing occur?": "1969",
    "Who painted 'The Starry Night'?": "Vincent van Gogh",
    "What is the chemical symbol for helium?": "He",
    "Which planet is known as the 'Red Planet'?": "Mars",
    "Who wrote 'The Canterbury Tales'?": "Geoffrey Chaucer",
    "What is the capital of Turkey?": "Ankara",
    "In what year did the Battle of Hastings take place?": "1066",
    "What is the largest reptile in the world?": "Saltwater Crocodile",
    "Who is known as the 'Father of Medicine'?": "Hippocrates",
    "What is the currency of Mexico?": "Mexican Peso",
    "Who painted 'Girl with a Pearl Earring'?": "Johannes Vermeer",
    "What is the capital of Indonesia?": "Jakarta"
}



class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question)
        answer = input("Your answer: ")
        return answer.lower()

    def run_quiz(self, num_questions):
        # Convert dictionary items to a list of tuples
        question_items = list(self.questions.items())
        
        # Choose random questions based on user input
        random_questions = random.sample(question_items, k=min(num_questions, len(question_items)))

        for question, correct_answer in random_questions:
            user_answer = self.display_question(question)
            if user_answer == correct_answer.lower():
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {correct_answer}.\n")

        print(f"You scored {self.score}/{min(num_questions, len(question_items))}.")

if __name__ == "__main__":
    try:
        num_questions = int(input("How many questions would you like to answer (1 - 100)? "))
        if 1 <= num_questions <= 100:
            my_quiz = Quiz(quiz_questions)
            my_quiz.run_quiz(num_questions)  # Pass num_questions here
        else:
            print("Please enter a number between 1 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

