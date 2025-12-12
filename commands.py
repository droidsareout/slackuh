def list_commands():
    commands = {
        ".exit": "Exit this interface",
        ".help": "View this program's available commands.",
        ".add": "Add a question and its answer. [question], [answer]",
        ".delete": "Remove a question and its answer. [question number]",
        ".clear": "Clear questions and answers.",
        ".list": "View questions and their answers.",
    }

    print ("======== COMMANDS ========")
    for command, info in commands.items():
        print(f"{command}: {info}")
