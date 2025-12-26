questions_answers = {}
command_list = {
    ".exit": "Close the Slackuh interface.",
    ".help": "View Slackuh's commands.",
    ".add": "Add a question and its answer. [question] [answer]",
    ".remove": "Remove a question and its answer. [question #]",
    ".clear": "Clear all question and answers.",
    ".list": "View all questions and their answers.",
}

def list_commands():
    print("======= COMMANDS =======")
    for command, info in command_list.items():
        print(f"{command}: {info}")

def add_question_answer():
    question = input("Add question: ")
    answer = input("Add answer: ")

    questions_answers[question] = answer

    print(f"Added question \"{question}\" with answer \"{answer}\".")

def list_questions_answers():
    print("======= QUESTIONS & ANSWERS =======")
    for index, (key, value) in enumerate(questions_answers.items(), 1):
        print(f"{index}: {key}\n{value}")

def remove_question_answer():
    question_to_remove = input("Remove question #: ")
    question_to_remove = int(question_to_remove)

    key = list(questions_answers.keys())[question_to_remove - 1]
    del questions_answers[key]

    print(f"Removed question #{question_to_remove}")
