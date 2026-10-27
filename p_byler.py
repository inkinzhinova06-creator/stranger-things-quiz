"""
# Stranger Things Quiz Project

## Purpose
The purpose of this project is to develop an interactive quiz on the series
"Stranger Things", which will allow users to test their knowledge about 
the key events, characters and storylines of the cult series. 

The quiz promotes educational and entertaining interaction with the audience, 
stimulating interest in the details of the plot and 
motivating critical reflection on the viewed content.

In addition, the project aims to create a user-friendly and intuitive interface for participating 
in the survey, as well as to create an accurate and fair knowledge assessment mechanism with subsequent 
preservation of the results.

The release of the final episode on December 31 makes the project especially timely, 
allowing users to revisit the story just before the official conclusion.

## Input and output format

# Input
- The user presses Enter to start the quiz
- For each question the user chooses an answer by typing 1, 2, or 3 in the terminal

# Output
- The program prints the introduction text exerting it from the file
- Displays each question and its answer options in the terminal
- Outputs the final score result message
- Saves the result message to result.txt

! Our tables with answers and corresponding final scores and phrases as well as input and output examples are in the file test_tables.txt !

Group: Monaenkova, Chavdar, Rogozina, Inkinzhinova, Lavrentyeva
"""


# downloading text from a file: a welcome text that will be shown before the test
def load_intro(): # defining a function with the name load_intro
    with open("intro.txt", "r", encoding="utf-8") as f: # opening text file in a "read" mode
        return f.read() # reading the entire text and returns it as a string, then complete the execution of the function and return the value (without printing it)

# a block with questions: it contains the questions, possible answers, points for each option (which one is correct)
questions = [ # variable "questions" itself is a list, but every question is a dictionary that contains key and values
    {
        "question": "Кто отправил посылку Джойс из России в 4 сезоне?", # key: "question", value: "Кто отправил посылку Джойс из России в 4 сезоне?"
        "answers": ["Хоппер", "Энзо", "Джонатан"],                      # key: "answers", values: ["Хоппер", "Энзо", "Джонатан"] - it is a list
        "points": [0, 10, 0]                                            # key: "points", values: [0, 10, 0]  - it is a list too, but with integers
    },                                                                  # so the right answer is "Энзо", as both lists (answers and points) are in the same order
    {                                                                   # answer index == points index
        "question": "Какой номер у сестры Эл, которая была найдена во втором сезоне?",
        "answers": ["008", "001", "010"],                               
        "points": [10, 0, 0]
    },
    {
        "question": "Кто помешал Лукасу спасти Макс?",
        "answers": ["Эрика", "Джейсон Карвер", "Эдди"],
        "points": [0, 10, 0]
    },
    {
        "question": "Байлер эндгейм?",                # It is a joke question!!
        "answers": ["Да", "100% да", "Конечно"],      # u
        # sers can get bonus 10 points thanks to it, as all answers are true :))))
        "points": [10, 10, 10]
    },
    {
        "question": "В какой штат переехала Джойс с Джонатаном, Уиллом и Эл",
        "answers": ["Калифорния", "Индиана", "Техас"],
        "points": [10, 0, 0]
    },
    {
        "question": "Когда пропал Уилл?",
        "answers": ["6 октября", "10 ноября", "6 ноября"],
        "points": [0, 0, 10]
    },
    {
        "question": "Как Дастин называл демогоргонов во втором сезоне?",
        "answers": ["Демопсы", "Демоны", "Демогоргоны"],
        "points": [10, 0, 0]
    },
    {
        "question": "Какую песню Джонатан впервые включил Уиллу когда родители ругались?",
        "answers": ["Running up that hill", "Should I stay or should I go", "Every breath you take"],
        "points": [0, 10, 0]
    },
    {
        "question": "Какая любимая игра Уилла?",
        "answers": ["Dungeons and dragons", "Baldur's Gate", "Hellfire Club"],
        "points": [10, 0, 0]
    },
    {
        "question": "За что избили Дастина в 5 сезоне?",
        "answers": ["За длинные волосы", "За футболку", "За татуировку"],
        "points": [0, 10, 0]
    },
]

