question_answers = {}


def list_commands():
    commands = {
        "exit": "Close the Slackuh interface.",
        "help": "View Slackuh's commands.",
        "add": "Add a question and its answer. [question] [answer]",
        "delete": "Remove a question and its answer. [question #]",
        "clear": "Clear all question and answers.",
        "list": "View all questions and their answers.",
    }

    print("===== COMMANDS =====")
    for command, info in commands.items():
        print(f"{command}: {info}")
