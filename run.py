from commands import list_commands, add_question_answer

running_program = True

print("Slackuh \nType \".help\" for a list of commands.")

while running_program:
    sent_text = input(">> ")

    match sent_text:
        case ".exit":
            running_program = False
        case ".help":
            list_commands()
        case ".add":
            add_question_answer()
        case _:
            print("Error: Command doesn't exist.")
