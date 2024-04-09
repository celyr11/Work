#Custom Quiz/Trivia Game
import random

def ask_question(Qbank, player):
    questions = list(set(Qbank) - set(player))
    if not questions:
        return None, None  
    Questionss = random.choice(questions)
    return Questionss, Qbank[Questionss]

def main():
    Qbank = {
        "Geography": [
            {"question": "What is the capital city of France?", "options": ["Paris", "Santo Domingo", "London", "Madrid", "Bueno Aires"], "Correct answer": 0},
            {"question": "Which continent is known as the Land Down Under?", "options": ["Asia", "Australia", "Africa", "Europe", "America"], "Correct answer": 1},
            {"question": "What is the longest river in the world?", "options": ["Amazon River", "Mississippi River", "Nile River", "Yangtze River", "Danube River"], "Correct answer": 0},
            {"question": "In which country is the Great Wall located?", "options": ["India", "Japan", "China", "Mongolia", "South Korea"], "Correct answer": 2},
            {"question": "What is the largest ocean on Earth?", "options": ["Pacific Ocean", "Arctic Ocean", "Southern Ocean", "Atlantic Ocean", "Indian Ocean"], "Correct answer": 0}
        ],
        "Astronomy": [
            {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Jupiter", "Venus", "Saturn", "Uranus"], "Correct answer": 0},
            {"question": "What is the largest planet in our solar system?", "options": ["Mars", "Jupiter", "Neptune", "Uranus", "Saturn"], "Correct answer": 1},
            {"question": "Which celestial body is Earth's natural satellite?", "options": ["Mars", "The Moon", "Saturn", "Jupiter", "Venus"], "Correct answer": 1},
            {"question": "What is the name of the closest star to Earth?", "options": ["Alpha Centauri", "Proxima Centauri", "Sirius", "Betelgeuse", "Vega"], "Correct answer": 1},
            {"question": "What is a group of stars forming a recognizable pattern called?", "options": ["Galaxy", "Nebula", "Constellation", "Quasar", "Supernova"], "Correct answerr": 2}
        ],
        "Language": [
            {"question": "What is the study of the origin and history of words called?", "options": ["Syntax", "Phonetics", "Etymology", "Morphology", "Semantics"], "Correct answer": 2},
            {"question": "What do you call a word that is spelled the same backward as forward?", "options": ["Synonym", "Antonym", "Palindrome", "Anagram", "Homonym"], "Correct answer": 2},
            {"question": "Which language is known as the language of love?", "options": ["Spanish", "Italian", "German", "French", "Portuguese"], "Correct answer": 3},
            {"question": "What is the term for words that sound like the noise they describe", "options": ["Onomatopoeia", "Alliteration", "Simile", "Metaphor", "Hyperbole"], "Correct answer": 0},
            {"question": "In grammar, what is the term for a word that replaces a noun?", "options": ["Pronoun", "Adjective", "Verb", "Conjunction", "Adverb"], "Correct answer": 0}
        ],
        "History": [
            {"question": "Who was the first President of the United States?", "options": ["George Washington", "Thomas Jefferson", " John Adams", "James Madison", "Benjamin Franklin"], "Correct answer": 0},
            {"question": "In which year did Christopher Columbus first reach America?", "options": ["1607", "1492", "1776", "1812", "1498"], "Correct answer": 1},
            {"question": "The Renaissance was a period known for its revival of interest in:", "options": ["Art and Learning", "Science", "Religion", "Exploration", "Trade"], "Correct answer": 0},
            {"question": "Who was the leader of the Civil Rights Movement in the United States and is known for his I Have a Dream speech?", "options": ["Malcolm X", "Rosa Parks", "Martin Luther King Jr.", "Thurgood Marshall", "Harriet Tubman"], "Correct answer": 2},
            {"question": "In which war did the Battle of Gettysburg take place?", "options": ["American Civil War", "World War I", "World War II", "Vietnam War", "Korean War"], "Correct answer": 0}
        ],
    }

    player = []
    finalscore = 0
    attempts = 0

    while attempts < 10:
        category, Q_options = ask_question(Qbank, player)
        if category is None:
            print("There are no more questions available. Game over!")
            break

        print(f"/nCategory: {category}")
        print("Question:", Q_options["Question"])
        for i, options in enumerate(Q_options["Options"], 1):
            print(f"{i}. {options}")

        try:
            answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input, enter a number.")
            continue

        attempts += 1

        if options["Answer"] == answer - 1:
            print("Correct!\n")
            finalscore += 1
            player.append(category)  
        else:
            print(f"Your answer is wrong!{Q_options['Options'][Q_options['The answer was: ']]}\n")

        print(f"Player's final score: {finalscore}/10")

    print(f"Final score: {finalscore}/10.")
    if finalscore >= 7:
        print("You won!!")
    else:
        print("You lose..")

    main()