def get_result(score): # declares the function "get_result" with parameter "score". This is the number of points (0-100) which is passed from "main()" function (function "main()" is located lower). Without the parameter, the function "get_result" wouldn't know the player's score and wouldn't be able to estimate the result of a player.
    if score >= 80: # checks if the score is more than or equal to 80 points (80-100 points)
        return "Ты настоящий эксперт Stranger Things!" # if the above condition is met, returns the string "Ты — настоящий эксперт Stranger Things!" and stops the function
    elif score >= 50: # if the first condition is not met, checks if the score is more than or equal to 50 points (50-79 points)
        return "Ты хорошо знаешь сериал." # if the above (second) condition is met, returns the string "Ты хорошо знаешь сериал." and stops the function
    else: # if both the first and second conditions are not met, "else" catches all the remaining scores (0-49 points)
        return "Ты только начинаешь знакомство со Stranger Things." # returns the string "Ты только начинаешь знакомство со Stranger Things." and stops the function

def save_result(text): # declares the function "save_result" with parameter "text". This is the string which is passed from "get_result()" function during the performance of the "main()" function. Without the parameter, the function "save_result" wouldn't know the player's result and wouldn't be able to record the result of a player into a text file.
    with open("result.txt", "w", encoding="utf-8") as f: # function "open("result.txt", "w")" creates (if it does not exist) or opens (if it exists) file "result.txt". "w" opens the file in write mode, which implies overwriting existing content - replacing existing content in the file with the new one. "encoding="utf-8" allows our text file to support Cyrillic letters, without it the Russian text wouldn't be shown correctly. "with ... as ..." auto-closes the file after all the operations with it are performed, it allows us not to close the file manually and make the code more reliable. "as f" assigns the file object we opened to variable which is named "f".
        f.write(text) # writes the string to the file "result.txt" which is represented by the variable "f". The text comes from the parameter. The method "write()" takes a string and saves it into the file, replacing the existing content in it.

def main(): # declares the main function "main" that starts the quiz
    print(load_intro()) # calls "load_intro", gets the intro text from the file and prints it to the screen
    input("Нажми Enter, чтобы начать...\n") # waits for the user to press Enter so that the quiz does not start immediately

    score = 0 # initializes the variable "score" with value 0 to store the total number of points

    for q in questions: # starts a loop that goes through each question dictionary in the list "questions"
        print("\n" + q["question"]) # prints an empty line and then prints the question text taken from the "question" key
        for a in q["answers"]: # starts an inner loop that goes through every answer option in the list under the "answers" key
            print(a) # prints the current answer option so that the user can see all three variants

        choice = input("Твой выбор (1-3): ") # requesting the user to select an answer option from 1 to 3
        while choice not in ["1", "2", "3"]: # the choice not in condition ["1", "2", "3"] means that the value of choice is NOT in the list of acceptable values
            print("\nВведите 1, 2 или 3.") # until the user enters the correct option (not "1", not "2", not "3"), the cycle will repeat over and over again.

            choice = input("Твой выбор (1-3): ") # requesting input again

        choice = int(choice) # convert a string to a number

        score += q["points"][choice - 1] # increases "score" by the number of points corresponding to the chosen answer (index is choice - 1 because lists start from 0)

    result = get_result(score) # calls "get_result" with the final score to get the text description of the result
    print("\nВаш результат:", result) # prints an empty line and then prints the text "Your result:" together with the result string
    save_result(result) # calls "save_result" to write the result text into the file "result.txt"

    print("\nРезультат сохранён в result.txt!") # prints a message informing the user that the result was saved to the file

if __name__ == "__main__": # checks if the current file is the main program and not imported as a module
    main() # calls the "main" function to start the quiz



