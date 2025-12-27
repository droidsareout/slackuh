questions_answers = {}
command_list = {
    ".exit": "Close the Slackuh interface.",
    ".help": "View Slackuh's commands.",
    ".add": "Add a question and its answer.",
    ".remove": "Remove a question and its answer.",
    ".clear": "Clear all questions and answers.",
    ".list": "View all questions and answers.",
}

def list_commands():
    print("======= COMMANDS =======")
    for command, info in command_list.items():
        print(f"{command}: {info}")

def add_question_answer():
    question = input("Add question: ")
    answer = input("Add answer: ")

    with open("material/questions.txt", "r") as file:
        question_number = sum(1 for line in file) + 1

        with open("material/questions.txt", "a") as file:
            file.write(f"#{question_number}: {question}\n")

    with open("material/answers.txt", "r") as file:
        answer_number = sum(1 for line in file) + 1

        with open("material/answers.txt", "a") as file:
            file.write(f"#{answer_number}: {answer}\n")

    print(f"Added question \"{question}\" with answer \"{answer}\".")

def list_questions_answers():
    print("======= QUESTIONS & ANSWERS =======")

    with open("material/questions.txt", "r") as file:
        questions_file_lines = file.readlines()

    with open("material/answers.txt", "r") as file:
        answers_file_lines = file.readlines()

    for questions_line, answers_line in zip(questions_file_lines, answers_file_lines):
        print(f"{questions_line.strip()}\n{answers_line}")

def remove_question_answer():
    question_to_remove = input("Remove question #: ")
    question_to_remove = int(question_to_remove)

    key = list(questions_answers.keys())[question_to_remove - 1]
    del questions_answers[key]

def clear_questions_answers():
    questions_answers.clear()
    print("Questions and answers cleared.")
