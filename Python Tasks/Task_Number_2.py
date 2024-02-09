
# Name : Muhammad Hanzala Khan
# Roll No: 102495
# Email : hanzalakhan6226@gmail.com

# use for random question
import random


class Question:
    def __init__(self, prompt, options, correct_option):
        self.prompt = prompt
        self.options = options
        self.correct_option = correct_option

    def display_question(self):
        print(self.prompt)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    def is_correct(self, user_answer):
        return user_answer == self.correct_option


def run_quiz(questions, attempts):
    selected_questions = random.sample(questions, attempts)
    score = 0

   # make loop function for selected question
    
    for question in selected_questions:
        question.display_question()
        while True:
            try:
                user_answer = int(input("Enter the number of your answer: "))
                if 1 <= user_answer <= len(question.options):
                    break
                else:
                    print(f"Please enter a number between 1 and {len(question.options)}")
            except ValueError:
                print("Please enter a valid number.")

        if question.is_correct(user_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question.correct_option}: {question.options[question.correct_option - 1]}\n")

    print(f"You got {score}/{attempts} questions correct.")


def main():
    # Create a list of 25 Question objects
    
    questions = [
        Question("What is the capital of France?", ["Berlin", "Paris", "London", "Madrid"], 2),
        Question("What is the largest planet in our solar system?", ["Mars", "Jupiter", "Venus", "Saturn"], 2),
        Question("Who is the author of 'Romeo and Juliet'?", ["Charles Dickens", "Jane Austen", "William Shakespeare", "Mark Twain"], 3),
       
        # Add more questions here...
       
        Question("What is the chemical symbol for gold?", ["Au", "Ag", "Hg", "Fe"], 1),
        Question("Which is the longest river in the world?", ["Amazon", "Nile", "Yangtze", "Mississippi"], 2),
        Question("What is the powerhouse of the cell?", ["Nucleus", "Chloroplast", "Mitochondria", "Ribosome"], 3),
        Question("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"], 1),
        Question("What is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], 4),
        Question("What is the boiling point of water in Celsius?", ["100°C", "0°C", "50°C", "200°C"], 1),
        
        # Add more questions as needed...
    ]

    # Number of attempts allowed
    attempts = 5

    # Run the quiz with limited attempts
    run_quiz(questions, attempts)


if __name__ == "__main__":
    main()
