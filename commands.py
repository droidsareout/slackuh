question_answers = {}
command_list = {
    ".exit": "Close the Slackuh interface.",
    ".help": "View Slackuh's commands.",
    ".add": "Add a question and its answer. [question] [answer]",
    ".delete": "Remove a question and its answer. [question #]",
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
