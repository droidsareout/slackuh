question_answers = {}
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
    question = input("Question: ")
    answer = input("Answer: ")

    question_answers[question] = answer

    print(f"Added question \"{question}\" with answer \"{answer}\".")

def list_questions_answers():
    print("======= QUESTIONS & ANSWERS =======")
    for index, (key, value) in enumerate(question_answers.items(), 1):
        print(f"{index}: {key}\n{value}")

def remove_question_answer():
    question_to_remove = input("Remove question #: ")
    question_to_remove = int(question_to_remove)

    key = list(question_answers.keys())[question_to_remove - 1]
    del question_answers[key]

    print(f"Removed question #{question_to_remove}")
